#!/usr/bin/env python3

import sys
import numpy as np
import pytest

def generator(n):
    for i in range(n):
        yield i

def test_we_can_import_listize():
    import listize

def test_listize_exists():
    import listize
    listize.listize

def test_listized_function_is_callable():
    import listize
    wrapped = listize.listize(generator)
    assert callable(wrapped)

def test_listized_function_returns_a_list():
    import listize
    wrapped = listize.listize(generator)
    for n in range(20):
        assert wrapped(n) == list(range(n))

def test_listized_function_can_be_called_with_named_args():
    import listize
    wrapped = listize.listize(generator)

    ans = wrapped(n=2)
    assert ans == [0, 1]

def test_listized_function_can_be_called_with_mutable_args():
    import listize
    @listize.listize
    def f(a, b):
        yield len(a)
        yield len(b)

    ans = f(b=[1, 2, 3], a={3, 4, 5})
    assert ans == [3, 3]

############################################################
# Functions below are for the optional part of the exercise.
# They use pytest magic to skip the tests if arrayize.py
# does not exist.

def test_arrayize_exists():
    arrayize = pytest.importorskip('arrayize')
    arrayize.arrayize

def test_arrayized_function_is_callable():
    arrayize = pytest.importorskip('arrayize')
    wrapped = arrayize.arrayize(generator)
    assert callable(wrapped)

def test_arryized_function_returns_an_array():
    arrayize = pytest.importorskip('arrayize')
    wrapped = arrayize.arrayize(generator)
    for n in range(1, 20):
        ans = wrapped(n)
        assert all(ans == list(range(n)))
        assert isinstance(ans, np.ndarray)

def test_arryized_function_returns_empty_array():
    arrayize = pytest.importorskip('arrayize')
    wrapped = arrayize.arrayize(generator)
    ans = wrapped(0)
    assert len(ans) == 0
    assert isinstance(ans, np.ndarray)

def test_arrayized_function_can_be_called_with_named_args():
    arrayize = pytest.importorskip('arrayize')
    @arrayize.arrayize
    def f(a, b):
        yield 123

    ans = f(b=2, a=1)
    assert ans == [123]
    assert isinstance(ans, np.ndarray)

def test_arrayized_function_can_be_called_with_mutable_args():
    arrayize = pytest.importorskip('arrayize')
    @arrayize.arrayize
    def f(a, b):
        yield len(a)
        yield len(b)

    ans = f(b=[1, 2, 3], a={3, 4, 5})
    assert all(ans == [3, 3])
    assert isinstance(ans, np.ndarray)

if __name__ == '__main__':
    pytest.main([__file__] + sys.argv[1:])
