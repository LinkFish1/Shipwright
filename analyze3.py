import re, io, glob, os

root = r'e:\Shipwright-wind-waker-style-cel-shading'
loc_path = root + r'\soh\soh\SohGui\Localization.cpp'
loc = io.open(loc_path, 'r', encoding='utf-8').read()
keys = set(m.group(1) for m in re.finditer(r'\{\s*"((?:[^"\\]|\\.)*)"\s*,\s*"((?:[^"\\]|\\.)*)"', loc))
print('table keys:', len(keys))

# Find all StringHelper::Translate("...") literal arguments across the whole repo
pat = re.compile(r'StringHelper::Translate\(\s*"((?:[^"\\]|\\.)*)"')
missing = []
for dirpath, _, fnames in os.walk(root):
    if 'build' in dirpath.split(os.sep) or '.git' in dirpath.split(os.sep):
        continue
    for fn in fnames:
        if not fn.endswith(('.cpp', '.h', '.hpp', '.c', '.cc')):
            continue
        fp = os.path.join(dirpath, fn)
        try:
            src = io.open(fp, 'r', encoding='utf-8', errors='ignore').read()
        except Exception:
            continue
        for m in pat.finditer(src):
            lit = m.group(1)
            if lit not in keys:
                rel = os.path.relpath(fp, root)
                missing.append((rel, lit))

uniq = sorted(set(missing))
print('Translate() literals NOT in table (count=%d):' % len(uniq))
for rel, lit in uniq:
    print('[%s] %r' % (rel, lit))
