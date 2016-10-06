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

def factorial(n):
    "This function can be used for testing…"
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

...
