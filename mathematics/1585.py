n = int(input())

for i in range(n):
    a, b = input().split()
    a, b = int(a), int(b)
    c = (a * b)/2
    c = int(c)

    print(f'{c} cm2')
