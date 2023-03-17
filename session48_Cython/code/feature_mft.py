

import numpy as np
import matplotlib.pylab as pl
import scipy.integrate as sciint
import scipy.optimize as opt

# TODO possibly remove this?
from parameters import *


def phi(x):
    return np.tanh(x)

def phi_prime(x):
    return 1./np.cosh(x)**2

def phi_pprime(x):
    return -2.*np.tanh(x)/np.cosh(x)**2


def E_phi_phi(C, tilC):

    #print("C=", C)

    def integrand_num(x):
        p_x = np.exp(-x**2/(2.*C) + 1./2.*tilC*phi(x)**2)
        return p_x * phi(x)**2

    def integrand_denom(x):
        p_x = np.exp(-x**2/(2.*C) + 1./2.*tilC*phi(x)**2)
        return p_x


    num, err = sciint.quad(integrand_num, -10, 10)
    denom, err = sciint.quad(integrand_denom, -10, 10)

    #print('num = ', num)
    #print('denom = ', denom)

    return num / denom


def p_x(x, q, qt):
    return np.exp(-x**2/(2.*q) + 1./2.*qt*phi(x)**2)



def exp_pair(f, g, C, alpha, beta):
    """ compute <f(h_alpha) g(h_beta)>_h~N(0,C) """


    if alpha == beta:

        range1 = np.sqrt(C[alpha,alpha])

        def integrand_diag(z):
            x = z * range1
            return f(x) * g(x) * np.exp(-z**2/2.)

        I, err = sciint.quad(integrand_diag, -range1*5.0, range1*5.0)

        return I / np.sqrt(2.*np.pi)


    else: # alpha != beta

        K = np.array([ [ C[alpha,alpha], C[alpha,beta]], [ C[beta,alpha], C[beta,beta] ] ] )

        #print("K =", K)

        lam, v = np.linalg.eig(K)

        #print("alpha=", alpha, "beta=", beta, "lambdas = ", lam)


        for i, l in enumerate(lam):
            if l < 0.0:
                if np.abs(l) > 1e-12:
                    print("error: negative lambdas!")
                    print("indices = ", alpha, beta)
                    print("K = ", K)
                    print("lambdas = ", lam)
                    lam[i] = 0.0

        ranges = np.sqrt(lam)

        def integrand(z_1, z_2):
            z = np.array([z_1, z_2])

            #x_1 = z_1 * range1 * v[0, 0] + z_2 * range2 * v[0, 1]
            #x_2 = z_1 * range1 * v[1, 0] + z_2 * range2 * v[1, 1]
            #return f(x_1) * g(x_2) * np.exp(-z_1**2/2. - z_2**2/2.)
            x = np.dot(v, z*ranges)
            return f(x[0]) * g(x[1]) * np.exp(-z_1**2/2. - z_2**2/2.)



        def int1(z_2):
            I, err = sciint.quad(lambda z_1: integrand(z_1, z_2), -ranges[0]*5.0, ranges[0]*5.0)
            return I

        I, err = sciint.quad(int1, -ranges[1]*5.0, ranges[1]*5.0)

        return I / (2.*np.pi)



def exp_quadruple(f, g, u, w, C, indices, Nsamples):
    """ compute forth moment """

    K = np.zeros((4,4), dtype=float)

    for i in range(4):
        for j in range(4):
            K[i,j] = C[indices[i], indices[j]]

    #print("indices = ", indices)

    lam, v = np.linalg.eig(K)

    for i, l in enumerate(lam):
        if l < 0.0:
            if np.abs(l) > 1e-12:
                print("error: negative lambdas!")
                print("indices = ", indices)
                print("K = ", K)
                print("lambdas = ", lam)
                exit()
            lam[i] = 0.0

    #print("lambdas =", lam)


    ranges = np.sqrt(lam)


    def integrand(z):
        x = np.dot(v, z*ranges)

        return f(x[0]) * g(x[1]) * u(x[2]) * w(x[3])


    I = 0.0
    for s in range(Nsamples):
        z = np.random.normal(size=4)
        I += integrand(z)


    return I/Nsamples



