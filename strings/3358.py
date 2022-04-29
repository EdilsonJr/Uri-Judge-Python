n = int(input())

for i in range(n):
    x = input()
    aux = 0
    c = True

    for j in x:
        if j == 'A' or j == 'a' or j == 'E' or j == 'e' or j == 'I' or j == 'i' or \
                j == 'O' or j == 'o' or j == 'U' or j == 'u':
            aux = 0
        else:
            aux += 1
            if aux == 3:
                c = False
                break

    if c:
        print(f'{x} eh facil')
    else:
        print(f'{x} nao eh facil')
