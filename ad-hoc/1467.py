while True:
    try:
        a, b, c = input().split()
        a, b, c = int(a), int(b), int(c)

        if a == b == c:
            print("*")
        else:
            if a == b:
                print("C")
            else:
                if a == c:
                    print("B")
                else:
                    print("A")

    except EOFError:
        break
