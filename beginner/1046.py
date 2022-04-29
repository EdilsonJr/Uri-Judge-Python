x = input().split()
a, b = x
a = int(a)
b = int(b)

if a == b:
    print('O JOGO DUROU 24 HORA(S)')
elif a < b:
    temp = b - a
    print(f'O JOGO DUROU {temp} HORA(S)')
else:
    temp = (24 - a) + b
    print(f'O JOGO DUROU {temp} HORA(S)')
