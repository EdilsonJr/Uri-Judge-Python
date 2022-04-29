n = int(input())

a = input()
a = a.split()

for i in range(len(a)):
    a[i] = int(a[i])

m = a[0]
p = 0
for j in range(1, len(a)):
    if a[j] < m:
        m = a[j]
        p = j

print(f'Menor valor: {m}')
print(f'Posicao: {p}')
