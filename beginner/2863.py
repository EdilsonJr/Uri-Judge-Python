while True:
    try:
        n = int(input())
        lista = []
        for i in range(n):
            x = float(input())
            lista.append(x)

        lista = sorted(lista)
        print(lista[0])

    except EOFError:
        break
