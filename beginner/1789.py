while True:
    try:
        n = int(input())
        x = input().split()
        x = [int(i) for i in x]
        x = sorted(x, reverse=True)

        if x[0] >= 20:
            print(3)
        elif x[0] < 10:
            print(1)
        else:
            print(2)

    except EOFError:
        break
