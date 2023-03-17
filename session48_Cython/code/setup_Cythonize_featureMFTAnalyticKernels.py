

import numpy as np
import matplotlib.pylab as pl
import scipy.integrate as sciint
import scipy.optimize as opt




from distutils.core import setup
from Cython.Build import cythonize
import timeit as timeit

setup(ext_modules=cythonize("feature_mft_analyticKernels.pyx"),include_dirs=[np.get_include()])
