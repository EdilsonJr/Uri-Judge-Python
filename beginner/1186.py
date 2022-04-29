matriz = []
letra = input()

for i in range(12):
    matriz.append([])
    for j in range(12):
        x = float(input())
        matriz[i].append(x)

c = 0
s = 0
cont = 0

for i in range(11, 0, -1):
    c += 1
    for j in range(c, 12):
        s += matriz[i][j]
        cont += 1

if letra == 'S':
    print(s)

if letra == 'M':
    m = s / cont
    print(f'{m:.1f}')