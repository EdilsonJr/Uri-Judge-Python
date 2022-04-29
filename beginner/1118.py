soma = 0
cont = 0
c = True

while c:
    nota = float(input())

    if 0 <= nota <= 10:
        soma += nota
        cont += 1

        if cont == 2:

            print("media = %.2f" % (soma / 2))
            cont = 0
            soma = 0

            while True:
                print("novo calculo (1-sim 2-nao)")
                novo = int(input())
                if novo == 2:
                    c = False
                    break
                elif novo == 1:
                    c = True
                    break

    else:
        print("nota invalida")
