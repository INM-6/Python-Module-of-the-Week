#!/usr/bin/env python3

import contextlib, io, collections, sys

def test_we_can_import_module():
    import deprecate

def test_decorator_exists():
    import deprecate
    deprecate.deprecate

def test_wrapped_function_is_callable():
    import deprecate
    @deprecate.deprecate('boo')
    def f(): pass

    assert callable(f)

def test_function_can_be_called_with_1_arg():
    import deprecate
    @deprecate.deprecate('boo')
    def f(*args): pass

    f(1)

def test_function_can_be_called_with_2_args():
    import deprecate
    @deprecate.deprecate('boo')
    def f(*args): pass

    f(2)

def test_function_can_be_called_with_5_args():
    import deprecate
    @deprecate.deprecate('boo')
    def f(*args): pass

    f(5)

def test_function_can_be_called_with_named_args():
    import deprecate
    @deprecate.deprecate('boo')
    def f(a, b): pass

    f(b=2, a=1)

def test_function_can_be_called_with_mutable_args():
    import deprecate
    @deprecate.deprecate('boo')
    def f(a, b): pass

    f(b=[], a={})

def test_function_returns_proper_value():
    import deprecate
    @deprecate.deprecate('boo')
    def f(a, b): return a + b

    assert f(4, 5) == 9

MESSAGE = 'use foobar instead'

def output_when_run_twice():
    import deprecate
    @deprecate.deprecate(MESSAGE)
    def myfunc(a, b):
        print('--IN FUNCTION--')
        return a + b

    arg_a, arg_b = 33, 44

    tmp = io.StringIO()
    with contextlib.redirect_stdout(tmp):
        ret1 = myfunc(arg_a, arg_b)
        ret2 = myfunc(arg_a, arg_b)

    expected = arg_a + arg_b
    return arg_a, arg_b, ret1, ret2, expected, tmp.getvalue()

def test_function_return_value():
    arg_a, arg_b, ret1, ret2, exp, out = output_when_run_twice()
    assert ret1 == exp
    assert ret2 == exp

def test_function_prints_warning():
    arg_a, arg_b, ret1, ret2, exp, out = output_when_run_twice()
    assert 'is deprecated' in out

def test_function_uses_function_name():
    arg_a, arg_b, ret1, ret2, exp, out = output_when_run_twice()
    assert 'myfunc' in out

def test_function_uses_message():
    arg_a, arg_b, ret1, ret2, exp, out = output_when_run_twice()
    assert MESSAGE in out

def test_function_prints_once():
    arg_a, arg_b, ret1, ret2, exp, out = output_when_run_twice()
    assert out.count('is deprecated') == 1

if __name__ == '__main__':
    import pytest
    pytest.main([__file__] + sys.argv[1:])