def iterate_C_pureMFT(C_a, alpha, beta):

    # zeroth order
    C_a1_0 = g2 * exp_pair(phi, phi, C_a, alpha, beta) + sigma2

    return C_a1_0



def iterate_C(C_a, til_Ca1, exp_pair, alpha, beta):

    # zeroth order
    C_a1_0 = g2 * exp_pair[alpha, beta] + sigma2

    # compute correction matrix (second term in Eq:12)
    #print("computing correction")

    assert(til_Ca1.shape[0] == til_Ca1.shape[1])

    corrC = 0.0

    for gamma in range(til_Ca1.shape[0]):
        corrC += til_Ca1[gamma, gamma] * ( exp_quadruple(phi, phi, phi, phi, C_a, np.array([alpha, beta, gamma, gamma]), Nsamples)\
                                           - exp_pair[alpha,beta] * exp_pair[gamma,gamma] )

        for delta in range(gamma+1, til_Ca1.shape[0]):
            corrC += (til_Ca1[gamma, delta] + til_Ca1[delta, gamma]) * ( exp_quadruple(phi, phi, phi, phi, C_a, np.array([alpha, beta, gamma, delta]), Nsamples)\
                                                                         - exp_pair[alpha,beta] * exp_pair[gamma,delta] )

    #print ("done, corrC = ", corrC)

    # first order
    C_a1_1 = g2**2 * corrC

    return C_a1_0 + C_a1_1



def final_tilC(C_A1, Y):
    """determine value of \tilde{C^(A+1)} for final layer"""

    C_inv = np.linalg.inv(C_A1)

    Y_outer = np.outer(Y, Y)

    tilC = -1./(2.*n) * ( C_inv - np.matmul( C_inv, np.matmul(Y_outer, C_inv) ) )

    #print("tilde C^(A+1) = ", tilC)

    return tilC


def iterate_tilC_back(tilC_A1, C, verbose):

    tilC = np.zeros( (tilC_A1.shape[0], tilC_A1.shape[1], A+1), dtype = float )
    tilC[:,:, A] = tilC_A1

    if verbose:
        print("iterating tilde C backwards")

    for a in range(A-1, -1, -1):
        if verbose:
            print("layer a=", a)
        for alpha in range(D):
            tilC[alpha, alpha, a] = g2 * tilC[alpha, alpha, a+1] * ( exp_pair(phi, phi_pprime, C[:,:,a], alpha, alpha) + exp_pair(phi_prime, phi_prime, C[:,:,a], alpha, alpha) )
            for beta in range(alpha):
                tilC_alpha_beta = g2 * tilC[alpha, beta, a+1] * exp_pair(phi_prime, phi_prime, C[:,:,a], alpha, beta)
                tilC[alpha, beta, a] = tilC_alpha_beta
                tilC[beta, alpha, a] = tilC_alpha_beta

    return tilC


def generate_training_data(n_samples, data_dim, task, task_param, seed_data):
    """generate training data for different tasks"""
    if task == 'xor':
        X, Y = generate_training_data_xor(n_samples, data_dim, task_param, seed_data)
    elif task == 'ising':
        X, Y = generate_training_data_ising(n_samples, data_dim, task_param, seed_data)
    else:
        raise ValueError("Task must be either xor or ising.")
    return X, Y

def generate_training_data_ising(D, N, delta_p, seed_data):
    """random Ising vectors with random labels assigned"""

    X1 = 2*(np.random.rand(int(D/2), N) > 0.5 + delta_p) - 1.0
    X2 = 2*(np.random.rand(int(D/2), N) > 0.5 - delta_p) - 1.0

    # setting of binary classification
    # labels +-1 for the two classes, examples presented
    # sorted by labels
    X = np.vstack ( (X1, X2) )
    Y = np.hstack ( (np.ones(int(D/2)), -np.ones(int(D/2))) )

    return X, Y


