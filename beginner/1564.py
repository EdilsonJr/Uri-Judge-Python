entrada = []
cont = 0
while True:
    try:
        x = int(input())
        entrada.append(x)
        cont += 1
    except:
        break

for i in entrada[0:cont]:
    if i == 0:
        print('vai ter copa!')
    if i != 0:
        print('vai ter duas!')
