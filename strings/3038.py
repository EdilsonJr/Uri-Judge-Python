while True:
    try:
        saida = ''
        x = input()

        for i in x:
            if i == ' ':
                saida += ' '
            elif i == '@':
                saida += 'a'
            elif i == '&':
                saida += 'e'
            elif i == '!':
                saida += 'i'
            elif i == '*':
                saida += 'o'
            elif i == '#':
                saida += 'u'
            else:
                saida += i

        print(saida)

    except EOFError:
        break
