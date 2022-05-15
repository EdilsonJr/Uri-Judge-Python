n = int(input())

for i in range(n):
    a, b, c, d = input().split()
    a, b, c, d = int(a), int(b), int(c), int(d)

    if (a < c and b < d) or (b < c and a < d):
        print('S')
    else:
        print('N')