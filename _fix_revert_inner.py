path = r"e:\Shipwright-wind-waker-style-cel-shading\soh\soh\SohGui\Localization.cpp"
s = open(path, encoding="utf-8").read()

Q  = chr(34)   # "
C  = chr(44)   # ,
SP = chr(32)   # space
BS = chr(92)   # backslash

# Re-add a backslash before any '"' that is immediately followed by
# ', ' and then a NON-quote char. This restores the inner escaped quotes
# (e.g. \"D-pad on Pause Screen\") that a previous blanket edit wrongly
# un-escaped, while leaving genuine close-key delimiters (", " -> value)
# untouched (those are followed by a quote, not a non-quote char).
out = []
n = len(s)
for i, c in enumerate(s):
    if c == Q and (i == 0 or s[i-1] != BS) and i + 1 < n and s[i+1] == C and i + 2 < n and s[i+2] == SP:
        nxt = s[i+3] if i + 3 < n else ""
        if nxt != Q:          # not a genuine close-key delimiter (", ")
            out.append(BS)   # restore the escaping backslash
    out.append(c)

new = "".join(out)
open(path, "w", encoding="utf-8").write(new)
# report how many restored
print("restored inner backslashes:", s.count(Q+C+SP) - new.count(Q+C+SP) + (0 if True else 0))
print("done")
