n = int(input())
x = input().split()
x = [int(i) for i in x]
total = sum(x)
ataque = [0] * n
i = 0

while i >= 0 and i < n:
    direcao = x[i] % 2
    if x[i] > 0:
        x[i] -= 1
        ataque[i] = 1
        total -= 1
    if direcao:
        i += 1
    else:
        i -= 1

ataque = ataque.count(1)
print(ataque, total)
