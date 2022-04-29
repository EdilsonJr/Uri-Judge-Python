n = int(input())
soma = 0
for i in range(n):
    a, b = input().split()
    b = int(b)

    if a == '1001':
        x = 1.50 * b
    elif a == '1002':
        x = 2.50 * b
    elif a == '1003':
        x = 3.50 * b
    elif a == '1004':
        x = 4.50 * b
    else:
        x = 5.50 * b

    soma += x

print(f'{soma:.2f}')
