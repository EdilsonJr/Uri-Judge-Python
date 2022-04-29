x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
v = int(input())

for i in range(len(x)):
    x[i] = v
    v = v * 2
    print(f'N[{i}] = {x[i]}')