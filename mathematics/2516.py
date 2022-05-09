while True:
    try:
        s, va, vb = input().split()
        s, va, vb = float(s), float(va), float(vb)

        if va <= vb:
            print('impossivel')
        else:
            tempo = s / (va - vb) * 1.0
            tempo = float(tempo)
            print(f'{tempo:.2f}')

    except EOFError:
        break
