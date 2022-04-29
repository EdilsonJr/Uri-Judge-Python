n = int(input())
lista = []

for i in range(n):
    x = input()
    lista.append(x)

lista = sorted(sorted(lista), key=str.lower)

for i in range(n):
    print(lista[i])
