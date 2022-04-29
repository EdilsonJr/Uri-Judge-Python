soma = 0
x = 0

while x != 1:
    m, n = input().split(" ")
    m = int(m)
    n = int(n)
    soma = 0
    if m > n:
        aux = m
        m = n
        n = aux
    if m <= 0 or n <= 0:
        x = 1
    if x != 1:
        for i in range(m,n+1):
            print(f'{i}', end=" ")
            soma += i
            if i == n:
                print(f'Sum={soma}')
