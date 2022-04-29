p = input()
saida = ''

for i in p.split():
    for letra in range(1, len(i), 2):
        saida += i[letra]
    saida += ' '

print(saida[:-1])
