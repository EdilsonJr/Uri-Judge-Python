def aux(a, b):
    if b == 0:
        return a
    else:
        return aux(b, a % b)


x, y = input().split('.')
x, y = int(x), int(y)

s = 36000 / aux(36000, 100 * x + y)
s = int(s)

print(s)
