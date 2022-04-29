inter = 0
gremio = 0
empates = 0
count = 0
c = True

while c:
    i, g = input().split()
    i = int(i)
    g = int(g)
    count += 1

    if i == g:
        empates += 1

    if i > g:
        inter += 1
    else:
        gremio += 1

    while True:
        print("Novo grenal (1-sim 2-nao)")
        novo = int(input())
        if novo == 2:
            c = False
            break
        elif novo == 1:
            c = True
            break

print(f'{count} grenais')
print(f'Inter:{inter}')
print(f'Gremio:{gremio}')
print(f'Empates:{empates}')
if inter > gremio:
    print('Inter venceu mais')
elif inter == gremio:
    print('Nao houve vencedor')
else:
    print('Gremio venceu mais')
