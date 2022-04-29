n = int(input())
x = input().split()
x = [int(i) for i in x]
aux = 0

for i in range(5):
    if n == x[i]:
        aux += 1

print(aux)
