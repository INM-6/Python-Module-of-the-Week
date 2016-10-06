"""
Exercise — wrapping a function to do something on every invocation

Write a decorator which prints the arguments
and the return value of the wrapped function.

>>> @logger
>>> def f(x, y):
...     return g(x) + g(y)

>>> @logger
>>> def g(x):
...     return 2 * x

>>> f(5, 6)
f is called with args [5, 6] kwargs {}
g is called with args [5] kwargs {}
g returns 10
g is called with args [6] kwargs {}
g returns 12
f returns 22
"""

def logger(f):
    ...
