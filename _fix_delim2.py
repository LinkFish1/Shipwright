path = r"e:\Shipwright-wind-waker-style-cel-shading\soh\soh\SohGui\Localization.cpp"
s = open(path, encoding="utf-8").read()

BS = chr(92)   # backslash
Q  = chr(34)   # "
C  = chr(44)   # ,
SP = chr(32)   # space
B  = chr(123)  # {
BR = chr(125)  # }

reps = [
    (BS + Q + C,        Q + C),        # close-key corrupted: \",  -> ",
    (C + SP + BS + Q,  C + SP + Q),  # open-value corrupted: , \" -> , "
    (BS + Q + SP + BR, Q + SP + BR),  # close-value corrupted: \" } -> " }
    (B + SP + BS + Q,  B + SP + Q),  # open-key corrupted: { \" -> { "
]
for old, new in reps:
    n = s.count(old)
    print("replace %r -> %r : %d" % (old, new, n))
    s = s.replace(old, new)

open(path, "w", encoding="utf-8").write(s)
print("done")
