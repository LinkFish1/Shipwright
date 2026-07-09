import os

ROOT = r'e:/Shipwright-wind-waker-style-cel-shading/soh'
TARGETS = ('.cpp', '.h', '.c', '.hpp')
BOM = b'\xef\xbb\xbf'

def has_cjk(s):
    for ch in s:
        o = ord(ch)
        if o >= 0x2E80:  # CJK + fullwidth + punctuation ranges start here
            return True
    return False

count = 0
for dirpath, dirs, files in os.walk(ROOT):
    # skip build/extern
    if any(seg in dirpath for seg in ('/build/', '\\build\\', '/.git/', '\\.git\\')):
        continue
    for fn in files:
        if not fn.endswith(TARGETS):
            continue
        p = os.path.join(dirpath, fn)
        try:
            data = open(p, 'rb').read()
        except Exception:
            continue
        if data[:3] == BOM:
            continue
        # decode as utf-8 to confirm; only add BOM if it's valid utf-8 containing CJK
        try:
            txt = data.decode('utf-8')
        except UnicodeDecodeError:
            continue
        if not has_cjk(txt):
            continue
        open(p, 'wb').write(BOM + data)
        count += 1
        print('BOM added:', p.replace(ROOT, ''))
print('Total BOM added:', count)