def generate_training_data_xor(D, data_dim, sigma, seed_data):
    """
    Random samples drawn from a high-dimensional XOR task.
    See http://proceedings.mlr.press/v139/refinetti21b/refinetti21b.pdf.
    """
    rng = np.random.default_rng(seed_data)
    means = np.eye(data_dim)[:2]
    cov = sigma**2 * np.eye(data_dim)

    X1 = rng.multivariate_normal(mean=means[0], cov=cov, size=int(D/4))
    X2 = rng.multivariate_normal(mean=-means[0], cov=cov, size=int(D/4))
    X3 = rng.multivariate_normal(mean=means[1], cov=cov, size=int(D/4))
    X4 = rng.multivariate_normal(mean=-means[1], cov=cov, size=int(D/4))

    X = np.vstack ( (X1, X2, X3, X4) )
    Y = np.hstack ( (np.ones(int(D/2)), -np.ones(int(D/2))) )


    return X, Y


def compute_overlap(X):
    return g_in2 * np.dot(X, X.T) / N_in


def compute_overlap2(X1, X2):
    return g_in2 * np.dot(X1, X2.T) / N_in


def initial_mft(C0, Y, verbose):

    C_mft = np.zeros( (D,D,A+1), dtype=float)

    C_mft[:,:,0] = C0

    if verbose:
        print("computing pure MFT as starting point...")

    # first compute the pure MFT without corrections in the first pass
    for a in range(A):
        if verbose:
            print("layer a = ", a)
        for alpha in range(D):
            for beta in range(alpha+1):
                C_alpha_beta = iterate_C_pureMFT(C_mft[:,:,a], alpha, beta)
                C_mft[alpha, beta, a+1] = C_alpha_beta
                C_mft[beta, alpha, a+1] = C_alpha_beta
            C_mft[alpha, alpha, a+1] += kappa
    if verbose:
        print("[done]")
    return C_mft


def correctionC(C, tilC, range_alpha=None):

    if range_alpha is None:
        range_alpha = range(C.shape[0])

    exp_phi_phi = np.zeros( (C.shape[0], C.shape[1], C.shape[2]-1), dtype=float)

    assert(C.shape[0] == C.shape[1])

    #print("shape(C)", C.shape)
    #print("shape(tilC)", tilC.shape)

    for a in range(0, C.shape[2]-1):
        # print("layer a = ", a)

        # first compute <phi phi> for next layer for all alpha, beta
        for alpha in range_alpha:
            for beta in range(alpha+1):
                C_alpha_beta = exp_pair(phi, phi, C[:,:,a], alpha, beta)

                exp_phi_phi[alpha, beta, a] = C_alpha_beta
                exp_phi_phi[beta, alpha, a] = C_alpha_beta

        # compute correction
        for alpha in range_alpha:
            for beta in range(alpha+1):
                C_alpha_beta = iterate_C(C[:,:,a], tilC[:,:,a+1], exp_phi_phi[:,:,a], alpha, beta)
                C[alpha, beta, a+1] = C_alpha_beta
                C[beta, alpha, a+1] = C_alpha_beta
        C[:,:,a+1] += kappa * np.eye(C.shape[0])
    return C, exp_phi_phi



def iterate_stats(C0, Y, num_iter, verbose=False):
    """one iteration of the statistics"""

    # obtain MFT solution as initial value
    C = initial_mft(C0, Y, verbose)
    C_mft = C.copy()

    last_tilC = np.zeros((C.shape[0], C.shape[1]), dtype=float)

    for r in range(num_iter):
        if verbose:
            print("iteration #", r)

        # obtain value of tilde C in final layer
        tilC_A1 = final_tilC(C[:, :, A], Y)

        if verbose:
            print("tilC in final layer =", tilC_A1)
            print("size of change of tilde C^(A+1)", np.mean(np.abs(tilC_A1 - last_tilC).flatten()))

        last_tilC = tilC_A1.copy()

        # iterate tilde C backwards through layers
        tilC = iterate_tilC_back(tilC_A1, C, verbose)

        #print("tilC in initial layer =", tilC[:,:,0])
        if verbose:
            print("computing corrections...")

        # compute correction to current C

        C, exp_phi_phi = correctionC(C, tilC)
        if verbose:
            print("[done]")

    return C_mft, C, tilC, exp_phi_phi



