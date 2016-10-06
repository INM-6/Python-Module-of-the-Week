#!/usr/bin/env python3

import contextlib, io, collections, sys

def test_we_can_import_module():
    import logger

def test_decorator_exists():
    import logger
    logger.logger

def test_wrapped_function_is_callable():
    import logger
    @logger.logger
    def f(): pass

    assert callable(f)

def test_function_can_be_called_with_1_arg():
    import logger
    @logger.logger
    def f(*args): pass

    f(1)

def test_function_can_be_called_with_2_args():
    import logger
    @logger.logger
    def f(*args): pass

    f(2)

def test_function_can_be_called_with_5_args():
    import logger
    @logger.logger
    def f(*args): pass

    f(5)

def test_function_can_be_called_with_named_args():
    import logger
    @logger.logger
    def f(a, b): pass

    f(b=2, a=1)

def test_function_can_be_called_with_mutable_args():
    import logger
    @logger.logger
    def f(a, b): pass

    f(b=[], a={})

def test_function_returns_proper_value():
    import logger
    @logger.logger
    def f(a, b): return a + b

    assert f(4, 5) == 9

def output_with_separator():
    import logger
    @logger.logger
    def myfunc(a, b):
        print('--IN FUNCTION--')
        return a + b

    arg_a, arg_b = 33, 44

    tmp = io.StringIO()
    with contextlib.redirect_stdout(tmp):
        ret = myfunc(arg_a, arg_b)

    expected = arg_a + arg_b
    return arg_a, arg_b, ret, expected, tmp.getvalue()

def test_function_return_value():
    arg_a, arg_b, ret, exp, out = output_with_separator()
    assert ret == exp

def test_function_prints_args():
    arg_a, arg_b, ret, exp, out = output_with_separator()
    before, after = out.split('--IN FUNCTION--')
    assert str(arg_a) in before
    assert str(arg_b) in before

def test_function_prints_return_value():
    arg_a, arg_b, ret, exp, out = output_with_separator()
    before, after = out.split('--IN FUNCTION--')
    assert str(ret) in after

def test_function_uses_called():
    arg_a, arg_b, ret, exp, out = output_with_separator()
    before, after = out.split('--IN FUNCTION--')
    assert ' called ' in before

def test_function_uses_returned():
    arg_a, arg_b, ret, exp, out = output_with_separator()
    before, after = out.split('--IN FUNCTION--')
    assert ' returns ' in after

if __name__ == '__main__':
    import pytest
    pytest.main([__file__] + sys.argv[1:])
