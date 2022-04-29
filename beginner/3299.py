n = input()
tam = len(n)
c = True

for i in range(tam):
    if n[i] == '1':
        if i+1 < tam:
            if n[(i+1)] == '3':
                c = not c
                break

if c:
    print(f'{n} NO es de Mala Suerte')
else:
    print(f'{n} es de Mala Suerte')
