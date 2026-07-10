Q = '"'
BS = "\\"

def fix_entry_line(s):
    st = s.strip()
    if not st.startswith("{"):
        return s
    if "}," not in s:
        return s
    ok = s.find(Q)
    if ok < 0:
        return s
    cv = s.rfind(Q)
    if cv < 0 or cv == ok:
        return s
    sep = s.rfind(", " + Q)
    if sep < 0:
        return s
    ck = sep - 1
    if ck >= 0 and s[ck] == BS:
        ck -= 1
    if ck < 0 or s[ck] != Q:
        return s
    ov = sep + 2
    if ov >= len(s) or s[ov] != Q:
        return s
    delims = {ok, ck, ov, cv}
    out = []
    i = 0
    n = len(s)
    while i < n:
        ch = s[i]
        if ch == Q:
            if i in delims:
                if i > 0 and s[i-1] == BS:
                    out.append(Q)
                else:
                    out.append(Q)
            else:
                if i > 0 and s[i-1] == BS:
                    out.append(Q)
                else:
                    out.append(BS)
                    out.append(Q)
            i += 1
        else:
            out.append(ch)
            i += 1
    return "".join(out)

L = open(r"e:\Shipwright-wind-waker-style-cel-shading\soh\soh\SohGui\Localization.cpp", encoding="utf-8").read().split("\n")
s = L[2938]
print("starts:", s.strip()[:25])
print("has },:", "}," in s)
print("--- INPUT ---")
print(s[:220])
r = fix_entry_line(s)
print("--- OUTPUT (head) ---")
print(r[:220])
print("changed:", r != s)
print("INPUT tail:", s[-40:])
print("OUTPUT tail:", r[-40:])
