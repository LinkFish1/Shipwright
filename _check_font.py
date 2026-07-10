import re, io

LOC  = r'e:\Shipwright-wind-waker-style-cel-shading\soh\soh\SohGui\Localization.cpp'

# ImGui GetGlyphRangesChineseSimplifiedCommon (the set any DroidSansFallback covers)
COMMON = [(0x0020,0x00FF),(0x3000,0x303F),(0x3400,0x4DBF),
           (0x4E00,0x9FFF),(0xFF00,0xFFEF)]
def in_common(cp):
    for lo,hi in COMMON:
        if lo<=cp<=hi: return True
    return False

# also: deposit Latin-1 supplement already covered; allow ASCII punctuation etc.
src = io.open(LOC, encoding='utf-8').read()
m = re.search(r'gChineseTable\s*=\s*\{(.*?)\n\};', src, re.S)
block = m.group(1)
block_start_line = src[:m.start(1)].count('\n') + 1
entry_re = re.compile(r'\{\s*"((?:[^"\\]|\\.)*)"\s*,\s*"((?:[^"\\]|\\.)*)"\s*\}')

rows = []
for em in entry_re.finditer(block):
    key = em.group(1); val = em.group(2)
    line = block_start_line + block[:em.start()].count('\n') + 1
    rows.append((line, key, val))

print('total entries:', len(rows))

# ---- A) out-of-common CJK chars in value ----
cjk = [(0x3400,0x4DBF),(0x4E00,0x9FFF),(0x20000,0x2A6DF),(0xF900,0xFAFF)]
def is_cjk(cp):
    for lo,hi in cjk:
        if lo<=cp<=hi: return True
    return False

out_common = []  # (line, key, chars)
for line,key,val in rows:
    bad=set()
    for ch in val:
        cp=ord(ch)
        if is_cjk(cp) and not in_common(cp):
            bad.add(ch)
    if bad:
        out_common.append((line,key,''.join(sorted(bad))))
print('\n=== OUT-OF-COMMONSET CJK CHARS (%d entries) ===' % len(out_common))
with io.open('_font_missing.txt','w',encoding='utf-8') as fh:
    for line,key,bad in out_common:
        fh.write('%d\t%s\t%s\n'%(line,key,bad))
        print('%d  key=%-38s  chars=%s'%(line,key[:38],bad))

# ---- B) untranslated (value == key) ----
untr=[ (line,key) for line,key,val in rows if key==val ]
print('\n=== UNTRANSLATED (value==key): %d ===' % len(untr))
for line,key in untr:
    print('%d  %s'%(line,key))
