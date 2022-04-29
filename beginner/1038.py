x = input().split()
i, q = x
i = int(i)
q = int(q)


if i == 1:
    tot = q * 4.00
    print(f'Total: R$ {tot:.2f}')

if i == 2:
    tot = q * 4.50
    print(f'Total: R$ {tot:.2f}')

if i == 3:
    tot = q * 5.00
    print(f'Total: R$ {tot:.2f}')

if i == 4:
    tot = q * 2.00
    print(f'Total: R$ {tot:.2f}')

if i == 5:
    tot = q * 1.50
    print(f'Total: R$ {tot:.2f}')
