n = int(input())

for i in range(n):
    a, b = input().split()
    a, b = int(a), int(b)

    total = int((a % b) + (a / b))

    print(total)
