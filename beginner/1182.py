matriz = []
soma = 0.0
ind = int(input())
o = input()

for i in range(12):
    linha = []
    for j in range(12):
        numero = float(input())
        linha.append(numero)
    matriz.append(linha)

for a in range(12):
    for b in range(12):
        if b == ind:
            soma += matriz[a][b]

if o == "S":
    print(f'{soma:.1f}')
elif o == "M":
    print(f'{soma/12:.1f}')
