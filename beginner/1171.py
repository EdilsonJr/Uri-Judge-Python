n = int(input())
lista = {}
for i in range(n):
    x = int(input())
    if (x in lista):
        lista[x] += 1
    else:
        lista[x] = 1

aux = lista.keys()
aux = sorted(aux)

for z in aux:
    print(f'{z} aparece {lista[z]} vez(es)')
