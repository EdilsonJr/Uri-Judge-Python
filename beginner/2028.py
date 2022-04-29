aux = 1

while True:
    try:
        lista = [0]
        a = int(input())
        temp = a

        for i in range(a):
            for j in range(temp):
                lista.append(temp)
            temp -= 1

        tam = len(lista)
        lista = sorted(lista)

        if tam == 1:
            print(f'Caso {aux}: {tam} numero')
            print(0)
        else:
            print(f'Caso {aux}: {tam} numeros')
            print(*lista)
        print()
        aux += 1

    except EOFError:
        break
