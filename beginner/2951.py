n, g = input().split()
n, g = int(n), int(g)
letra = []
valor = []
soma = 0

for i in range(n):
    l, v = input().split()
    letra.append(l), valor.append(int(v))

x = int(input())
runas = input().split()

for i in range(x):
    for j in range(n):
        if runas[i] == letra[j]:
            soma += valor[j]

if soma >= g:
    print(soma)
    print('You shall pass!')
else:
    print(soma)
    print('My precioooous')
