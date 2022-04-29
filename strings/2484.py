while True:
    try:
        p = input()
        tam = len(p)
        espaco = 0

        for j in range(tam):
            s = ''
            if espaco != 0:
                for i in range(espaco):
                    s += ' '

            for i in range(len(p)):
                s += p[i]
                if i < (len(p) - 1):
                    s += ' '
            print(s)
            espaco += 1
            p = p[:-1]
        print()

    except EOFError:
        break
