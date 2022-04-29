n = int(input())

for i in range(n):
    ent = input()

    d1 = ent[2] + ent[3]
    d1 = int(d1)
    d2 = ent[5] + ent[6] + ent[7]
    d2 = int(d2)
    d3 = ent[11] + ent[12]
    d3 = int(d3)

    soma = d1 + d2 + d3

    print(soma)

