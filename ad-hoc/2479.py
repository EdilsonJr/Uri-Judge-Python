n = int(input())
sim = 0
nao = 0
lista = []

for i in range(n):
    x = input().split()

    if x[0] == '+':
        sim += 1
    else:
        nao += 1

    lista.append(x[1])

lista = sorted(lista)

for i in range(n):
    print(lista[i])

print(f'Se comportaram: {sim} | Nao se comportaram: {nao}')
