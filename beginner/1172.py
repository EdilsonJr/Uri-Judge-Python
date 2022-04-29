for i in range(0, 10):
    x = int(input())
    if x <= 0:
        x = 1
        print(f'X[{i}] = 1')
    else:
        print(f'X[{i}] = {x}')
