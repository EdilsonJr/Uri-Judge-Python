n = int(input())

for i in range(1, n + 1):
    x = input().split()
    a, b, c = x

    a = float(a)
    b = float(b)
    c = float(c)

    media = a * 0.2 + b * 0.3 + c * 0.5

    print(f'{media:.1f}')

