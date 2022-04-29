n = int(input())
lista = [0, 1]
x = 0
for i in range(1, n-1):
    if n == 1:
        print(0)
    elif n == 2:
        print(lista)
    else:
        x = lista[i] + lista[i-1]
        lista.append(x)

print(*lista)
