c = True
while c:
    m, n = input().split()
    m, n = int(m), int(n)
    saida = ''

    if m == n == 0:
        c = not c
        break

    x = m + n
    x = str(x)

    for i in range(len(x)):
        if x[i] != '0':
            saida += x[i]

    print(saida)
