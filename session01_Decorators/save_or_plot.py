# -*- coding: utf-8 -*-
"""
Exercise: matplotlib!

Write a context manager which gives you a matplotlib figure object,
and either saves the plot to a file or pops it up on screen,
depending on a *global* parameter SAVEFIGS (in a real program
this parameter would be settable by a commandline options).

with save_or_plot('name') as f:
    f.plot([0, 3, 2, 5])
"""

import sys
import contextlib
from matplotlib import pyplot

SAVEFIGS = sys.argv[1:2] == ['--save']

@contextlib.contextmanager
def save_or_plot(name):
    f = pyplot.figure()
    if not SAVEFIGS:
        f.canvas.set_window_title(name)
    yield f
    if SAVEFIGS:
        f.savefig(name + '.svg')
    else:
        f.show()
