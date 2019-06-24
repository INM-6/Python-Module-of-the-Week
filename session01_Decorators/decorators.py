"""
Decorators
"""

# 1 Decorators##################################################################
# Have a look at the warnings examples in warnings.py. How would you
# go about writing a more general deprectation warning if you have
# multiple deprecated functions? Wouldn't it be nice to 'decorate' a function
# as 'deprecated' instead of explicitely raising a warning each time?

# One solution would be a wrapper function, which you apply to your
# deprecated functions, eg

def wrapper(old_function):
    print 'do something before'
    result = old_function()
    print 'doing something after'
    return result


def deprecated(old_function):
    print 'A'
    def wrapper():
        print 'deprecated'
        res = old_function()

        return res

    print 'C'
    return wrapper


@deprecated
def myfunction():
    print 'Myfunction'

print 'Calling wrapper explicitely'
wrapper(myfunction)

print 'Calling myfunction'
myfunction()

print myfunction





# -1 Predefined Decorators #####################################################

# Decorators to be used with methods in classes:
# @staticmethod, @classmethod, @abc.abstractmethod, @context.contextmanager


# Example code for @classmethod and @abc.abstractmethod
import abc

class BasePizza(object):
    __metaclass__  = abc.ABCMeta

    default_ingredients = ['cheese']

    @classmethod
    @abc.abstractmethod
    def get_ingredients(cls):
         """Returns the ingredient list."""
         return cls.default_ingredients

class DietPizza(BasePizza):
    def get_ingredients(self):
        return ['egg'] + super(DietPizza, self).get_ingredients()

