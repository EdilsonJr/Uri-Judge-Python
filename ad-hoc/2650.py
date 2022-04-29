n, t = input().split()
n, t = int(n), int(t)
titans = []

while n:
    n -= 1
    x = input().split()
    if int(x[-1]) > t:
        titans.append(' '.join(x[:-1]))

for j in titans:
    print(j)
