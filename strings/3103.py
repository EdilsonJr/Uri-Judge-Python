n = int(input())

for i in range(n):
    y = input()
    y = sorted(y)

    for j in range(len(y)):
        if y[j] != '0':
            temp = y[j]
            y[j] = y[0]
            y[0] = temp
            break

    print(*y, sep='')