def test_stats(C_train, tilC, exp_phi_phi, x_star, X, verbose):
    """approximate the statistics of the output for a test point
       by neglecting all effects of the test point on the training range;
       C, and \tilde{C} are hence computed only for all training points"""

    # compute missing values for C for test point

    exp_phi_phi_star = np.zeros((D+1, D+1, A), dtype=float)
    exp_phi_phi_star[:D, :D, :] = exp_phi_phi

    C_star = np.zeros( (D+1, D+1, A+1), dtype=float)
    C_star[:D, :D, :] = C_train

    tilC_star = np.zeros( (D+1, D+1, A+1), dtype=float)
    tilC_star[:D, :D, :] = tilC

    # overlap of test point with all other points
    C0_star = compute_overlap2(X, x_star)

    # insert as last row and column in layer 0
    C_star[D, :D, 0] = C0_star
    C_star[:D, D, 0] = C0_star
    C_star[D, D, 0] = compute_overlap(x_star)

    #print("C_star[a=0] = ", C_star[:,:,0])

    for r in range(2):

        C_inv = np.linalg.inv(C_star[:D, :D, A])

        if r > 0:
            tilG = C_star[:D, D, A] / ( np.dot(C_star[D,:D, A], np.dot(C_inv, C_star[:D, D, A])) - C_star[D, D, A] )

            if verbose:
                print("tilG = ", tilG)

            tilC_star[D, :D, A] = np.dot( tilC[:, :, A], tilG )
            tilC_star[D, D, A] = np.dot( tilG, np.dot(tilC[:, :, A], tilG) )

            tilC_star = iterate_tilC_back(tilC_star[:, :, A], C_star, verbose)

        #print("tilC in initial layer =", tilC[:,:,0])
        if verbose:
            print("computing corrections...")

        # compute correction to current C

        C_star, exp_phi_phi_star = correctionC(C_star, tilC_star, [D])

    if verbose:
        print("C_star[a=A] = ", C_star[:,:,A])

    return C_star, tilC_star



def test_stats_mft(C_mft, x_star, X, verbose):
    """approximate the statistics of the output for a test point
       by neglecting all effects of the test point on the training range;
       C, and \tilde{C} are hence computed only for all training points"""

    # compute missing values for C for test point

    C_star = np.zeros( (D+1, D+1, A+1), dtype=float)
    C_star[:D, :D, :] = C_mft

    # overlap of test point with all other points
    C0_star = compute_overlap2(X, x_star)

    # insert as last row and column in layer 0
    C_star[D, :D, 0] = C0_star
    C_star[:D, D, 0] = C0_star
    C_star[D, D, 0] = compute_overlap(x_star)

    #print("C_star[a=0] = ", C_star[:,:,0])

    if verbose:
        print("computing mean-field iteration")

    for a in range(0, A):
        if verbose:
            print("layer a = ", a)

        # first compute <phi phi> for next layer for all alpha, beta
        for alpha in range(D+1):
            C_alpha_star = g2 * exp_pair(phi, phi, C_star[:,:,a], alpha, D) + sigma2
            C_star[alpha, D, a+1] = C_alpha_star
            C_star[D, alpha, a+1] = C_alpha_star
    if verbose:
        print("C_star[a=A] = ", C_star[:,:,A])

    return C_star




def mu_sigma2_pred(C, C_star, C_star_star, Y, eps):
    """
    Compute the mean of the predictive distribution assuming only Gaussian statistics
    described by the kernel
    C: overlaps of all training points
    C_star: last row containing overlaps with all training data points and test point
    Y: training labels
    eps: regularizer (readout noise)
    """

    C_inv = np.linalg.inv(C + eps*np.eye(D))

    mu_pred = np.dot(C_star, np.dot(C_inv, Y))

    sigma2_pred = C_star_star - np.dot(C_star, np.dot(C_inv, C_star.T))

    return mu_pred, sigma2_pred
