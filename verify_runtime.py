import re, glob, os
root = r'e:\Shipwright-wind-waker-style-cel-shading\soh\soh\SohGui'

def decode(s):
    out=''; i=0; n=len(s)
    mp={'n':'\n','t':'\t','r':'\r','"':'"',"'":"'",'\\':'\\','/':'/','0':'\0'}
    while i<n:
        c=s[i]
        if c=='\\' and i+1<n:
            out+=mp.get(s[i+1],s[i+1]); i+=2
        else:
            out+=c; i+=1
    return out

loc = open(os.path.join(root, 'Localization.cpp'), encoding='utf-8', errors='ignore').read()
# Extract each { ... } entry; concatenate all string literals inside it as the key.
runtime_keys = set()
for entry in re.finditer(r'\{\s*((?:"(?:[^"\\]|\\.)*"\s*)+),', loc):
    # the key part is the FIRST run of concatenated literals (before the comma separating key/value)
    body = entry.group(1)
    lits = re.findall(r'"((?:[^"\\]|\\.)*)"', body)
    key_raw = ''.join(lits)
    runtime_keys.add(decode(key_raw))

missing = []
files = glob.glob(os.path.join(root,'*.cpp'))+glob.glob(os.path.join(root,'*.h'))+glob.glob(os.path.join(root,'*.hpp'))
for f in files:
    src = open(f, encoding='utf-8', errors='ignore').read()
    for m in re.finditer(r'StringHelper::Translate\(\s*("(?:[^"\\]|\\.)*"(?:\s*"[^"\\]+")*)', src):
        raw = m.group(1)
        full = decode(''.join(re.findall(r'"((?:[^"\\]|\\.)*)"', raw)))
        if full not in runtime_keys:
            missing.append((os.path.basename(f), full[:70]))
print('Translate() calls with NO matching key:', len(missing))
for x in missing:
    print('  ', x)
