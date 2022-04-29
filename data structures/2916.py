""" Runtime """

while True:
    try:
        n, k = input().split()
        n, k = int(n), int(k)

        notas = input().split()
        notas = [int(i) for i in notas]
        notas = sorted(notas, reverse=True)

        soma = 0

        for i in range(k):
            soma += notas[i]

        print(soma)

    except EOFError:
        break
