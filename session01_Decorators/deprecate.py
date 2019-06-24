# -*- coding: utf-8 -*-
"""
Exercise — keeping state in decorators

Write a decorator which prints a warning the first
time a given function is executed. This is a modification
of deprecate() from previous exercise.

@deprecate('do not use')
def f(): pass

>>> f()
f is deprecated, do not use
>>> f()
>>> f()

The trick is how to store the state!
"""

import functools

def deprecate(msg):
    def decorator(func):
        func._warning = True
        def wrapper(*args, **kwargs):
            if func._warning:
                print(func.__name__, 'is deprecated,', msg)
                func._warning = False
            return func(*args, **kwargs)
        return functools.update_wrapper(wrapper, func)
    return decorator

if 0:
    def deprecate(msg):
        def decorator(func):
            warning = [True]
            def wrapper(*args, **kwargs):
                if warning[0]:
                    print(func.__name__, 'is deprecated,', msg)
                    warning[0] = False
                return func(*args, **kwargs)
            return functools.update_wrapper(wrapper, func)
        return decorator

if 0:
    def deprecate_using_nonlocal(msg):
        def decorator(func):
            warning = True
            def wrapper(*args, **kwargs):
                nonlocal warning
                if warning:
                    print(func.__name__, 'is deprecated,', msg)
                    warning = False
                return func(*args, **kwargs)
            return functools.update_wrapper(wrapper, func)
        return decorator
