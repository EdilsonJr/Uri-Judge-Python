n = int(input())

for i in range(n):
    texto = input()
    x = int(input())
    saida = ''
    for j in texto:
        posicao = ord(j)-x

        if posicao < 65:
            saida += chr(91-(65-posicao))
        else:
            saida += chr(ord(j)-x)
    print(saida)
