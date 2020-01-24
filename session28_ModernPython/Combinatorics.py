import itertools

abc = 'ABC'
print('permutations:')
for p in itertools.permutations(abc):
    print(p)

print('with no repetition')
for c in itertools.combinations(abc, 2):
    print(c)

print('with replacement:')
for c in itertools.combinations_with_replacement(abc, 2):
    print(c)
