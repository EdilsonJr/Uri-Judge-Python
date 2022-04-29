s = [0, 0, 1]

for i in range(3, 18):

    if i % 2 == 0:
        x = s[i - 1] * s[i - 2]
    else:
        x = s[i - 1] + s[i - 2]

    s.append(x)

while True:
    try:
        n = int(input())
        print(s[n])

    except EOFError:
        break
