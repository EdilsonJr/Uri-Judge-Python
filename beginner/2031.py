n = int(input())

for i in range(n):
    j1 = input()
    j2 = input()

    if j1 == 'ataque':
        if j2 == 'ataque':
            print('Aniquilacao mutua')
        else:
            print('Jogador 1 venceu')

    elif j2 == 'ataque':
        print('Jogador 2 venceu')

    elif j1 == 'papel':
        if j2 == 'papel':
            print('Ambos venceram')
        else:
            print('Jogador 2 venceu')

    elif j2 == 'papel':
        print('Jogador 1 venceu')

    else:
        print('Sem ganhador')
