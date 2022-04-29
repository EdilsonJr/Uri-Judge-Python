p, n = input().split()
p, n = int(p), int(n)
cond = True
lista = input().split()
lista = [int(i) for i in lista]
new = []

for i in range(n-1):
   aux = abs(lista[i] - lista[i+1])
   new.append(aux)

for i in new:
    if i > p:
        cond = not cond

if cond:
    print('YOU WIN')
else:
    print('GAME OVER')
