n = input()

x = int(n)

a = x // 365
x = x % 365
m = x // 30
x = x % 30

print(f'{a} ano(s)')
print(f'{m} mes(es)')
print(f'{x} dia(s)')
