n = int(input())

for i in range(n):
    a, b = input().split()
    a, b = int(a), int(b)
    c = a ** b
    c = str(c)

    print(len(c))
