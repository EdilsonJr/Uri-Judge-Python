n = int(input())

for i in range(n):
    x = input().split()
    x = [int(i) for i in x]
    aux = x[0]
    soma = 0
    for j in range(1, aux+1):
        soma += x[j]

    print(soma - aux + 1)
