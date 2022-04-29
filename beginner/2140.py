c = True

while c:
    n, m = map(int, input().split())

    if n == 0 or m == 0:
        c = not c
        break
    else:
        r = m - n
        if r == 7 or r == 12 or r == 22 or r == 52 or r == 102 or r == 15 or r == 25 or r == 55 or r == 105 or r == 30 or r == 60 or r == 110 or r == 70 or r == 120 or r == 150 or r == 200:
            print("possible")
        else:
            print("impossible")
