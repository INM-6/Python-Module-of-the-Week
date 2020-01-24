s = sum([i**2 for i in range(3)])
print(s)

s = sum(i**2 for i in range(3))
print(s)

d = dict((i, i % 7) for i in range(12))
print(d)
