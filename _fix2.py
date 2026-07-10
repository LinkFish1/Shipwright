p = 'e:/Shipwright-wind-waker-style-cel-shading/soh/soh/SohGui/Localization.cpp'
lines = open(p, encoding='utf-8').read().split('\n')

# Line 2306 (index 2305): close-key and open-value are escaped, must be plain.
l = lines[2305]
old = 'Anywhere\\".\\", \\"将地图'
new = 'Anywhere\\".", "将地图'
assert old in l, '2306 target not found: ' + repr(l)
lines[2305] = l.replace(old, new, 1)

# Line 2939 (index 2938): close-key and open-value are escaped, must be plain.
l = lines[2938]
old = 'Truth\\" for exceptions.\\", \\"移除'
new = 'Truth\\" for exceptions.", "移除'
assert old in l, '2939 target not found: ' + repr(l)
lines[2938] = l.replace(old, new, 1)

open(p, 'w', encoding='utf-8').write('\n'.join(lines))
print('fixed 2306 and 2939')
