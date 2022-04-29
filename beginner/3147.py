h, e, a, o, w, x = input().split()
h, e, a, o, w, x = int(h), int(e), int(a), int(o), int(w), int(x)

bem = h + e + a + x
mal = o + w

if bem >= mal:
    print('Middle-earth is safe.')
else:
    print('Sauron has returned.')
