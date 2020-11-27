"""

Simple functions
----------------

Header 3
~~~~~~~~

.. autosummary::
    :toctree: toctree/utils

    add
    multiply


Weird functions
---------------

.. autosummary::
    :toctree: toctree/utils

    jump

"""

import torch


def add(x, y):
    """
    Adds x and y.

    Parameters
    ----------
    x, y: torch.Tensor

    Returns
    -------
    torch.Tensor

    """
    return x + y


def jump(x, y):
    """
    Blah blah

    Parameters
    ----------
    x, y: torch.Tensor

    Returns
    -------
    torch.Tensor

    """
    return x + y


def multiply(x, y):
    """
    Multiplies ``x`` by `y`.

    Parameters
    ----------
    x, y: torch.Tensor

    Returns
    -------
    torch.Tensor

    """
    return x + y
