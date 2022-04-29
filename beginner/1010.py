l1 = input().split(" ")
l2 = input().split(" ")

c1, q1, v1 = l1
c2, q2, v2 = l2

total = (int(q1) * float(v1)) + (int(q2) * float(v2))

print(f'VALOR A PAGAR: R$ {total:.2f}')
