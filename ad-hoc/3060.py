v = int(input())
p = int(input())

total = (v // p) * p

if total == v:
    for i in range(p):
        print(v // p)
else:
    dif = v - total
    for i in range(dif):
        print((v // p) + 1)
    for i in range(p - dif):
        print(v // p)
