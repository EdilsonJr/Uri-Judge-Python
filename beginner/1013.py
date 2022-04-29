x = input().split(" ")

maior = 0
l = x
lista  = list(map(int, l))

for i in range(3):
    if lista[i] > maior:
        maior = lista[i]
print(f'{maior} eh o maior')
