def fibonot(n):
    n1 = 1
    n2 = 2
    n3 = 3
    while n > 0:
        n1 = n2
        n2 = n3
        n3 = n1 + n2
        n -= (n3 - n2 - 1)
    n += (n3 - n2 - 1)
    return n2 + n


n = int(input())
print(fibonot(n))
