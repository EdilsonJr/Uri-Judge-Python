o = input()
m = []

for i in range(12):
    m.append([])

    for j in range(12):
        x = float(input())
        m[i].append(x)

if o == 'S':
    s = 0
    c = 11
    for i in range(11, 0, -1):
        for j in range(0, c):
            s = s + m[i][j]
        c = c - 1
    print(f'{s:.1f}')

if o == 'M':
    s = 0
    c = 11
    c2 = 0
    for i in range(11, 0, -1):
        for j in range(0, c):
            s = s + m[i][j]
            c2 = c2 + 1
        c = c - 1

    m = s / c2

    print(f'{m:.1f}')
