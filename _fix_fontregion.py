path = r"e:\Shipwright-wind-waker-style-cel-shading\soh\soh\SohGui\Localization.cpp"
L = open(path, encoding="utf-8").read().split("\n")

BS = chr(92)
Q = chr(34)
C = chr(44)

# find map closing '};'
semi = next(i for i, s in enumerate(L) if s.strip() == "};")
# operate only on the code region AFTER the map
n = 0
for i in range(semi + 1, len(L)):
    old = L[i]
    new = old.replace(BS + Q + C, Q + C)   # \",  -> ",
    if new != old:
        n += 1
        L[i] = new

open(path, "w", encoding="utf-8").write("\n".join(L))
print("fixed lines in post-map region:", n)
