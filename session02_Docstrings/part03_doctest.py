#!/usr/bin/env python3
# encoding: utf8

import doctest

def funcA(a):
    '''
    func(num) -> qsrh

    returns the quadruplesquareroothalf of num. Use for example like
    >>> funcA(10)
    3.1622776601683795

    or probably even like
    >>> funcA(15) + 42
    45.87298334620742
    '''
    return a



def funcB(b):
    '''
    func(qsrh) -> num

    returns the de-quadruplesquareroothalfed result.

    <write nice doc-test here>
    >>> True
    '''
    val = 2*funcA(b)
    return (val*val)/4.
