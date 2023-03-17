
verbose = False   # verbose flag

g2 = 1.4       # g_a^2
g_in2 = 1.0    # g_in^2

#sigma2 = 0.1   # sigma^2
sigma2 = 0.05   # sigma^2

n = 100        # width of layers

#A = 7
A = 3          # number of layers

D = 12
#D = 6          # number of data points (must be even)
seed_train_data = 481
seed_test_data = 379

N_in = 100     # dimension of input vector

task = 'ising'        # either xor or ising task
delta_p = 0.2  # shift of probability of entries in Ising vectors
sigma_xor = 0.3   # signal to noise ratio in xor task, feature learning approximation breaks down small values

if task == 'xor':
    task_param = sigma_xor
elif task == 'ising':
    task_param = delta_p
else:
    raise ValueError("Task must be either xor or ising.")


Nsamples = 100 # number of samples to draw for approximating integrals

#num_iter = 1 # number of iterations of
num_iter = 3   # number of iterations of


N_test = 8    # number of test points


eps = 0.0      # ridge parameter (variance of readout noise)
kappa = 0.05    # regularization parameter = weight decay factor

# all nu = 1 here, so all layers have same width


data_dir = 'data/'
suffix = task + '_task_param_' + str(task_param) + '_A=' + str(A) + 'D=' + str(D)  + 'g2=' + str(g2) + 'sigma2=' + str(sigma2) + 'kappa' + str(kappa)
dataname = 'feature_mft'
save_path = data_dir + suffix + '/'
