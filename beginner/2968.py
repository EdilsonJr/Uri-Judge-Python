import math
a, b = input().split()
a = int(a)
b = int(b)
placas = a * b
result = []

for i in range(1, 10):
    perc = i / 10
    qtd = math.ceil(placas * perc)
    result.append(qtd)

print(*result)
