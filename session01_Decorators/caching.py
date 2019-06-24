# -*- coding: utf-8 -*-
"""
Exercise — a cache

Write a decorator which caches the results of some
function. Store the results of every invocation.
Every time the function is called with the same
arguments, simply retrieve the value from storage.
Otherwise call the function.

>>> @cached
>>> def f(x): print('here')

>>> f(3)
here
>>> f(3)
"""

import functools

def fibonacci(n):
    "This function can be used for testing…"
    if n <= 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

def caching(func):
    argdict = {}
    def wrapper(*args):
        if args in argdict:
            return argdict[args]
        else:
            res = func(*args)
            argdict[args] = res
            return res
    return wrapper

if 0:
    def caching(func):
        return functools.lru_cache()(func)    # ;)

if 0:
    def caching(func):
        argdict = {}
        def wrapper(*args, **kwargs):
            key = args, tuple(sorted(kwargs.items()))
            try:
                hash(key)
            except TypeError:
                # not hashable
                return func(*args, **kwargs)

            try:
                return argdict[key]
            except KeyError:
                res = func(*args, **kwargs)
                argdict[key] = res
                return res
        return wrapper
