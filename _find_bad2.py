path = r"e:\Shipwright-wind-waker-style-cel-shading\soh\soh\SohGui\Localization.cpp"
lines = open(path, encoding="utf-8").read().split("\n")

# Only scan lines that look like table entries: start with optional spaces then '{'
import re
for ln, line in enumerate(lines, 1):
    s = line.strip()
    if not s.startswith("{"):
        continue
    # count unescaped double quotes
    cnt = 0
    esc = False
    for ch in line:
        if esc:
            esc = False
        elif ch == "\\":
            esc = True
        elif ch == '"':
            cnt += 1
    if cnt != 4:
        print(f"line {ln}: {cnt} unescaped quotes -> {line[:120]}")
