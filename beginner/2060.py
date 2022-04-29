n = int(input())
x = input().split()
x = [int(i) for i in x]
m2 = 0
m3 = 0
m4 = 0
m5 = 0

for i in range(n):
    if x[i] % 2 == 0:
        m2 += 1
    if x[i] % 3 == 0:
        m3 += 1
    if x[i] % 4 == 0:
        m4 += 1
    if x[i] % 5 == 0:
        m5 += 1

print(f'{m2} Multiplo(s) de 2')
print(f'{m3} Multiplo(s) de 3')
print(f'{m4} Multiplo(s) de 4')
print(f'{m5} Multiplo(s) de 5')
