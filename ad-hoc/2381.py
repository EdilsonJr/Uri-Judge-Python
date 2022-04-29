n, x = input().split()
n, x = int(n), int(x)
nomes = []

for i in range(n):
    nome = input()
    nomes.append(nome)

nomes = sorted(nomes)

print(nomes[x-1])
