import io

path = r"e:\Shipwright-wind-waker-style-cel-shading\soh\soh\SohGui\Localization.cpp"
lines = open(path, encoding="utf-8").read().split("\n")

Q = '"'   # doublequote
C = ','
SP = ' '
BS = '\\'

def fix_entry_line(s):
    # Only single-line entries: starts with '{' (stripped) and contains '},' on same line.
    st = s.strip()
    if not st.startswith("{"):
        return s
    if "}," not in s:
        return s
    # Find the 4 delimiter quote positions structurally.
    # open_key = first '"'
    ok = s.find(Q)
    if ok < 0:
        return s
    # close_value = last '"'
    cv = s.rfind(Q)
    if cv < 0 or cv == ok:
        return s
    # separator = LAST ', "' (comma, space, quote) -> open_value is the quote there;
    # close_key is the quote immediately before that ', "'
    sep = s.rfind(", " + Q)
    if sep < 0:
        return s
    # close_key: the '"' right before sep (possibly escaped as \")
    ck = sep - 1
    if ck >= 0 and s[ck] == BS:
        ck -= 1
    if ck < 0 or s[ck] != Q:
        return s
    # open_value: the '"' at sep+2 (the quote in ', "')
    ov = sep + 2
    if ov >= len(s) or s[ov] != Q:
        return s
    delims = {ok, ck, ov, cv}
    # Rebuild: every '"' at a delimiter -> plain; every other '"' -> escaped.
    out = []
    i = 0
    n = len(s)
    while i < n:
        ch = s[i]
        if ch == Q:
            if i in delims:
                # ensure plain: if preceded by backslash, drop it
                if i > 0 and s[i-1] == BS:
                    out.append(Q)
                else:
                    out.append(Q)
            else:
                # ensure escaped
                if i > 0 and s[i-1] == BS:
                    out.append(Q)   # already escaped
                else:
                    out.append(BS)
                    out.append(Q)
            i += 1
        else:
            out.append(ch)
            i += 1
    return "".join(out)

fixed = 0
for ln in range(len(lines)):
    new = fix_entry_line(lines[ln])
    if new != lines[ln]:
        fixed += 1
        lines[ln] = new

open(path, "w", encoding="utf-8").write("\n".join(lines))
print("fixed single-line entries:", fixed)
