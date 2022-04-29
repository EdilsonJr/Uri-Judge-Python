a, b, c = input().split()
a, b, c = int(a), int(b), int(c)

if a > b:
    if c > b:
        print(':)')
    else:
        if b - c < a - b:
            print(':)')
        else:
            print(':(')

elif a < b:
    if c < b:
        print(':(')
    else:
        if b - c > a - b:
            print(':(')
        else:
            print(':)')

else:
    if c > a:
        print(':)')
    else:
        print(':(')
