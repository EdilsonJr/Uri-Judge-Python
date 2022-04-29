n = 0
soma = 0
while n != 2:
    nota = float(input())
    if 0 <= nota <= 10:
        soma += nota
        n += 1
    else:
        print('nota invalida')

media = soma / 2
print(f'media = {media:.2f}')
