n = int(input())
q_c= 0
q_r= 0
q_s= 0
q_t = 0

for i in range(1, n + 1):
    x = input().split()
    qtd, tipo = x
    if tipo == 'C':
        q_c = q_c + int(qtd)
    if tipo == 'R':
        q_r = q_r + int(qtd)
    if tipo == 'S':
        q_s = q_s + int(qtd)
    q_t = q_t + int(qtd)

p_c = (q_c / q_t) * 100
p_r = (q_r / q_t) * 100
p_s = (q_s / q_t) * 100

print(f'Total: {q_t} cobaias')
print(f'Total de coelhos: {q_c}')
print(f'Total de ratos: {q_r}')
print(f'Total de sapos: {q_s}')
print(f'Percentual de coelhos: {p_c:.2f} %')
print(f'Percentual de ratos: {p_r:.2f} %')
print(f'Percentual de sapos: {p_s:.2f} %')
