n = int(input())

for i in range(n):
    entrada = input()

    if len(entrada) > 3:
        print(3)
    else:
        qtd = 0
        if entrada[0:1] == 'o':
            qtd += 1
        if entrada[1:2] == 'n':
            qtd += 1
        if entrada[2:3] == 'e':
            qtd += 1

        if qtd >= 2:
            print(1)
        else:
            print(2)
