m = 0
aux = 0

while True:
    try:
        n = int(input())
        if aux > n and m == 0:
            m = aux + 1
        aux = n

    except EOFError:
        break

if m == 0:
    m = aux + 1

print(m)
