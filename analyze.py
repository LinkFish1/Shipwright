import re, io

root = r'e:\Shipwright-wind-waker-style-cel-shading'
loc_path = root + r'\soh\soh\SohGui\Localization.cpp'

loc = io.open(loc_path, 'r', encoding='utf-8').read()
# Keys present in gChineseTable
keys = set(m.group(1) for m in re.finditer(r'\{\s*"((?:[^"\\]|\\.)*)"\s*,\s*"((?:[^"\\]|\\.)*)"', loc))

# All English UI strings already wrapped in Translate (these are handled if in table)
wrapped = set()
for f in __import__('glob').glob(root + r'\soh\soh\SohGui\*.cpp') + __import__('glob').glob(root + r'\soh\soh\SohGui\*.h') + __import__('glob').glob(root + r'\soh\soh\SohGui\*.hpp'):
    src = io.open(f, 'r', encoding='utf-8', errors='ignore').read()
    for m in re.finditer(r'StringHelper::Translate\(\s*"((?:[^"\\]|\\.)*)"', src):
        wrapped.add(m.group(1))

lines = io.open(root + r'\extracted_strings.txt', 'r', encoding='utf-8').read().split('\n')
if lines and lines[-1] == '':
    lines = lines[:-1]

print('total extracted:', len(lines))
print('total table keys:', len(keys))

# For each extracted line, is it already a key?
untranslated = []
for i, s in enumerate(lines, 1):
    if s in keys:
        continue
    untranslated.append((i, s))

print('extracted lines NOT in table:', len(untranslated))
print('--- first 30 untranslated (line#: text) ---')
for i, s in untranslated[:30]:
    print('%d: %r' % (i, s))
print('--- last 10 untranslated ---')
for i, s in untranslated[-10:]:
    print('%d: %r' % (i, s))
