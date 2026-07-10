path = r"e:\Shipwright-wind-waker-style-cel-shading\soh\soh\SohGui\Localization.cpp"
L = open(path, encoding="utf-8").read().split("\n")

# find the map closing '};'
semi = -1
for i in range(4660, 4690):
    if "};" in L[i]:
        print("possible }; at", i + 1, repr(L[i][:40]))
        semi = i
print("chosen semi line", semi + 1)

# scan post region for \"
cnt = 0
BS = chr(92)
Q = chr(34)
for i in range(semi + 1, len(L)):
    s = L[i]
    j = 0
    while True:
        k = s.find(BS + Q, j)
        if k < 0:
            break
        cnt += 1
        if cnt <= 60:
            print("  line", i + 1, "ctx", repr(s[max(0, k - 25):k + 25]))
        j = k + 2
print("total \\quote in post region:", cnt)
