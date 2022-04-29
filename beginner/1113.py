i = 0

while i != 1:
    x, y = input().split(" ")
    x = int(x)
    y = int(y)
    if x == y:
        i = 1
    elif x > y:
        print('Decrescente')
    else:
        print('Crescente')
