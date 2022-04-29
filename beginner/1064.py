y = 0
tot = 0
for x in range(1,7):
    a = float(input())
    if a > 0:
        y = y + 1
        tot = tot + a
print(f'{y} valores positivos')
media = tot / y
print(f'{media:.1f}')
