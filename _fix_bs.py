path = r"e:\Shipwright-wind-waker-style-cel-shading\soh\soh\SohGui\Localization.cpp"
s = open(path, encoding="utf-8").read()

BS = chr(92)  # backslash

# Corruption: two backslashes before an escape char -> one backslash
old_q = BS + BS + '"'      # \\"
new_q = BS + '"'           # \"
old_n = BS + BS + 'n'      # \\n
new_n = BS + 'n'           # \n
old_t = BS + BS + 't'
new_t = BS + 't'
old_r = BS + BS + 'r'
new_r = BS + 'r'

def count(s, sub):
    return s.count(sub)

print("before: \\\"=", count(s, old_q), " \\\\n=", count(s, old_n),
      " \\\\t=", count(s, old_t), " \\\\r=", count(s, old_r))

s = s.replace(old_q, new_q)
s = s.replace(old_n, new_n)
s = s.replace(old_t, new_t)
s = s.replace(old_r, new_r)

print("after:  \\\"=", count(s, old_q), " \\\\n=", count(s, old_n),
      " \\\\t=", count(s, old_t), " \\\\r=", count(s, old_r))

open(path, "w", encoding="utf-8").write(s)
print("done")
