n = int(input())
x = input().split()
aux = 0

for i in range(n):
    if x[i] == '1':
        aux += 1

print(aux)
