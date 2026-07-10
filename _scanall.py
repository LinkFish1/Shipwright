import re
p = 'e:/Shipwright-wind-waker-style-cel-shading/soh/soh/SohGui/Localization.cpp'
lines = open(p, encoding='utf-8').read().split('\n')
# An escaped close-key delimiter: \" immediately followed by ", " (comma space quote = delimiter)
bad = []
for i, l in enumerate(lines, 1):
    if re.search(r'\\",\s"', l):
        bad.append((i, 'escaped-closekey-delim', l[:90]))
    if re.search(r',\s\\"', l):
        bad.append((i, 'escaped-openvalue-delim', l[:90]))
print('bad delimiter lines:', len(bad))
for b in bad:
    print(b)
