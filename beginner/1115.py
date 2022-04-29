n = 0

while n != 1:
    x, y = input().split()
    x = int(x)
    y = int(y)

    if x == 0 or y == 0:
        break

    if x > 0:
        if y > 0:
            print('primeiro')
        if y < 0:
            print('quarto')
    if x < 0:
        if y > 0:
            print('segundo')
        if y < 0:
            print('terceiro')
