n = int(input())

for x in range(n):
    entrada = input()
    saida = ''

    for i in entrada:
        if i.islower():
            saida += i

    print(saida[::-1])
