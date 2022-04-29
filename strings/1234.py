while True:
    try:
        saida = ''
        x = input()
        c = True

        for i in x:
            if i == ' ':
                saida += ' '
                continue
            if c:
                saida += i.upper()
                c = False
            else:
                saida += i.lower()
                c = True

        print(saida)

    except EOFError:
        break
