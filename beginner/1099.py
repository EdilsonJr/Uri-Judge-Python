n = int(input())

for i in range(1, n + 1):
    x = input().split()
    a, b = x
    a = int(a)
    b = int(b)

    soma = 0
    if a > b:
        for d in range(int(b) + 1, int(a)):
            if d % 2 != 0:
                soma = soma + d
    if a < b:
        for d in range(int(a) + 1, int(b)):
            if d % 2 != 0:
                soma = soma + d
    if a == b:
        soma = 0
    print(soma)
