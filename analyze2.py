import re, io, glob

root = r'e:\Shipwright-wind-waker-style-cel-shading'
sohgui = root + r'\soh\soh\SohGui'

def read_literal(src, i):
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

starter = re.compile(r'(AddWidget\(\s*[\w.]+\s*,\s*|AddMenuEntry\(\s*|AddSidebarEntry\(\s*[^,]+,\s*|'
                     r'CheckboxOptions\(\)\.Tooltip\(\s*|SeparatorText\(\s*|RegisterPopup\(\s*|'
                     r'BtnSelectorOptions\(\)\.Tooltip\(\s*|\.tooltip\s*=\s*)"')

def read_concat_runs(src):
    runs = []
    for m in starter.finditer(src):
        qpos = m.end() - 1
        if src[qpos] != '"':
            continue
        buf, j = read_literal(src, qpos)
        full = buf
        while True:
            k = j
            while k < len(src) and src[k] in ' \t\r\n':
                k += 1
            if k < len(src) and src[k] == '"':
                buf2, j2 = read_literal(src, k)
                full += buf2
                j = j2
            else:
                break
        runs.append((qpos, j, full))
    return runs

def decode_escapes(s):
    out = ''
    i = 0; n = len(s)
    mp = {'n':'\n','t':'\t','r':'\r','"':'"',"'":"'",'\\':'\\','/':'/','0':'\0'}
    while i < n:
        c = s[i]
        if c == '\\' and i+1 < n:
            out += mp.get(s[i+1], s[i+1]); i += 2
        else:
            out += c; i += 1
    return out

def is_english(s):
    return any('a' <= c <= 'z' or 'A' <= c <= 'Z' for c in s)

# Keys in table
loc = io.open(sohgui + r'\Localization.cpp', 'r', encoding='utf-8').read()
keys = set(m.group(1) for m in re.finditer(r'\{\s*"((?:[^"\\]|\\.)*)"\s*,\s*"((?:[^"\\]|\\.)*)"', loc))

# Ranges of StringHelper::Translate(...) arguments
def translate_spans(src):
    spans = []
    for m in re.finditer(r'StringHelper::Translate\s*\(', src):
        # find matching close paren (shallow: string literal only, no nested parens expected)
        depth = 0; k = m.end(); n = len(src)
        while k < n:
            c = src[k]
            if c == '(':
                depth += 1
            elif c == ')':
                if depth == 0:
                    spans.append((m.start(), k+1)); break
                depth -= 1
            k += 1
    return spans

def inside(pos, spans):
    return any(a <= pos < b for a, b in spans)

candidates = {}  # (file,lineno) -> eng string
files = glob.glob(sohgui + r'\*.cpp') + glob.glob(sohgui + r'\*.h') + glob.glob(sohgui + r'\*.hpp')
for f in files:
    src = io.open(f, 'r', encoding='utf-8', errors='ignore').read()
    spans = translate_spans(src)
    for qpos, jend, full in read_concat_runs(src):
        if inside(qpos, spans):
            continue  # already wrapped
        eng = full  # raw, matches how apply_translations.py + table keys are stored
        if not is_english(eng):
            continue  # already Chinese / non-english -> treat as translated
        if eng in keys:
            continue  # already in table (unused but fine)
        lineno = src[:qpos].count('\n') + 1
        rel = f[len(sohgui)+1:]
        candidates.setdefault((rel, lineno), eng)

print('GENUINE untranslated English UI strings (not wrapped, not in table):', len(candidates))
for (rel, lineno), eng in sorted(candidates.items()):
    print('[%s:%d] %r' % (rel, lineno, eng))
