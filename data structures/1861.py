saida = {}
lista = []

while True:
    try:
        k, m = input().split()
        if k in saida:
            saida[k] += 1
            lista.append(m)
        else:
            saida[k] = 1
            lista.append(m)

    except EOFError:
        break

for i in lista:
    saida.pop(i, None)

print('HALL OF MURDERERS')

for i, x in sorted(saida.items()):
    print(i, x)
