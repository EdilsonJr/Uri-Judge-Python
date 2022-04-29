n = int(input())
x = []
x = input().split()
q = 0

for i in range(1, n):
    if (int(x[i - 1]) > int(x[i])):
        q = i + 1
        break

print(q)
