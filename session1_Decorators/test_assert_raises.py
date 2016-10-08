#!/usr/bin/env python3

import sys

def test_we_can_import_module():
    import assert_raises

def test_context_manager_exists():
    import assert_raises
    assert_raises.assert_raises

def test_context_manager_raises_exception():
    import assert_raises
    with assert_raises.assert_raises(Exception):
        1 / 0

def test_unexpected_success():
    import assert_raises
    try:
        with assert_raises.assert_raises(ZeroDivisionError):
            pass
    except AssertionError:
        pass
    else:
        raise AssertionError('AssertionError was not raised')

def test_cm_checks_exception_type():
    import assert_raises
    try:
        with assert_raises.assert_raises(ZeroDivisionError):
            raise ValueError
    except AssertionError:
        pass
    else:
        raise AssertionError('AssertionError was not raised')

if __name__ == '__main__':
    import pytest
    pytest.main([__file__] + sys.argv[1:])
