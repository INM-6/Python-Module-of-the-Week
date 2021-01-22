def myGenerator1(n):
    for i in range(n):
        yield i


def myGenerator2(n, m):
    for j in range(n, m):
        yield j


def myGenerator3(n, m):
    yield from myGenerator1(n)
    yield from myGenerator2(n, m)
    yield from myGenerator2(m, m+5)


def N(n=1):
    yield n
    yield from N(n+1)


def P(G):
    m = next(G)
    yield m
    yield from P(i for i in G if i % m != 0)


for n in N():
    print(n)
    if n > 30:
        break

p = P(N(2))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))

