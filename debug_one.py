import re, os
root = r'e:\Shipwright-wind-waker-style-cel-shading\soh\soh\SohGui'
loc = open(os.path.join(root, 'Localization.cpp'), encoding='utf-8', errors='ignore').read()

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

# find the Fisherman key in loc raw
for m in re.finditer(r'\{\s*"((?:[^"\\]|\\.)*)"\s*,\s*"((?:[^"\\]|\\.)*)"', loc):
    if 'Fisherman' in m.group(1):
        raw_key = m.group(1)
        print('RAW KEY:', repr(raw_key))
        print('DECODED KEY:', repr(decode(raw_key)))
        break

# Now find the Translate arg in Enhancements
src = open(os.path.join(root,'SohMenuEnhancements.cpp'), encoding='utf-8', errors='ignore').read()
for m in re.finditer(r'StringHelper::Translate\(\s*("(?:[^"\\]|\\.)*"(?:\s*"[^"\\]+")*)', src):
    raw = m.group(1)
    full = decode(''.join(re.findall(r'"((?:[^"\\]|\\.)*)"', raw)))
    if 'Fisherman' in full:
        print('RAW ARG:', repr(raw))
        print('DECODED ARG:', repr(full))
        break
