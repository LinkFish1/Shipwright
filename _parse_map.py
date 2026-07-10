path = r"e:\Shipwright-wind-waker-style-cel-shading\soh\soh\SohGui\Localization.cpp"
lines = open(path, encoding="utf-8").read().split("\n")

# locate map: first 'gChineseTable' then its opening '{'
text = "\n".join(lines)
start = text.index("gChineseTable")
i = text.index("{", start)
# now parse initializer list; track brace depth; collect entries
n = len(text)
depth = 0
in_str = False
esc = False
entry_start = None
entries = []  # list of (lineno, snippet)
lineno = text[:i].count("\n") + 1

j = i
# We'll just scan and flag any UNESCAPED brace that is not the per-entry { } frame.
# Robust: walk; when not in string, a '{' starts an entry; expect '"'..'"' , '"'..'"' '}'.
# If while NOT in string we see an unexpected token, record.
k = i
state = "expect_entry_open"  # expect '{'
problems = []
while k < n:
    c = text[k]
    if in_str:
        if esc:
            esc = False
        elif c == "\\":
            esc = True
        elif c == '"':
            in_str = False
        k += 1
        continue
    # not in string
    if c == '"':
        in_str = True
        k += 1
        continue
    if c == "\n":
        lineno += 1
        k += 1
        continue
    if c.isspace():
        k += 1
        continue
    if c == "{":
        # start of an entry (or the map open already past). We are inside map now.
        # push: expect key string
        state = "expect_key"
        entry_open_line = lineno
        k += 1
        continue
    if c == "}":
        # end of an entry or end of map
        state = "expect_comma_or_close"
        k += 1
        continue
    if c == ",":
        if state == "expect_comma_or_close":
            state = "expect_entry_open"
        elif state in ("after_key",):
            state = "expect_value"
        else:
            # comma in unexpected place
            problems.append((lineno, "unexpected ',' state=%s" % state))
        k += 1
        continue
    if c == ":":
        # could be part of something; ignore
        k += 1
        continue
    # any other non-string, non-brace, non-comma char while parsing an entry frame
    if state in ("expect_key", "expect_value", "after_key", "expect_comma_or_close", "expect_entry_open"):
        problems.append((lineno, "unexpected char %r in state=%s" % (c, state)))
        k += 1
        continue
    k += 1

for p in problems[:40]:
    print(p)
print("total problems:", len(problems))
