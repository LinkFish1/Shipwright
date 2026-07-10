L = open(r"e:\Shipwright-wind-waker-style-cel-shading\soh\soh\SohGui\Localization.cpp", encoding="utf-8").read().split("\n")
Q = chr(34)
# map region lines 22..4676 (1-indexed); index 21..4675
bad = []
for i in range(21, 4676):
    s = L[i]
    if "};" in s:
        break
    if "} {" in s:                      # close brace, space, open brace => missing comma
        bad.append((i + 1, "missing-comma", s[:90]))
    if '", {' in s or ',"{' in s:       # value is a brace group
        bad.append((i + 1, "value-brace", s[:90]))
    # entry whose value looks like a bare brace group instead of string
    if s.strip().startswith("{") and ("{ {" in s or ", {" in s):
        bad.append((i + 1, "open-brace", s[:90]))
for b in bad[:50]:
    print(b)
print("total suspicious:", len(bad))
