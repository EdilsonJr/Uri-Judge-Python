n = int(input())
s = input().split()

for x, i in enumerate(s):
    if i[0:2] == 'UR' and len(i) == 3:
        s[x] = 'URI'
    if i[0:2] == 'OB' and len(i) == 3:
        s[x] = 'OBI'

i = ' '.join(s)

print(i)
