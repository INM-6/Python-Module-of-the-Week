from collections import ChainMap

d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
d3 = {**d1, **d2}
chain = ChainMap(d1, d2)

print(chain)

for key, value in chain.items():
    print(key, value)
