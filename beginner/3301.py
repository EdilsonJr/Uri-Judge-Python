h, z, l = input().split()
h = int(h)
z = int(z)
l = int(l)
lista = [h, z, l]
o = sorted(lista)

if h == o[1]:
    print('huguinho')
elif z == o[1]:
    print('zezinho')
else:
    print('luisinho')
