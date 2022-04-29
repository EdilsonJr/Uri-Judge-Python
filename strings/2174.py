n = int(input())
lista = []

for i in range(n):
    x = input()
    lista.append(x)

lista = set(lista)
qtd = 151 - len(lista)

print(f'Falta(m) {qtd} pomekon(s).')
