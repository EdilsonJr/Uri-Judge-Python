n = int(input())

for i in range(n):
    a, b, c = input().split()
    a, b, c = int(a), int(b), int(c)

    x = - (b / (2 * a))
    y = a*x*x + b*x + c

    print(f'{y:.2f}')
