path = r"e:\Shipwright-wind-waker-style-cel-shading\soh\soh\SohGui\Localization.cpp"
lines = open(path, encoding="utf-8").read().split("\n")
out = []
for ln, line in enumerate(lines, 1):
    s = line.strip()
    if not s.startswith("{"):
        continue
    cnt = 0
    esc = False
    for ch in line:
        if esc:
            esc = False
        elif ch == "\\":
            esc = True
        elif ch == '"':
            cnt += 1
    if cnt not in (2, 4):
        out.append(f"line {ln}: {cnt} quotes -> {line[:110]}")
open(r"e:\Shipwright-wind-waker-style-cel-shading\_bad_lines.txt", "w", encoding="utf-8").write("\n".join(out))
print("total flagged:", len(out))
