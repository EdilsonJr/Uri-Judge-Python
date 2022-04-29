par = []
imp = []
cont = 0
p = 0
i = 0

while cont < 15:
    x = int(input())
    if x % 2 == 0:
        par.append(x)
        p += 1
    if x % 2 != 0:
        imp.append(x)
        i += 1
    if p > 4:
        for c in range(0, 5):
            print(f'par[{c}] = {par[c]}')
        par = []
        p = 0
    if i > 4:
        for c in range(0, 5):
            print(f'impar[{c}] = {imp[c]}')
        imp = []
        i = 0
    cont = cont + 1

if i > 0:
    for j in range(i):
        print(f'impar[{j}] = {imp[j]}')
if p > 0:
    for h in range(p):
        print(f'par[{h}] = {par[h]}')
