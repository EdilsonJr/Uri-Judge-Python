n = int(input())
dado = [1, 2, 3, 4, 5, 6]

while n > 0:
    n -= 1

    v = []
    v.append(int(input()))
    x = input().split()

    for i in x:
        v.append(int(i))

    v.append(int(input()))
    entradas = sorted(v)

    if entradas != dado or (v[0]+v[5]) != 7 or (v[1]+v[3]) != 7 or (v[2]+v[4]) != 7:
        print('NAO')
    else:
        print('SIM')
