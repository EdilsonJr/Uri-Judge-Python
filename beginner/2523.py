while True:
    try:
        letras = input()
        n = int(input())
        l = [int(x) for x in input().split()]
        n = ''
        for x in l:
            n += letras[x - 1]
        print(n)

    except EOFError:
        break
