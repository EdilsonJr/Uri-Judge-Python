c = True
count = 0
soma = 0
while c:
    x = int(input())
    if x < 0:
        c = False
        break
    else:
        soma += x
        count += 1

media = soma / count
print(f'{media:.2f}')
