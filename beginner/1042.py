x = input().split()
v = [int(i) for i in x]

v.sort()
print(*v, sep='\n')
print()
print(*x, sep='\n')
