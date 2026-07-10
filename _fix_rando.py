import io, re

LOC = r'e:\Shipwright-wind-waker-style-cel-shading\soh\soh\SohGui\Localization.cpp'

def norm(s):       # collapse double-backslash (from earlier double-escape bug) -> single
    return s.replace('\\\\', '\\')
def unescape(s):
    s = s.replace('\\"', '"').replace('\\n', '\n').replace('\\\\', '\\')
    return s
def escape(s):
    s = s.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')
    return s

# canonical English key (real newline / real quote) -> canonical Chinese value
T = {
"This option is disabled due to other options making the game unbeatable.": "此选项因其他选项导致游戏无法通关而被禁用。",
"Closed as child": "儿童时期封闭",
"Fast": "快速",
"Free": "自由",
"FortressCarpenters": "堡垒木匠",
"GerudoKeys": "格鲁德钥匙",
"Greg as Reward": "以格雷格作为奖励",
"Greg as Wildcard": "以格雷格作为万用替代",
"BridgeRewardOptions": "开启桥奖励选项",
"RainbowBridge": "彩虹桥",
"GanonTrial": "加农试炼",
"MixedEntrances": "混合入口",
"This option is disabled since warp song locations are not shuffled.": "此选项因传送歌曲位置未被随机化而被禁用。",
"TriforceHunt": "三角力量狩猎",
"TriforceHuntTotalPieces": "三角力量狩猎总碎片数",
"MQDungeons": "MQ迷宫",
"MQDungeonsSelection": "MQ迷宫选择",
"ShuffleDungeonReward": "随机化地牢奖励",
"LinksPocket": "林克的口袋",
"Advancement": "进阶",
"Anything": "任意",
"Nothing": "无",
"Medallion": "徽章",
"Specific Count": "指定数量",
"Shopsanity": "商店疯狂",
"Cheap Balanced": "廉价均衡",
"Fixed": "固定",
"Range": "范围",
"Set By Wallet": "由钱包决定",
"One-Time Only": "仅一次",
"ShuffleScrubs": "随机化德库商人",
"ScrubsPrices": "德库商人价格",
"ShuffleBeehives": "随机化蜂巢",
"This option is disabled because Shuffle Beehives is not enabled.": "此选项因“随机化蜂巢”未启用而被禁用。",
"ShuffleCows": "随机化奶牛",
"Malon's hint points to a cow, so requires cows to be shuffled.": "玛隆的提示指向奶牛，因此需要奶牛被随机化。",
"All Pots": "全部花盆",
"All Grass": "全部草丛",
"All Crates": "全部木箱",
"ShuffleFishingPole": "随机化钓竿",
"This option is disabled since the fishing pole is not shuffled.": "此选项因钓竿未被随机化而被禁用。",
"Bean Merchant Only": "魔豆商人专属",
"All But Beans": "除魔豆外全部",
"ShuffleMerchants": "随机化商人",
"MerchantPrices": "商人价格",
"On (Separate)": "开启（独立）",
"On (Pack)": "开启（打包）",
"Shuffle100GSReward": "随机化100黄金骷髅奖励",
"There is no point to hinting 100 skulls if it is not shuffled.": "若未随机化，提示100个骷髅毫无意义。",
"ShuffleDekuStickBag": "随机化德库木棒袋",
"ShuffleDekuNutBag": "随机化德库坚果袋",
"Shuffle Overworld Fish": "随机化地面世界鱼类",
"Shuffle Both": "两者皆随机化",
"ShuffleGanonBossKey": "随机化加农头目钥匙",
"LacsRewardOptions": "LACS奖励选项",
"ShuffleKeyRings": "随机化钥匙环",
"SkipChildZelda": "跳过儿童塞尔达",
"BigPoeTargetCount": "大波埃目标数量",
"Poe Collector will just give you the item instead with 0 big poes.": "若大波埃数量为0，波埃收集者将直接给予你该物品。",
"Completed": "已完成",
"Shuffle": "随机化",
"GossipStoneHints": "流言石提示",
"Ambiguous": "模糊",
"Strong": "强",
"Very Strong": "极强",
"Progressive": "渐进",
"Condensed Progressive": "精简渐进",
"Scarce": "稀少",
"Minimal": "最少",
"Fairy Ocarina": "妖精陶笛",
"No Logic": "无逻辑",
"This option has been disabled because only one type of O2R has been loaded": "此选项已被禁用，因为仅加载了一种 O2R 类型",
"IncludeTycoonWallet": "包含富豪钱包",
"ShopsanityPrices": "商店疯狂价格",
"ShuffleDungeonsEntrances": "随机化地牢入口",
"ShuffleBossEntrances": "随机化头目入口",
"ShuffleOverworldEntrances": "随机化地面世界入口",
"ShuffleInteriorsEntrances": "随机化室内入口",
"ShuffleGrottosEntrances": "随机化洞窟入口",
"ShuffleThievesHideoutEntrances": "随机化盗贼藏身处入口",
"LogicRules": "逻辑规则",
"DoorOfTime": "时之门",
"ShuffleOcarinas": "随机化陶笛",
"ClosedForest": "封闭森林",
"ShuffleOverworldSpawns": "随机化地面世界出生点",
"DecoupleEntrances": "解耦入口",
"Deku Only": "仅德库",
"Song only": "仅歌曲",
"Always open": "始终开启",
"Stones": "精神石",
"Medallions": "徽章",
"Dungeon rewards": "迷宫奖励",
"Tokens": "令牌",
"Random Number": "随机数量",
"Adult": "成年",
"On + Ganon": "开启 + 加农",
"Full": "全部",
"Simple": "简单",
"Age Restricted": "年龄限制",
"Win": "胜利",
"Selection Only": "仅选择",
"End of Dungeons": "迷宫终点",
"Any Dungeon": "任意迷宫",
"Overworld": "野外",
"Anywhere": "任意地点",
"Own Dungeon": "所属迷宫",
"Disabled because the currently selected Gerudo Fortress Carpenters\n": "因当前所选的格鲁德堡垒木匠\n而禁用",
"setting and/or Gerudo Fortress Keys setting is incompatible with\n": "且/或格鲁德堡垒钥匙设置与之不兼容\n",
"having a Gerudo Fortress Keyring.": "拥有格鲁德堡垒钥匙环。",
"This option is disabled because Triforce Hunt is enabled.": "此选项因三角力量狩猎已启用而被禁用。",
"Ganon's Boss key\nwill instead be given to you after Triforce Hunt completion.": "加农的头目钥匙\n将在三角力量狩猎完成后给予你。",
"All Tokens": "全部令牌",
"Disabled because Shuffle Deku Stick Bag is on.": "因“随机化德库木棒袋”开启而禁用。",
"Disabled because Shuffle Deku Nut Bag is on.": "因“随机化德库坚果袋”开启而禁用。",
"Shuffle only Hyrule Loach": "仅随机化海拉鲁泥鳅",
"Shuffle Fishing Pond": "随机化钓鱼池",
"Mask of Truth": "真实面具",
"Stone of Agony": "痛苦之石",
'This option is disabled because "': '此选项因"',
' are shuffled to "': '被随机化为"',
'Loach hint is only available with "': '泥鳅提示仅在"',
' set to "': '设为"',
"\nas that's the only ": '\n因为这是唯一的',
"setting where you present the loach to the fishing pond owner.": "你向钓鱼池主人出示泥鳅时的设置。",
'This option is force-enabled because "': '此选项被强制启用，因为"',
' is set to "': '被设为"',
' is enabled.': '已启用。',
}

