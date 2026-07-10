path = r"e:\Shipwright-wind-waker-style-cel-shading\soh\soh\SohGui\Localization.cpp"
lines = open(path, encoding="utf-8").read().split("\n")

# find map region
start = next(i for i, s in enumerate(lines) if "gChineseTable" in s)
# find map open brace
semi = None
for i in range(start, len(lines)):
    if lines[i].count("{") and "gChineseTable" in lines[i]:
        # open brace is on this or next; find first '{' after gChineseTable
        pass
# simpler: find the '};' that closes the table
end = next(i for i in range(start, len(lines)) if lines[i].strip() == "};")

print("map region lines", start+1, "..", end+1)

bad = []
for i in range(start, end):
    s = lines[i].rstrip()
    if s.endswith("}") and not s.endswith("},") and not s.endswith("};"):
        nxt = lines[i+1].lstrip() if i+1 <= end else ""
        if nxt.startswith("{"):
            bad.append((i+1, "MISSING COMMA before next entry", s[:60]))
    # also detect a stray '{' that opens a nested initializer: line starts with '{' but previous valid
# also: an entry line that has '{' count != '}' count (unbalanced braces in entry frame)
for i in range(start, end):
    s = lines[i]
    if s.count("{") != s.count("}"):
        bad.append((i+1, "brace imbalance %d/%d" % (s.count("{"), s.count("}")), s[:60]))

for b in bad[:50]:
    print(b)
print("total suspicious:", len(bad))
