import json, re

rsk = json.load(open(r'_rsk.json', encoding='utf-8'))
import importlib.util
spec = importlib.util.spec_from_file_location("rsk_zh", r'_rsk_zh.py')
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
trans = mod.trans

loc = r'soh/soh/SohGui/Localization.cpp'
text = open(loc, encoding='utf-8').read()
marker = '    // __TRANSLATION_TAIL__'

# build dedup map EN->ZH
m = {}
missing = []
for rid, en in rsk.items():
    if rid in trans:
        m[en] = trans[rid]
    else:
        missing.append(rid)

def esc(s):
    # EN strings hold literal backslash-n (parsed from C++ source);
    # ZH strings hold REAL newlines (Python interpreted \n).
    # Normalize both to a proper C++ "\n" escape in the output.
    s = s.replace('\\', '\\\\')   # literal backslash -> two backslashes
    s = s.replace('\n', '\\n')    # real newline -> backslash-n
    s = s.replace('"', '\\"')     # quote -> backslash-quote
    return s

lines = []
for en, zh in m.items():
    lines.append('    { "%s", "%s" },' % (esc(en), esc(zh)))

block = '    // ---- randomizer option descriptions (RSK) ----\n' + '\n'.join(lines) + '\n'
text = text.replace(marker, block + marker, 1)
open(loc, 'w', encoding='utf-8').write(text)
print('written', len(m), 'unique desc entries')
print('MISSING translations for', len(missing), 'ids:')
print(missing)
