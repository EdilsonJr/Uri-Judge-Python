while True:
    try:
        a = int(input())
        s = 1 + a / 100;

        if a % 100 == 0:
            s -= 1

        s = int(s)
        print(s)

    except EOFError:
        break
