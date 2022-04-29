n = int(input())
um = ['o', 'n', 'e']
dois = ['t', 'w', 'o']
tres = ['t', 'h', 'r', 'e', 'e']

for i in range(n):
    x = input()
    tam = len(x)
    erros = 0
    u = 0
    d = 0

    if tam == 5:
        for j in range(5):
            if x[j] != tres[j]:
                erros += 1

        if erros <= 1:
            print(3)
    else:
        for j in range(3):
            if x[j] != um[j] and x[j] != dois[j]:
                erros += 1
            if x[j] == um[j]:
                u += 1
            if x[j] == dois[j]:
                d += 1

        if erros <= 1:
            if u > d:
                print(1)
            else:
                print(2)

