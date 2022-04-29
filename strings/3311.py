def func(item):
    return item[1]


n = int(input())
lista = []

for i in range(n):
    n_l = []
    x = input()
    n_l.append(x)
    n_l.append(x[0])
    lista.append(n_l)

lista.sort(key=func)

for i in range(n):
    print(lista[i][0])
