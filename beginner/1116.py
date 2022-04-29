n = int(input())

for i in range(1, n + 1):
    x, y = input().split()
    x = int(x)
    y = int(y)

    if y == 0:
        print('divisao impossivel')
    else:
        div = float(x) / y
        print(f'{div:.1f}')
