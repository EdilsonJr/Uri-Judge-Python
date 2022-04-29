lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
aux = 0
temp = 97
for i in range(26):
    print(f'{temp} e {lista[aux]}')
    aux += 1
    temp += 1
