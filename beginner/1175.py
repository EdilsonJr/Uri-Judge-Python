lista = []
for i in range(0, 20):
    x = int(input())
    lista.append(x)

newList = [num for num in reversed(lista)]

for i in range(0, 20):
    print(f'N[{i}] = {newList[i]}')
