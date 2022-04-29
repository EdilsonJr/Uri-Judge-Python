a = input()

x = int(a)

x1 = x // 100
x = x % 100
x2 = x // 50
x = x % 50
x3 = x // 20
x = x % 20
x4 = x // 10
x = x % 10
x5 = x // 5
x = x % 5
x6 = x // 2
x = x % 2
x7 = x // 1
x = x % 1

print(a)
print(f'{x1} nota(s) de R$ 100,00')
print(f'{x2} nota(s) de R$ 50,00')
print(f'{x3} nota(s) de R$ 20,00')
print(f'{x4} nota(s) de R$ 10,00')
print(f'{x5} nota(s) de R$ 5,00')
print(f'{x6} nota(s) de R$ 2,00')
print(f'{x7} nota(s) de R$ 1,00')
