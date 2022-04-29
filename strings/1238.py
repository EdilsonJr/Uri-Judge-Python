n = int(input())

for i in range(n):
    s1, s2 = input().split()
    c = []

    if len(s1) > len(s2):
        maior = len(s1)
    else:
        maior = len(s2)

    for k in range(maior):
        try:
            c.append(s1[k])
        except:
            pass

        try:
            c.append(s2[k])
        except:
            pass

    print(*c, sep='')
