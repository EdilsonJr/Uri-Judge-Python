c = True

while c:
    x = int(input())
    soma = 0
    y = 0

    if x == 0:
        c = False
        break

    if x % 2 == 1:
        x += 1

    while y != 5:
        soma += x
        x += 2
        y += 1

    print(soma)
