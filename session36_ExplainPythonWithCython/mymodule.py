# cython: language_level=3

rate_orig = 12.43


def add_inplace(rate):
    print(rate is rate_orig)
    rate += 20
    print(rate is rate_orig)


add_inplace(rate_orig)
