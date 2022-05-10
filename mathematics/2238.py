a, b, c, d = input().split()
a, b, c, d = int(a), int(b), int(c), int(d)
saida = -1

if a != b and c != d:
    temp = c
    aux = a

    while aux <= temp:
        if aux % a == 0 and aux % b != 0 and c % aux == 0 and d % aux != 0:
            saida = aux
            break
        aux += a

print(saida)
