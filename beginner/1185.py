matriz = []
letra = input()

for i in range(12):
    matriz.append([])
    for j in range(12):
        x = float(input())
        matriz[i].append(x)

c = 12
s = 0
cont = 0

for i in range(11):
    c -= 1
    for j in range(c):
        s += matriz[i][j]
        cont += 1

if letra == 'S':
    print(s)

if letra == 'M':
    m = s / cont
    print(f'{m:.1f}')
