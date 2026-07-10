import io

path = r"e:\Shipwright-wind-waker-style-cel-shading\soh\soh\SohGui\Localization.cpp"
src = open(path, encoding="utf-8").read()
lines = src.split("\n")

def unescaped_quotes(s):
    pos = []
    esc = False
    for i, ch in enumerate(s):
        if esc:
            esc = False
        elif ch == "\\":
            esc = True
        elif ch == '"':
            pos.append(i)
    return pos

fixed = 0
for ln in range(len(lines)):
    line = lines[ln]
    if not line.lstrip().startswith("{"):
        continue
    pos = unescaped_quotes(line)
    if len(pos) in (2, 4):
        continue  # ok (multi-line continuation or valid)
    if len(pos) < 4:
        continue
    n = len(pos)
    open_key = pos[0]
    close_value = pos[-1]
    # close_key: the quote p where after it (ignore spaces) comes ','
    close_key = None
    for p in pos[1:]:
        after = line[p+1:]
        if after.lstrip().startswith(','):
            close_key = p
            break
    # open_value: the quote q where before it (ignore spaces) is ','
    open_value = None
    for q in pos[1:]:
        before = line[:q]
        if before.rstrip().endswith(','):
            open_value = q
            break
    delims = {open_key, close_key, open_value, close_value}
    # escape inner quotes (build new string right-to-left to keep indices valid)
    new = list(line)
    for p in sorted(delims, reverse=True):
        # ensure it's a plain quote (not already escaped) - by definition it is unescaped
        pass
    # Insert backslash before each non-delimiter unescaped quote
    inserts = [p for p in pos if p not in delims]
    for p in sorted(inserts, reverse=True):
        # make sure not already preceded by backslash
        if p > 0 and new[p-1] == '\\':
            continue
        new.insert(p, '\\')
    lines[ln] = ''.join(new)
    fixed += 1

open(path, "w", encoding="utf-8").write("\n".join(lines))
print("fixed lines:", fixed)
