n = int(input())
lista = []

for i in range(n):
    p, qtd = input().split()
    p, qtd = float(p), int(qtd)
    m = (p / qtd) * 1000
    lista.append(m)

lista = sorted(lista)

saida = lista[0]

print(f'{saida:.2f}')
