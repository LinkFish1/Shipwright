path = r"e:\Shipwright-wind-waker-style-cel-shading\soh\soh\SohGui\Localization.cpp"
s = open(path, encoding="utf-8").read()

reps = [
    ('{\ "', '{ "'),       # open-key corrupted
    ('\",', '",'),        # close-key corrupted (before separator comma)
    (', \"', ', "'),      # open-value corrupted (after separator comma)
    ('\" },', '" },'),    # close-value corrupted (before })
]
for old, new in reps:
    n = s.count(old)
    print(f"{old!r} -> {new!r} : {n}")
    s = s.replace(old, new)

open(path, "w", encoding="utf-8").write(s)
print("done")
