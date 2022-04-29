m = int(input())
a = int(input())
b = int(input())

c = ((a + b) - m) * -1

maior = a

if b > maior:
    maior = b

if c > maior:
    maior = c

print(maior)
