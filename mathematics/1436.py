casos = 1
n = int(input())

while casos <= n:
    lista = input().split()
    saida = []

    for i in lista:
        if 11 <= int(i) <= 20:
            saida.append(i)

    if len(saida) % 2 != 0:
        saida.sort()
        tam = int((len(saida)/2))
        print(f'Case {casos}: {saida[tam]}')

    casos += 1
