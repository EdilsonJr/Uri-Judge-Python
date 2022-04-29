n = int(input())

for i in range(n):
    x = input().split()
    o = x[1]
    res = x[4]
    res = int(res)

    if o == '+':
        valor = int(x[0]) + int(x[2])
    elif o == '-':
        valor = int(x[0]) - int(x[2])
    elif o == 'x':
        valor = int(x[0]) * int(x[2])

    saida = abs(valor - res)
    s = 'E'
    for j in range(saida):
        s += 'r'
    s += 'ou!'

    print(s)
