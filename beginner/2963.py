n = int(input())
lista = []
for i in range(n):
    x = int(input())
    lista.append(x)

new = sorted(lista, reverse=True)

if lista[0] == new[0]:
    print('S')
else:
    print('N')
