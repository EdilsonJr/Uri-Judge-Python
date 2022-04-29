n = int(input())
b = 0
aux = n * n
p = aux / 2

if aux % 2 != 0:
    b = (aux / 2) + 1

else:
    b = aux / 2

b = int(b)
p = int(p)

print(f'{b} casas brancas e {p} casas pretas')
