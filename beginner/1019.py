n = input()

x = int(n)

h = x // 3600
x = x % 3600
m = x // 60
x = x % 60

print(f'{h}:{m}:{x}')
