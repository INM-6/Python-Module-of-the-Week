from functools import partial


def power(base, exponent):
    return base ** exponent


def square(base):
    return power(base, 2)


square = partial(power, exponent=2)
