n = int(input())
x = 0

for i in range(1,100):
    a = int(input())
    if a > x:
        m = a
        p = i + 1
        x = a

print(m)
print(p)
