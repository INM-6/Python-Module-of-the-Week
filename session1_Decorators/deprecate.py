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
