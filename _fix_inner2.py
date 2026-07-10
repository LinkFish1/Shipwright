path = r"e:\Shipwright-wind-waker-style-cel-shading\soh\soh\SohGui\Localization.cpp"
L = open(path, encoding="utf-8").read().split("\n")

BS = chr(92)
Q = chr(34)

def unescaped_positions(s):
    esc = False
    pos = []
    for i, c in enumerate(s):
        if esc:
            esc = False
        elif c == BS:
            esc = True
        elif c == Q:
            pos.append(i)
    return pos

# only fix the two known broken single-line entries
for ln in (2306, 2939):
    idx = ln - 1
    s = L[idx]
    pos = unescaped_positions(s)
    # delimiters: first = open-key, last = close-value; the rest are inner quotes to escape
    inner = pos[1:-1]
    # insert backslashes from right to left to keep indices valid
    new = list(s)
    for p in sorted(inner, reverse=True):
        if new[p - 1] == BS:
            continue  # already escaped (shouldn't happen)
        new.insert(p, BS)
    L[idx] = "".join(new)
    print("line", ln, "escaped", len(inner), "inner quotes")

open(path, "w", encoding="utf-8").write("\n".join(L))
print("done")
