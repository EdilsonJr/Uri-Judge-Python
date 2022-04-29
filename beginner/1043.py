x = input().split()
v = [float(i) for i in x]
v.sort()
a1, b1, c1 = v
a, b, c = x
a = float(a)
b = float(b)
c = float(c)

if (a1+b1) > c1:
    soma = a1+b1+c1
    print(f'Perimetro = {soma:.1f}')
else:
    soma = ((a+b) * c) / 2
    print(f'Area = {soma:.1f}')
