import math
l1 = input().split(" ")
l2 = input().split(" ")

x1, y1 = l1
x2, y2 = l2

x = math.sqrt(((float(x2) - float(x1)) ** 2) + ((float(y2) - float(y1)) ** 2))

print(f'{x:.4f}')
