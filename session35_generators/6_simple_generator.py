def very_simple_generator():
    yield 1
    yield 2
    yield 'dog'
    yield lambda x: x**2
    yield {'a': 'b'}


for i in very_simple_generator():
    print(i)


# can go on forever
def generate_all_numbers_starting_from(N):
    i = N
    while(True):
        yield i
        i += 1


for a in generate_all_numbers_starting_from(12):
    print(a)
    if a > 27:
        break


# can do all the things iterators do
def generate_all_numbers_smaller(N):
    for i in range(N):
        yield i


a, b, c = generate_all_numbers_smaller(3)
