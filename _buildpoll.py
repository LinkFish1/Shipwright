import time, subprocess, sys
log = 'e:/Shipwright-wind-waker-style-cel-shading/build_log10.txt'
# wait until BUILD_RC_ appears in the log (build finished) or timeout
for _ in range(120):
    try:
        data = open(log, encoding='utf-8', errors='replace').read()
    except Exception as e:
        data = ''
    if 'BUILD_RC_' in data:
        # print last 40 lines
        lines = data.splitlines()
        print('BUILD FINISHED. last lines:')
        for ln in lines[-40:]:
            print(ln)
        break
    time.sleep(5)
else:
    print('TIMEOUT: build still running after 10 min')
    # also report current tail
    try:
        data = open(log, encoding='utf-8', errors='replace').read()
        for ln in data.splitlines()[-20:]:
            print(ln)
    except Exception as e:
        print('log read error', e)
