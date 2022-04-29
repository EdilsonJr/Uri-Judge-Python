x = int(input())
aux = 0
for i in range(0, 1000):
    if aux < x:
        print(f'N[{i}] = {aux}')
        aux += 1
    else:
        aux = 0
        print(f'N[{i}] = {aux}')
        aux += 1
