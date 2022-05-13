casos = 1

while True:
    try:
        x, y = input().split()

        juros = 100 * ((float(y)/float(x))-1)

        print("Projeto %d:" % casos)
        print("Percentual dos juros da aplicacao: %.2f %%" % juros)
        print()

        casos += 1

    except EOFError:
        break