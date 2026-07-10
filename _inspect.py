p = 'e:/Shipwright-wind-waker-style-cel-shading/soh/soh/SohGui/Localization.cpp'
lines = open(p, encoding='utf-8').read().split('\n')
for n in (2305, 2565, 2581, 2938):
    line = lines[n]
    print('==== LINE', n + 1, 'len', len(line), '====')
    for i, ch in enumerate(line):
        if ch == '"':
            # count preceding backslashes
            j = i - 1
            bs = 0
            while j >= 0 and line[j] == '\\':
                bs += 1
                j -= 1
            esc = 'ESCAPED' if bs % 2 == 1 else 'plain  '
            print(f'  pos {i:3d} {esc}  ctx={line[max(0,i-3):i+4]!r}')
