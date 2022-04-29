n = int(input())
figurinhas = []
repetidas = []
valores = []

for i in range(n):
    x = int(input())
    figurinhas.append(x)

for figurinha in figurinhas:
    if figurinha not in valores:
        valores.append(figurinha)
    else:
        repetidas.append(figurinha)

print(len(valores))
print(len(repetidas))
