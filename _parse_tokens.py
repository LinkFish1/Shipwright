path = r"e:\Shipwright-wind-waker-style-cel-shading\soh\soh\SohGui\Localization.cpp"
text = open(path, encoding="utf-8").read()

# region between 'gChineseTable' opening brace and its closing '};'
a = text.index("gChineseTable")
i = text.index("{", a)
# find matching close '};' — scan from here for the '};' at brace-depth 0 inside this list
depth = 0
in_str = False
esc = False
end = None
j = i
while j < len(text):
    c = text[j]
    if in_str:
        if esc:
            esc = False
        elif c == "\\":
            esc = True
        elif c == '"':
            in_str = False
        j += 1
        continue
    if c == '"':
        in_str = True
        j += 1
        continue
    if c == "{":
        depth += 1
    elif c == "}":
        depth -= 1
        if depth == 0:
            # this '}' is the map close; ensure followed by ';'
            end = j
            break
    j += 1

region = text[i:end]  # the initializer list content (without outer braces)

# Tokenize region into STRING / COMMA / OPEN / CLOSE (string-aware)
tokens = []  # (kind, lineno, snippet)
lineno = text[:i].count("\n") + 1
k = 0
N = len(region)
cur_line = lineno
while k < N:
    c = region[k]
    if c == "\n":
        cur_line += 1
        k += 1
        continue
    if c.isspace():
        k += 1
        continue
    if in_str:
        # continue current string
        pass
    if region[k] == '"':
        # read string
        in_str = True
        esc = False
        start = k
        k += 1
        s = ""
        while k < N:
            d = region[k]
            if d == "\n":
                cur_line += 1
                s += d
                k += 1
                continue
            if esc:
                esc = False
                s += d
                k += 1
                continue
            if d == "\\":
                esc = True
                s += d
                k += 1
                continue
            if d == '"':
                s += d
                k += 1
                in_str = False
                break
            s += d
            k += 1
        tokens.append(("STR", cur_line, s[:30]))
        continue
    if c == ",":
        tokens.append((",", cur_line, ","))
        k += 1
        continue
    if c == "{":
        tokens.append(("{", cur_line, "{"))
        k += 1
        continue
    if c == "}":
        tokens.append(("}", cur_line, "}"))
        k += 1
        continue
    # unexpected char
    tokens.append(("?", cur_line, c))
    k += 1

# Walk expecting: { STR , STR } ,  { STR , STR } , ...
problems = []
t = 0
m = len(tokens)
entry_no = 0
state = "expect_open"
while t < m:
    kind = tokens[t][0]
    if state == "expect_open":
        if kind == "{":
            state = "expect_key"
            t += 1
            continue
        else:
            problems.append((tokens[t][1], "expect '{' got %s" % kind, tokens[t][2]))
            t += 1
            continue
    if state == "expect_key":
        if kind == "STR":
            state = "expect_comma1"
            t += 1
            continue
        else:
            problems.append((tokens[t][1], "expect KEY str got %s" % kind, tokens[t][2]))
            t += 1
            continue
    if state == "expect_comma1":
        if kind == ",":
            state = "expect_value"
            t += 1
            continue
        else:
            problems.append((tokens[t][1], "expect ',' after key got %s" % kind, tokens[t][2]))
            t += 1
            continue
    if state == "expect_value":
        if kind == "STR":
            state = "expect_close"
            t += 1
            continue
        else:
            problems.append((tokens[t][1], "expect VALUE str got %s" % kind, tokens[t][2]))
            t += 1
            continue
    if state == "expect_close":
        if kind == "}":
            entry_no += 1
            state = "expect_comma_or_end"
            t += 1
            continue
        else:
            problems.append((tokens[t][1], "expect '}' after value got %s" % kind, tokens[t][2]))
            t += 1
            continue
    if state == "expect_comma_or_end":
        if kind == ",":
            state = "expect_open"
            t += 1
            continue
        else:
            problems.append((tokens[t][1], "expect ',' or '}' got %s (entry#%d)" % (kind, entry_no), tokens[t][2]))
            # try to recover by advancing
            t += 1
            continue

print("total entries parsed:", entry_no)
print("first problems (up to 15):")
for p in problems[:15]:
    print("  line", p[0], p[1], repr(p[2]))
