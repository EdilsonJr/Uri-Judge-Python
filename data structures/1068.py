while True:
    try:
        n = input()
        aux = 0

        for i in range(len(n)):
            if n[i] == '(':
                aux += 1
            elif n[i] == ')':
                aux -= 1
            if aux < 0:
                break

        if aux != 0:
            print('incorrect')
        else:
            print('correct')

    except EOFError:
        break
