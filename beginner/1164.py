n = int(input())

while n != 0:
    x = int(input())
    soma = 0

    for i in range(1, x + 1):
        if x % i == 0:
            soma += i

    soma -= x

    if soma == x:
        print(f'{x} eh perfeito')
    else:
        print(f'{x} nao eh perfeito')

    n -= 1
