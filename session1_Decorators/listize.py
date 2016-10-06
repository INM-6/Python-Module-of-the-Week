"""
Exercise: listize decorator

When a function returns a list of results, we might need
to gather those results in a list:

def lucky_numbers(n):
    ans = []
    for i in range(n):
        if i % 7 != 0:
            continue
        if sum(int(digit) for digit in str(i)) % 3 != 0:
            continue
        ans.append(i)
    return ans

This looks much nicer when written as a generator.

① Convert lucky_numbers to be a generator.

② Write a 'listize' decorator which gathers th results from a
generator and returns a list and use it to wrap the new lucky_numbers().

Subexercise: ③ Write an 'arrayize' decorator which returns the results
in a numpy array instead of a list.

>>> @listize
... def f():
...     yield 1
...     yield 2
>>> f()
[1, 2]
"""

def listize():
    ...
