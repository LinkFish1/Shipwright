import re

PATHS = [
    r'soh\soh\SohGui\SohMenuEnhancements.cpp',
    r'soh\soh\SohGui\ResolutionEditor.cpp',
]


def find_translate_close(s, start):
    """s[start] is the '(' of StringHelper::Translate(. Return index right AFTER its
    matching close ')', respecting C++ string literals (incl. escapes)."""
    i = s.index('(', start) + 1
    depth = 1
    instr = False
    while i < len(s):
        c = s[i]
        if instr:
            if c == '\\':
                i += 2
                continue
            if c == '"':
                instr = False
            i += 1
            continue
        if c == '"':
            instr = True
        elif c == '(':
            depth += 1
        elif c == ')':
            depth -= 1
            if depth == 0:
                return i + 1
        i += 1
    return -1


def fix_file(path):
    s = open(path, encoding='utf-8').read()
    out = []
    i = 0
    L = len(s)
    changed = False
    while i < L:
        key = 'StringHelper::Translate('
        p = s.find(key, i)
        if p == -1:
            out.append(s[i:])
            break
        out.append(s[i:p])
        # scan to Translate's close
        close = find_translate_close(s, p)
        if close == -1:
            out.append(s[p:])
            break
        # look at preceding context for fmt::format(
        preceding = s[max(0, p - 60):p]
        in_fmt = ('fmt::format(' in preceding) and (
            preceding.rfind('fmt::format(') > preceding.rfind(')'))
        # skip whitespace after close
        k = close
        while k < L and s[k] in ' \t\r\n':
            k += 1
        has_cstr = s.startswith('.c_str()', k)
        if in_fmt:
            # fmt wants std::string as first arg -> must NOT have .c_str()
            if has_cstr:
                out.append(s[p:k])            # drop erroneous .c_str()
                i = k + len('.c_str()')
                changed = True
                continue
            else:
                out.append(s[p:close])
                i = close
                continue
        else:
            if has_cstr:
                out.append(s[p:k])
                i = k + len('.c_str()')
                continue
            else:
                # broken: Translate closed but missing .c_str() before the
                # outer call's close. Insert it.
                out.append(s[p:close])
                out.append('.c_str()')
                i = close
                changed = True
                continue
    if changed:
        open(path, 'w', encoding='utf-8').write(''.join(out))
        print('FIXED', path)
    else:
        print('NOCHANGE', path)


for f in PATHS:
    fix_file(f)
print('DONE')
