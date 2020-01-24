import functools


def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        print('here I could do something beforehand')
        func(*args, **kwargs)
        func(*args, **kwargs)
        print('here I could do something beforehand')
    return wrapper_do_twice


@do_twice
def print_hello(name=''):
    print(f"hello {name}")


print(print_hello.__name__)
