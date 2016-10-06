"""
Exercise — context manager to check an exception was raised

This example comes from unit testing. We want to make sure that
we raise the right exceptions on errors.

Write a cm 'assert_raises' that
① checks that an exception *was* raised
② checks that the exception is of the right type

>>> with assert_raises(ZeroDivisionError):
...     1 / 0

>>> with assert_raises(ZeroDivisionError):
...     0[0] / 0
Traceback (most recent call last):
  ...
AssertionError: expected ZeroDivisionError not AttributeError

>>> with assert_raises(ZeroDivisionError):
...     0 / 1
Traceback (most recent call last):
  ...
AssertionError: expected ZeroDivisionError exception
"""

def assert_raises(exception_type):
    ...
