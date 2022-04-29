n = int(input())
maior = 0.0
aluno = 0

for i in range(n):
    a, b = input().split()
    if float(b) > maior:
        maior = float(b)
        aluno = int(a)

if maior >= 8:
    print(aluno)
else:
    print('Minimum note not reached')
