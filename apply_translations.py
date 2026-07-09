import re, os, glob, sys
from translations_map import TRANSLATIONS

DRYRUN = '--apply' not in sys.argv

root = r'e:\Shipwright-wind-waker-style-cel-shading\soh\soh\SohGui'

# Map English full-string -> which file it lives in (derive by scanning).
# We locate each English string by reconstructing concatenation runs in each file.

# Patterns that begin a UI string context (the literal right after the pattern is the start quote).
def find_files():
    return (glob.glob(os.path.join(root, '*.cpp')) +
            glob.glob(os.path.join(root, '*.h')) +
            glob.glob(os.path.join(root, '*.hpp')))

def decode_escapes(s):
    """Decode C++ string-literal escapes (\n \t \" \\ etc.) into actual characters."""
    out = ''
    i = 0
    n = len(s)
    mp = {'n': '\n', 't': '\t', 'r': '\r', '"': '"', "'": "'", '\\': '\\', '/': '/', '0': '\0'}
    while i < n:
        c = s[i]
        if c == '\\' and i + 1 < n:
            out += mp.get(s[i+1], s[i+1])
            i += 2
        else:
            out += c
            i += 1
    return out

def read_concat_runs(src):
    """Return list of (start_index_of_opening_quote, end_index_after_closing_quote, full_decoded_string)
    for every string-literal concatenation run that begins right after a UI-call pattern."""
    runs = []
    # UI call starters; the literal immediately follows
    starter = re.compile(r'(AddWidget\(\s*[\w.]+\s*,\s*|AddMenuEntry\(\s*|AddSidebarEntry\(\s*[^,]+,\s*|'
                         r'CheckboxOptions\(\)\.Tooltip\(\s*|SeparatorText\(\s*|RegisterPopup\(\s*|'
                         r'BtnSelectorOptions\(\)\.Tooltip\(\s*|\.tooltip\s*=\s*)"')
    for m in starter.finditer(src):
        qpos = m.end() - 1
        if src[qpos] != '"':
            continue
        i = qpos
        n = len(src)
        buf, j = read_literal(src, i)
        full = buf
        # continue concatenation
        while True:
            k = j
            while k < n and src[k] in ' \t\r\n':
                k += 1
            if k < n and src[k] == '"':
                buf2, j2 = read_literal(src, k)
                full += buf2
                j = j2
            else:
                break
        runs.append((qpos, j, decode_escapes(full)))
    return runs

def read_literal(src, i):
    """i points at opening quote. Return (decoded_content, index_after_closing_quote)."""
    assert src[i] == '"'
    j = i + 1
    n = len(src)
    buf = ''
    while j < n:
        c = src[j]
        if c == '\\':
            buf += c + src[j+1]
            j += 2
            continue
        if c == '"':
            j += 1
            return buf, j
        buf += c
        j += 1
    return buf, j

# Build reverse map: file -> list of (qpos, jend, eng) for english strings that match TRANSLATIONS
todo = []
for f in find_files():
    src = open(f, encoding='utf-8', errors='ignore').read()
    # skip if already contains Translate wraps everywhere? just locate
    for qpos, jend, full in read_concat_runs(src):
        if full in TRANSLATIONS:
            todo.append((f, qpos, jend, full))

# Group by file, apply replacements from end to start to preserve offsets
byfile = {}
for f, qpos, jend, full in todo:
    byfile.setdefault(f, []).append((qpos, jend, full))

applied = 0
for f, items in byfile.items():
    src = open(f, encoding='utf-8', errors='ignore').read()
    items_sorted = sorted(items, key=lambda x: x[0], reverse=True)
    # verify no overlaps
    new_src = src
    for qpos, jend, full in items_sorted:
        # the literal span [qpos, jend) currently is: "...." possibly with concatenated segments
        # We wrap: replace the opening quote char region: insert "StringHelper::Translate(" before qpos,
        # and ")" after jend, plus ".c_str()" — but careful: jend is after closing quote.
        # Build replacement of the substring [qpos:jend] by adding wrapper around it.
        seg = new_src[qpos:jend]
        # seg starts with " and ends with "
        replacement = 'StringHelper::Translate(' + seg + ').c_str()'
        new_src = new_src[:qpos] + replacement + new_src[jend:]
    if not DRYRUN:
        open(f, 'w', encoding='utf-8').write(new_src)
    applied += len(items)

print('[DRYRUN] ' if DRYRUN else 'Applied wraps to', applied, 'strings across', len(byfile), 'files.')

# Now append keys to Localization.cpp
loc_path = os.path.join(root, 'Localization.cpp')
loc = open(loc_path, encoding='utf-8', errors='ignore').read()
marker = '    // __TRANSLATION_TAIL__'
assert marker in loc
block_lines = []
for eng, zh in TRANSLATIONS.items():
    # format key with continuation to match style: we keep as single literal string (may contain \n etc.)
    # Use repr-free escaping: the source already uses \\n for newline; our eng has real \n (decoded).
    # We must re-escape: in C++ source, a literal newline inside "" is written as \n (two chars).
    key_src = eng.replace('\\', '\\\\').replace('"', '\\"')
    key_src = key_src.replace('\n', '\\n').replace('\r', '\\r')
    val_src = zh.replace('\\', '\\\\').replace('"', '\\"')
    # Chinese has no need for \n escaping but keep consistent
    val_src = val_src.replace('\n', '\\n').replace('\r', '\\r')
    block_lines.append('    { "%s", "%s" },' % (key_src, val_src))
block = '\n'.join(block_lines) + '\n\n'
loc = loc.replace(marker, block + marker, 1)
if not DRYRUN:
    open(loc_path, 'w', encoding='utf-8').write(loc)
print('[DRYRUN] ' if DRYRUN else 'Added', len(TRANSLATIONS), 'keys to Localization.cpp')
