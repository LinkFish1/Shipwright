import time, sys
log = 'e:/Shipwright-wind-waker-style-cel-shading/build_log10.txt'
# wait up to 200s, polling every 10s, stop when BUILD_RC_ appears
out = sys.stdout.buffer
for _ in range(20):
    try:
        d = open(log, encoding='utf-8', errors='replace').read()
    except Exception as e:
        d = ''
    if 'BUILD_RC_' in d:
        idx = d.rfind('BUILD_RC_')
        out.write(('BUILD DONE: ' + d[idx:idx+20] + '\n').encode('utf-8', 'replace'))
        lines = d.splitlines()
        tail = '\n'.join(lines[-25:])
        out.write(('TAIL:\n' + tail + '\n').encode('utf-8', 'replace'))
        break
    time.sleep(10)
else:
    try:
        d = open(log, encoding='utf-8', errors='replace').read()
    except Exception:
        d = ''
    out.write(('STILL RUNNING after 200s. TAIL:\n' + '\n'.join(d.splitlines()[-15:]) + '\n').encode('utf-8', 'replace'))
