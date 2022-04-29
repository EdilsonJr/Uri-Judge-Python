a = int(input())
b = int(input())

if a < 6 or b < 6:
    print('NO')
elif a >= 18 or b >= 18:
    print('YES')
elif a >= 14 and b >= 14:
    print('YES')
else:
    print('NO')
