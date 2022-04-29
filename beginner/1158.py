n = int(input())
soma = 0
while n != 0:
    x, y = input().split()
    x = int(x)
    y = int(y)
    soma = 0
    if x % 2 == 0:
        x += 1

    while y != 0:
        soma += x
        x += 2
        y -= 1

    print(soma)
    n -= 1
