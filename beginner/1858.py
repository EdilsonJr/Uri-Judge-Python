n = int(input())
x = input().split()

for i in range(n):
    x[i] = int(x[i])

m = min(x)
result = x.index(m) + 1

print(result)
