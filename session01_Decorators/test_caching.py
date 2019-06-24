#!/usr/bin/env python3

import sys, math

def test_we_can_import_module():
    import caching

def test_decorator_exists():
    import caching
    caching.caching

def test_wrapped_function_is_callable():
    import caching
    @caching.caching
    def f(): pass

    assert callable(f)

def test_function_can_be_called_with_1_arg():
    import caching
    @caching.caching
    def f(*args): pass

    f(1)

def test_function_can_be_called_with_2_args():
    import caching
    @caching.caching
    def f(*args): pass

    f(2)

def test_function_can_be_called_with_5_args():
    import caching
    @caching.caching
    def f(*args): pass

    f(5)

def test_function_can_be_called_with_named_args():
    import caching
    @caching.caching
    def f(a, b): pass

    f(b=2, a=1)

def test_function_can_be_called_with_mutable_args():
    import caching
    @caching.caching
    def f(a, b): pass

    f(b=[], a={})

def test_function_returns_proper_value():
    import caching
    @caching.caching
    def f(a, b): return a + b

    assert f(4, 5) == 9

def _factorial(n, counter=None):
    if counter:
        counter[0] += 1

    if n <= 1:
        return 1
    else:
        return n * _factorial(n-1, counter)

def test_factorial_value():
    for n in range(10):
        ans = _factorial(n)
        assert ans == math.factorial(n)

def _test_factorial_caching(n):
    counter = [0]
    _factorial(n, counter)
    assert counter[0] == n

def test_factorial_caching_1():
    _test_factorial_caching(1)

def test_factorial_caching_10():
    _test_factorial_caching(10)

def test_factorial_caching_30():
    _test_factorial_caching(30)

if __name__ == '__main__':
    import pytest
    pytest.main([__file__] + sys.argv[1:])
