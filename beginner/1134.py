i = 0
alcool = 0
gasol = 0
diesel = 0

while i != 4:
    x = int(input())
    if x == 4:
        i = 4
    if x == 1:
        alcool += 1
    if x == 2:
        gasol += 1
    if x == 3:
        diesel += 1

print('MUITO OBRIGADO')
print(f'Alcool: {alcool}')
print(f'Gasolina: {gasol}')
print(f'Diesel: {diesel}')
