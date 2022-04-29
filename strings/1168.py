n = int(input())

for i in range(n):
    x = input()
    tam = len(x)
    leds = 0
    for j in range(tam):
        if x[j] == '1':
            leds += 2
        if x[j] == '2':
            leds += 5
        if x[j] == '3':
            leds += 5
        if x[j] == '4':
            leds += 4
        if x[j] == '5':
            leds += 5
        if x[j] == '6':
            leds += 6
        if x[j] == '7':
            leds += 3
        if x[j] == '8':
            leds += 7
        if x[j] == '9':
            leds += 6
        if x[j] == '0':
            leds += 6

    print(f'{leds} leds')
