n = int(input())
g = 0
v = 0

for i in range(n):
    x, y = input().split()
    if x == 'G':
        g += int(y)
    else:
        v += int(y)

if v >= g:
    print('A greve vai parar.')
else:
    print('NAO VAI TER CORTE, VAI TER LUTA!')
