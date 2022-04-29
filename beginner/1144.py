n = int(input())
x = 1
for i in range (1, n + 1):
    print(x, x*x, x**3)
    print(x, (x*x)+1, (x**3)+1)
    x += 1
