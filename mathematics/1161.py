while True:
    try:
        m, n = input().split()
        m, n = int(m), int(n)
        v1, v2 = 0, 0

        if m == 0 or m == 1:
            v1 = 1
        else:
            v1 = m
            for i in range(m - 1, 0, -1):
                v1 = v1 * i

        if n == 0 or n == 1:
            v2 = 1
        else:
            v2 = n
            for i in range(n - 1, 0, -1):
                v2 = v2 * i

        print(v1 + v2)

    except EOFError:
        break
