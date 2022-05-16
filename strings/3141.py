nome = input()
da, ma, aa = input().split('/')
dn, mn, an = input().split('/')
da, ma, aa = int(da), int(ma), int(aa)
dn, mn, an = int(dn), int(mn), int(an)

idade = aa - an

d = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]

xa = d[ma - 1] + da
xn = d[mn - 1] + dn

if ma == mn and da == dn:
    print('Feliz aniversario!')
    print(f'Voce tem {idade} anos {nome}.')
elif ma > mn:
    print(f'Voce tem {idade} anos {nome}.')
else:
    if ma == mn:
        if da > dn:
            print(f'Voce tem {idade} anos {nome}.')
        else:
            if (idade - 1) < 0:
                idade = idade
            else:
                idade -= 1
            print(f'Voce tem {idade} anos {nome}.')
    else:
        if (idade - 1) < 0:
            idade = idade
        else:
            idade -= 1
        print(f'Voce tem {idade} anos {nome}.')
