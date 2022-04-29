n = int(input())
car = 0
bon = 0

for i in range(n):
    a, b = input().split()

    if b == 'M':
        car += 1

    if b == 'F':
        bon += 1

print(f'{car} carrinhos')
print(f'{bon} bonecas')
