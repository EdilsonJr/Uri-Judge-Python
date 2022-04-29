"""
IMPORTANTE:

* Time limit exceeded
* Preciso arredondar para baixo a saida da media.

"""

def ordenacao(lista, ids):
    for i in range(len(lista)):
        for j in range(len(lista)):
            if lista[i] < lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
                temp = ids[i]
                ids[i] = ids[j]
                ids[j] = temp

    return lista, ids


c = True
casos = 1

while c:
    n = int(input())

    if n == 0:
        c = not c
        break

    div = []
    num = []
    tot_gasto = 0

    for i in range(n):
        moradores, gasto = input().split()
        moradores, gasto = int(moradores), int(gasto)
        tot_gasto += gasto
        x = int(gasto / moradores)
        num.append(moradores)
        div.append(x)

    ordenacao(div, num)
    media = tot_gasto / sum(num)

    for i in range(n):
        try:
            if div[i] == div[i + 1]:
                div.remove(div[i])
                num[i + 1] = num[i] + num[i + 1]
                num.remove(num[i])
                n -= 1
        except:
            pass

    print(f'Cidade# {casos}:')
    for i in range(n):
        if i != n-1:
            print(f'{num[i]}-{div[i]} ', end='')
        else:
            print(f'{num[i]}-{div[i]}')
    print(f'Consumo medio: {media:.2f} m3.')
    print()

    casos += 1

