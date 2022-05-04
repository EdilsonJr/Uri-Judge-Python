maior = 0
while True:
    entrada = input().split()
    aux = []

    if entrada == ['0']:
        break

    for i in entrada:
        aux.append(str(len(i)))
        if len(i) >= maior:
            maior = len(i)
            palavra = i
    saida = '-'.join(aux)
    print(saida)

print()
print(f'The biggest word: {palavra}')
