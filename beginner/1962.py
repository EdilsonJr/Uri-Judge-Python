n = int(input())
aux = 2015

for i in range(n):
    x = int(input())
    if x == aux:
        print('1 A.C.')
    elif x > aux:
        valor = x - aux + 1
        print(f'{valor} A.C.')
    else:
        valor = aux - x
        print(f'{valor} D.C.')
