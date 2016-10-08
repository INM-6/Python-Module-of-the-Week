#!/usr/bin/env python3

import sys

def test_we_can_import_module():
    import printtime

def test_decorator_exists():
    import printtime
    printtime.printtime

def test_wrapped_function_is_callable():
    import printtime
    @printtime.printtime
    def f(): pass

    assert callable(f)

def test_function_can_be_called_with_1_arg():
    import printtime
    @printtime.printtime
    def f(*args): pass

    f(1)

def test_function_can_be_called_with_2_args():
    import printtime
    @printtime.printtime
    def f(*args): pass

    f(2)

def test_function_can_be_called_with_5_args():
    import printtime
    @printtime.printtime
    def f(*args): pass

    f(5)

def test_function_can_be_called_with_named_args():
    import printtime
    @printtime.printtime
    def f(a, b): pass

    f(b=2, a=1)

def test_function_can_be_called_with_mutable_args():
    import printtime
    @printtime.printtime
    def f(a, b): pass

    f(b=[], a={})

TEST_CASES = [(1, 2, 3),
              (1.0, 2.0, 3.0),
              ("a", "b", "ab"),
              ((), (), ()),
              ((1,2,3), (4, 5, 6), tuple(range(1, 7))),
              ([], [], []),
              ([1,2,3], [4, 5, 6], list(range(1, 7)))]

def test_function_returns_proper_value_0_args():
    import printtime
    @printtime.printtime
    def f(): return 234

    assert f() == 234

def test_function_returns_proper_value_1_arg():
    import printtime
    @printtime.printtime
    def f(a): return 234

    assert f(11) == 234

def test_function_returns_proper_value_2_args():
    import printtime
    @printtime.printtime
    def f(a, b): return 234

    assert f(12, 'second arg') == 234

if __name__ == '__main__':
    import pytest
    pytest.main([__file__] + sys.argv[1:])
