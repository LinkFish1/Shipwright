path = r"e:\Shipwright-wind-waker-style-cel-shading\soh\soh\SohGui\Localization.cpp"
text = open(path, encoding="utf-8").read()
lines = text.split("\n")

a = text.index("gChineseTable")
i = text.index("{", a)          # map open brace
n = len(text)
depth = 0
in_str = False
esc = False
entry_opens = []   # (entry_index, line_no)
lineno = text[:i].count("\n") + 1
k = i
while k < n:
    c = text[k]
    if in_str:
        if esc:
            esc = False
        elif c == "\\":
            esc = True
        elif c == '"':
            in_str = False
        if c == "\n":
            lineno += 1
        k += 1
        continue
    if c == '"':
        in_str = True
        if c == "\n":
            lineno += 1
        k += 1
        continue
    if c == "\n":
        lineno += 1
        k += 1
        continue
    if c == "{":
        if depth == 0:
            depth = 1          # map open
        else:
            # depth >= 1: this '{' opens an entry (depth 1->2) or nested (depth>=2)
            if depth == 1:
                entry_opens.append((len(entry_opens) + 1, lineno))
            depth += 1
        k += 1
        continue
    if c == "}":
        depth -= 1
        if depth == 0:
            break
        k += 1
        continue
    k += 1

print("total entries:", len(entry_opens))
# element 2744 (1-indexed)
target = 2744
if target <= len(entry_opens):
    idx, ln = entry_opens[target - 1]
    print("entry", target, "at line", ln)
    # print surrounding entries' lines
    for e in range(max(1, target - 2), min(len(entry_opens), target + 3) + 1):
        il, el = entry_opens[e - 1]
        print("  entry", e, "line", el, "->", lines[el - 1][:80])
else:
    print("only", len(entry_opens), "entries; target", target, "out of range")
