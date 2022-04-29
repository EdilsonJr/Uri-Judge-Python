n = int(input())

for i in range(n):
    a, b = input().split()
    a, b = int(a), int(b)

    c = a + b

    if c == 0:
        print('PROXYCITY')
    elif c == 1:
        print('P.Y.N.G.')
    elif c == 2:
        print('DNSUEY!')
    elif c == 3:
        print('SERVERS')
    elif c == 4:
        print('HOST!')
    elif c == 5:
        print('CRIPTONIZE')
    elif c == 6:
        print('OFFLINE DAY')
    elif c == 7:
        print('SALT')
    elif c == 8:
        print('ANSWER!')
    elif c == 9:
        print('RAR?')
    else:
        print('WIFI ANTENNAS')
