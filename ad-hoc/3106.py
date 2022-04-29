n = int(input())
lista = input().split()
lista = [int(i) for i in lista]

for i in range(n):
    lista[i] = lista[i] // 3 * 3

print(sum(lista))
