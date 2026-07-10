import re

path = r"e:\Shipwright-wind-waker-style-cel-shading\soh\soh\SohGui\Localization.cpp"
src = open(path, encoding="utf-8").read()
lines = src.split("\n")

# Locate gChineseTable initializer braces
start = src.index("gChineseTable")
# find first '{' after 'gChineseTable =' or 'gChineseTable['
# We'll just scan char by char tracking brace depth and quote state.
i = src.index("{", start)
depth = 0
in_str = False
esc = False
str_start_line = None
bad = []
line_of = lambda pos: src.count("\n", 0, pos) + 1
for idx in range(i, len(src)):
    c = src[idx]
    if in_str:
        if esc:
            esc = False
        elif c == "\\":
            esc = True
        elif c == '"':
            in_str = False
            # record closing
    else:
        if c == '"':
            in_str = True
            str_start_line = line_of(idx)
        elif c == '{':
            depth += 1
        elif c == '}':
            depth -= 1
            if depth == 0:
                # end of map
                break
# Report: if we ended still in_str, the string at str_start_line is unterminated.
if in_str:
    print("UNCLOSED STRING starting at line", str_start_line)
else:
    print("No obviously unclosed string at EOF; scanning per-entry balance instead.")

# Per-entry scan: find each '{ "..." ... },' and validate quote balance within.
# Simpler: report the first line whose raw content, when re-parsed char-by-char,
# leaves in_str true at end of line (string spanning into next line) AND detect
# double-close by checking the entry structure.
in_str = False
esc = False
entry_open_line = None
for ln, line in enumerate(lines, 1):
    for ch in line:
        if in_str:
            if esc:
                esc = False
            elif ch == "\\":
                esc = True
            elif ch == '"':
                in_str = False
        else:
            if ch == '"':
                in_str = True
    if in_str:
        # string continues to next line
        pass
    # We just track; print lines where a string stays open across boundary
print("--- lines where a string literal is still open at end of line ---")
in_str = False
esc = False
for ln, line in enumerate(lines, 1):
    for ch in line:
        if in_str:
            if esc:
                esc = False
            elif ch == "\\":
                esc = True
            elif ch == '"':
                in_str = False
        else:
            if ch == '"':
                in_str = True
    if in_str:
        print("  open-at-EOL line", ln, "->", lines[ln-1][:90])
