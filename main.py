import time

s = 0
m = 0
h = 0


while True:
    s += 1
    time.sleep(1)
    if s == 60:
        s = 0
        m += 1
    if m == 60:
        m = 0
        h += 1

    if h == 1 :
        hh = 'Hour'
    else:
        hh = 'Hours'
    if m == 1 :
        mm = 'Minute'
    else:
        mm = 'Minutes'
    if s == 1 :
        ss = 'Second'
    else:
        ss = 'Seconds'

    print(f'Time passed: {h} {hh}, {m} {mm}, {s} {ss}')