# fragment lines matched by clean English prefix (normalized key form)
FRAG = {
"This option is disabled because ": '此选项因"',
" are shuffled to ": '被随机化为"',
"Loach hint is only available with ": '泥鳅提示仅在"',
" set to ": '设为"',
"\nas that's the only ": '\n因为这是唯一的',
"setting where you present the loach to the fishing pond owner.": "你向钓鱼池主人出示泥鳅时的设置。",
"This option is force-enabled because ": '此选项被强制启用，因为"',
" is set to ": '被设为"',
" is enabled.": '已启用。',
}

GARBAGE = {
    '{ ") {',
    'if (StaticData::trickToEnum.contains(trick.GetNameTag())) {',
    'SPDLOG_ERROR(", ") {',
    'SPDLOG_ERROR(" },',
    '{ "seed", "seed" },',
    '{ "finalSeed", "finalSeed" },',
    '{ "settings", "settings" },',
}

lines = io.open(LOC, encoding='utf-8').read().split('\n')
out = []; removed = 0; changed = 0
pat = re.compile(r'^(\s*\{\s*)"((?:[^"\\]|\\.)*)"\s*,\s*"((?:[^"\\]|\\.)*)"(\s*\},?)\s*$')
for ln in lines:
    if ln.strip() in GARBAGE:
        removed += 1; continue
    m = pat.match(ln)
    if m:
        g1, key_raw, val_raw, g4 = m.group(1), m.group(2), m.group(3), m.group(4)
        nk = norm(key_raw)            # fix corrupted key (collapse \\ -> \)
        ckey = unescape(nk)
        new_val = None
        if ckey in T:
            new_val = escape(T[ckey])
        else:
            for pfx, fv in FRAG.items():
                if nk.startswith(pfx):
                    new_val = fv; break
        if new_val is None:
            new_val = norm(val_raw)   # keep (normalize if needed)
            out.append(g1 + '"' + nk + '", "' + new_val + '"' + g4); continue
        changed += 1
        out.append(g1 + '"' + nk + '", "' + new_val + '"' + g4); continue
    out.append(ln)

io.open(LOC, 'w', encoding='utf-8').write('\n'.join(out))
left = [l for l in out if l.strip() in GARBAGE]
print('removed garbage:', removed)
print('changed entries:', changed)
print('leftover garbage:', len(left))
