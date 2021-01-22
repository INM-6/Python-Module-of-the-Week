# Iterators
An iterator is an object representing a stream of data.
It returns data one element at a time.
Functionallity is defined by the __next__() function:
- must not take an argument
- returns the next element of the stream
- if there are no objects in the stream left raise StopIteration exception

[example 1](./1_iterators_next.py)

writing this is of course unwieldy which is why we are lucky to have the built-in iter() function.
iter()  takes an arbitrary object and tries to return an iterator that will return the object’s contents or elements.
Raises TypeError if the object doesn’t support iteration.

An object is called iterable if you can get an iterator for it.

Python expects iterable objects in several locations.
Most notably in the for statement.
In the statement for X in Y, Y must be an iterator or some object for which iter() can create an iterator.

[example 2](./2_iterators_iter.py)

Iterators automatically implement a lot of nice features:
They can be materialized as lists and tuples by passing it to the constructor functions.
Even sequence unpacking, max(), min(), ...

[example 3](./3_iterator_features.py)



# Generator Expressions
two common uses for iterators are:
1. performing some operation on every element of an iterable
2. selecting some subset of elements

To make these operations even easier and more concise python stole Generator Expression (and List Comprehensions) from Haskell

[example 4](./4_generator_expressions.py)


the general form for this is:
( expression for expr in sequence1
             if condition1
             for expr2 in sequence2
             if condition2
             for expr3 in sequence3 ...
             if condition3
             for exprN in sequenceN
             if conditionN )

A nice thing about these expressions is that they can be directly passed to other objects or functions.
When doing so one can leave out the surrounding parantheses, which is basically what is happening when using List Comprehensions.

[example 5](./5_expressions_without_parentheses.py)

# Generators

Generators are a special class of functions that simplify the task of writing iterators.
Regular functions compute a value and return it, but generators return an iterator that returns a stream of values.

The defining statement of a generator is yield.
It works similar to return.
The big difference is that on reaching a yield the generator’s state of execution is suspended and local variables are preserved.
On the next call to the generator’s __next__() method, the function will resume executing.

[example 6](./6_simple_generator.py)

"Recently" a few additions have been made to the syntax of Generators.
First of all "yield from" (added with python 3.3) allows to delegate to another generator.

[example 7](7_yield_from.py)

Secondly it is possible to send information to a generator via send

[example 8](./8_send.py)

So to finish:

[example 9](./9_sudoku_solver.py)
