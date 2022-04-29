while True:
    try:
        a, b = input().split()
        a = int(a)
        b = int(b)
        if a == 0:
            c = 0
        if b == 0:
            d = 0
        c = (a * 12) / 360
        d = (b * 60) / 360
        c = int(c)
        d = int(d)

        if c < 10 and d < 10:
            print(f'0{c}:0{d}')
        elif c < 10 <= d:
            print(f'0{c}:{d}')
        elif c >= 10 > d:
            print(f'{c}:0{d}')
        else:
            print(f'{c}:{d}')

    except EOFError:
        break
