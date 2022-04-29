def mov(p, m):
    if m == 1:
        v1, v2 = 'A', 'B'
    elif m == 2:
        v1, v2 = 'B', 'C'
    elif m == 3:
        v1, v2 = 'A', 'C'

    if p == v1:
        return v2
    elif p == v2:
        return v1
    else:
        return p


n = int(input())
p = input()

for i in range(n):
    m = int(input())
    p = mov(p, m)

print(p)
