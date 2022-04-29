while True:
    try:
        h = input()
        h = h.split(':')

        hora = int(h[0]) + 1
        minuto = int(h[1])

        aux = hora - 8

        if aux < 0:
            print('Atraso maximo: 0')
        else:
            minuto += 60 * aux
            print(f'Atraso maximo: {minuto}')

    except EOFError:
        break
