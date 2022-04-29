x, y = input().split()
x = int(x)
y = int(y)
count = 0
lista = []
for i in range(1, y + 1):
    lista.append(i)
    count += 1
    if count == x:
        print(*lista)
        lista.clear()
        count = 0
