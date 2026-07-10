import io, re, sys

LOC = r'e:\Shipwright-wind-waker-style-cel-shading\soh\soh\SohGui\Localization.cpp'
FONTS = [
    r'e:\Shipwright-wind-waker-style-cel-shading\x64\Release\DroidSansFallback.ttf',
    r'e:\Shipwright-wind-waker-style-cel-shading\soh\soh\SohGui\fonts\DroidSansFallback.ttf',
]

# --- parse gChineseTable entries ---
src = io.open(LOC, encoding='utf-8').read()
entry_re = re.compile(r'\{\s*"((?:[^"\\]|\\.)*)"\s*,\s*"((?:[^"\\]|\\.)*)"\s*\}')
# only entries inside gChineseTable (between the map's opening and the closing "};")
start = src.index('gChineseTable')
# find the first '{' after 'gChineseTable' that opens the initializer list
ob = src.index('{', start)
# find matching close '};'
depth = 0
i = ob
table_region = None
while i < len(src):
    if src[i] == '{':
        depth += 1
    elif src[i] == '}':
        depth -= 1
        if depth == 0:
            table_region = src[ob+1:i]
            break
    i += 1

entries = entry_re.findall(table_region)
print('entries parsed:', len(entries))

# decode C-style escapes in the value to real unicode (we only need the value's chars)
def unescape(s):
    # handle \n \t \\ \" and \x.. / \u.... minimally
    out = []
    j = 0
    while j < len(s):
        if s[j] == '\\' and j+1 < len(s):
            nxt = s[j+1]
            if nxt == 'n': out.append('\n')
            elif nxt == 't': out.append('\t')
            elif nxt == 'r': out.append('\r')
            elif nxt == '\\': out.append('\\')
            elif nxt == '"': out.append('"')
            else: out.append(nxt)
            j += 2
        else:
            out.append(s[j]); j += 1
    return ''.join(out)

# collect all chars used in VALUES (the Chinese text)
val_chars = {}
for k, v in entries:
    dec = unescape(v)
    for ch in dec:
        val_chars[ch] = val_chars.get(ch, 0) + 1

# --- load font cmap ---
def load_cmap(path):
    try:
        from fontTools.ttLib import TTFont
    except Exception as e:
        print('fontTools not available:', e); sys.exit(2)
    f = TTFont(path, fontNumber=0)
    cmap = f.getBestCmap()
    return set(cmap.keys())

for fp in FONTS:
    try:
        cps = load_cmap(fp)
    except Exception as e:
        print('FAILED to load', fp, e); continue
    print('FONT', fp)
    print('  font codepoints:', len(cps))
    missing = [ch for ch in val_chars if ord(ch) not in cps]
    nonascii = [ch for ch in missing if ord(ch) >= 0x80]
    print('  VALUE chars total distinct:', len(val_chars))
    print('  VALUE chars MISSING from this font (total):', len(missing))
    print('  === NON-ASCII missing (real tofu culprits):', len(nonascii))
    for ch in sorted(nonascii, key=lambda c: ord(c)):
        print('    U+%04X %r  (count=%d)' % (ord(ch), ch, val_chars[ch]))
    # also list the ascii missing for completeness
    ascii_missing = [ch for ch in missing if ord(ch) < 0x80]
    print('  (ascii missing, covered by base font, OK):', len(ascii_missing))
