num = input().split()
x = input().split()
num = [int(i) for i in num]
x = [int(i) for i in x]
qtd = 0

for i in range(6):
    for j in range(6):
        if num[i] == x[j]:
            qtd += 1

if qtd == 3:
    print('terno')
elif qtd == 4:
    print('quadra')
elif qtd == 5:
    print('quina')
elif qtd == 6:
    print('sena')
else:
    print('azar')
