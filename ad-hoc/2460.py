n = input()
fila = input().split()
m = input()
saida = input().split()

for i in saida:
    fila.remove(i)

print(*fila)
