import numpy as np
import matplotlib.pylab as pl
from matplotlib import gridspec
import scipy.integrate as sciint
import scipy.optimize as opt

from parameters import *

import feature_mft as feature_mft
import feature_mft_analyticKernels as fmft_anayltic
# from utils_analysis import *
import cProfile as cProfile
import pstats as pstats
import time as time

# import line_profiler as line_profiler
import cython as cython
from Cython.Build import cythonize


#Run profiling and compare the efficiency of the convetional feature_mft modules
#and the feature_mft_analyticKernels modules which uses analytic kernels, Cython and LAPACK

task='ising'
num_iter=1
for i, delta_p in enumerate([0.2]):
    X, Y = fmft_anayltic.generate_training_data(D, N_in, task, delta_p)
    C0 = fmft_anayltic.compute_overlap(X)
    pr = cProfile.Profile()
    pr.enable()
    C_mft,C,tilC,exp_phi_phi=fmft_anayltic.iterate_stats(C0,Y,num_iter)
    pr.disable()
    stats = pstats.Stats(pr).sort_stats('cumulative')
    stats.print_stats(20)

    # pr.enable()
    # C_mft,C,tilC,exp_phi_phi=feature_mft.iterate_stats(C0,Y,num_iter)
    # pr.disable()
    # stats = pstats.Stats(pr).sort_stats('cumulative')
    # stats.print_stats(20)


