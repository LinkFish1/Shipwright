import io, re

LOC = r'e:\Shipwright-wind-waker-style-cel-shading\soh\soh\SohGui\Localization.cpp'
SRC = r'e:\Shipwright-wind-waker-style-cel-shading\soh\soh\Enhancements\randomizer\settings.cpp'

def unescape(s):
    return s.replace('\\"', '"').replace('\\n', '\n').replace('\\\\', '\\')
def escape(s):
    return s.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')

# per-literal translation (canonical literal -> Chinese). Keys preserve source spellings
# ("avaliable", "Beehives", "Triforce") so they match the runtime string.
lit = {
 "This option is disabled due to other options making the game unbeatable.":
   "此选项因其他选项导致游戏无法通关而被禁用。",
 "This option is disabled since warp song locations are not shuffled.":
   "此选项因传送歌曲位置未被随机化而被禁用。",
 'This option is disabled because "Dungeon Rewards" are shuffled to "End of Dungeons".':
   '此选项因“地牢奖励”被随机化为“迷宫终点”而禁用。',
 'This option is disabled because "Dungeon Rewards" are shuffled to "Vanilla".':
   '此选项因“地牢奖励”被随机化为“原版”而禁用。',
 "This option is disabled because Shuffle Beehives is not enabled.":
   "此选项因“随机化蜂巢”未启用而被禁用。",
 "Malon's hint points to a cow, so requires cows to be shuffled.":
   "玛隆的提示指向奶牛，因此需要奶牛被随机化。",
 "This option is disabled since the fishing pole is not shuffled.":
   "此选项因钓竿未被随机化而被禁用。",
 "There is no point to hinting 100 skulls if it is not shuffled.":
   "若未随机化，提示100个骷髅毫无意义。",
 "Disabled because Shuffle Deku Stick Bag is on.":
   "因“随机化德库木棒袋”开启而禁用。",
 "Disabled because Shuffle Deku Nut Bag is on.":
   "因“随机化德库坚果袋”开启而禁用。",
 "Poe Collector will just give you the item instead with 0 big poes.":
   "若大波埃数量为0，波埃收集者将直接给予你该物品。",
 "This option has been disabled because only one type of O2R has been loaded":
   "此选项已被禁用，因为仅加载了一种 O2R 类型",
 "Disabled because the currently selected Gerudo Fortress Carpenters\n":
   "因当前所选的格鲁德堡垒木匠\n而禁用",
 "setting and/or Gerudo Fortress Keys setting is incompatible with\n":
   "且/或格鲁德堡垒钥匙设置与之不兼容\n",
 "having a Gerudo Fortress Keyring.":
   "拥有格鲁德堡垒钥匙环。",
 "This option is disabled because Triforce Hunt is enabled.":
   "此选项因三角力量狩猎已启用而被禁用。",
 "Ganon's Boss key\nwill instead be given to you after Triforce Hunt completion.":
   "加农的头目钥匙\n将在三角力量狩猎完成后给予你。",
 'Loach hint is only available with "Fishsanity" set to "Shuffle only Hyrule Loach"\nas that\'s the only ':
   '泥鳅提示仅在“钓鱼狂热”设为“仅随机化海拉鲁泥鳅”\n因为这是唯一的',
 "setting where you present the loach to the fishing pond owner.":
   "你向钓鱼池主人出示泥鳅时的设置。",
 'This option is force-enabled because "Ganon\'s Boss Key" is set to "100 GS Reward".':
   '此选项被强制启用，因为“加农的头目钥匙”被设为“100 黄金骷髅奖励”。',
 'This option is disabled because "Skip Child Zelda" is enabled.':
   '此选项因“跳过儿童塞尔达”已启用而被禁用。',
}

# --- parse Disable(...) calls in settings.cpp ---
src = io.open(SRC, encoding='utf-8').read()
calls = re.findall(r'\bDisable\((.*?)\);', src, re.S)
full = {}   # concatenated canonical key -> value
for args in calls:
    lits = re.findall(r'"((?:[^"\\]|\\.)*)"', args, re.S)
    canon = [unescape(x) for x in lits]
    key = ''.join(canon)
    val = ''.join(lit.get(c, c) for c in canon)
    if any(c not in lit for c in canon):
        print('WARN missing literal in:', key[:60])
    full[key] = val

print('Disable calls parsed:', len(calls), 'distinct full keys:', len(full))

# --- edit Localization.cpp ---
lines = io.open(LOC, encoding='utf-8').read().split('\n')
entry_re = re.compile(r'^\s*\{\s*"((?:[^"\\]|\\.)*)"\s*,\s*"((?:[^"\\]|\\.)*)"\s*\},?\s*$')
done = set()
out = []
for ln in lines:
    m = entry_re.match(ln)
    if m:
        key_raw = m.group(1)
        ck = unescape(norm(key_raw)) if False else unescape(key_raw)
        if ck in full:
            done.add(ck)
            newval = escape(full[ck])
            out.append('    { "%s", "%s" },' % (escape(ck), newval))
            continue
    out.append(ln)

# insert any full keys not already present, before TranslateImpl
newlines = []
for k, v in full.items():
    if k in done:
        continue
    newlines.append('    { "%s", "%s" },' % (escape(k), escape(v)))
ins = None
for i, ln in enumerate(out):
    if 'static std::string TranslateImpl' in ln:
        ins = i
        break
if ins is None:
    raise SystemExit('TranslateImpl anchor not found')
out[ins:ins] = newlines

io.open(LOC, 'w', encoding='utf-8').write('\n'.join(out))
print('upserted existing:', len(done), 'inserted new:', len(newlines))
