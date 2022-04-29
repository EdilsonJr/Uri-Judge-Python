num = input().split()
x = input().split()
qtd = False

for i in range(5):
    if num[i] == x[i]:
        qtd = True
        break

if qtd:
    print('N')
else:
    print('Y')
