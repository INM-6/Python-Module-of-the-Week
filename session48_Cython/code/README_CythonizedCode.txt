README - How to run cythonized code:

In order to increase the performance of the code we decided to implement some
changes in the code:


1.) The pairwise correlations in feature_mft_analyticKernels are evaluated for the erf- activation function.
    This is done by using analytic expression which one can indeed obtain for erf-activations.
2.) The quadruple method has been cythonized in order to speed up the run-time of the program.
    Further the evaluation of eigenvectors and eigenvalues is done with the scipy LAPACK API

In order to use cythonized code, the file needs the suffix ".pyx"
After this, one runs the "setup_Cythonize_featureMFTAnalyticKernels.py" script with the terminal command

python3.8 setup_Cythonize_featureMFTAnalyticKernels.py build_ext --inplace


After doing this, one can simply run the program "RunProfiling_CythonizedKernelEvaluation.py"
using the terminal command:
python3.8 RunProfiling_CythonizedKernelEvaluation.py


What needs to be installed for the code to work:

numpy
scipy
cProfile
Cython
timeit

What needs to be in the same folder to run "RunProfiling_CythonizedKernelEvaluation":
Most recent versions of:
	utils_analysis.py
	parameters.py
