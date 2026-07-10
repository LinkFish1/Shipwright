import io

path = r"e:\Shipwright-wind-waker-style-cel-shading\soh\soh\SohGui\Localization.cpp"
lines = open(path, encoding="utf-8").read().split("\n")

BS = chr(92)   # backslash
Q  = chr(34)   # "
C  = chr(44)   # ,
SP = chr(32)   # space

def fix_single_entry(s):
    # only single-line entries: contains both '{' and '},' on the same line
    if not s.strip().startswith("{"):
        return s
    if "}," not in s:
        return s
    n = len(s)
    # 1) open_key = first '"'; strip preceding backslash if any
    ok = s.find(Q)
    if ok < 0:
        return s
    if ok > 0 and s[ok - 1] == BS:
        s = s[:ok - 1] + s[ok:]
        n = len(s)
    # 2) close_value = last '"'; strip preceding backslash if any
    cv = s.rfind(Q)
    if cv < 0 or cv == ok:
        return s
    if cv > 0 and s[cv - 1] == BS:
        s = s[:cv - 1] + s[cv:]
        n = len(s)
        cv = cv - 1
    # 3) separator: find ', ' whose preceding (skip BS) is '"' and following is '"'
    # re-read ok/cv after possible edits
    ok = s.find(Q)
    cv = s.rfind(Q)
    sep = -1
    for i in range(n - 1):
        if s[i] == C and i + 1 < n and s[i + 1] == SP:
            before = s[i - 1] if i - 1 >= 0 else ""
            after = s[i + 2] if i + 2 < n else ""
            if before == Q and after == Q:
                sep = i
                break
    if sep < 0:
        return s
    # close_key: the '"' right before sep (strip BS), open_value: '"' right after sep (strip BS)
    ck = sep - 1
    while ck >= 0 and s[ck] == BS:
        ck -= 1
    if ck < 0 or s[ck] != Q:
        return s
    ov = sep + 2
    while ov < n and s[ov] == BS:
        ov += 1
    if ov >= n or s[ov] != Q:
        return s
    # rebuild: close_key plain '"', ", ", open_value plain '"'
    new = s[:ck] + Q + C + SP + Q + s[ov + 1:]
    return new

fixed = 0
for ln in range(len(lines)):
    new = fix_single_entry(lines[ln])
    if new != lines[ln]:
        fixed += 1
        lines[ln] = new

open(path, "w", encoding="utf-8").write("\n".join(lines))
print("fixed single-line entries:", fixed)
