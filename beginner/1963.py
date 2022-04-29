a, b = input().split()
a, b = float(a), float(b)

p = (b * 100 / a) - 100

print(f'{p:.2f}%')
