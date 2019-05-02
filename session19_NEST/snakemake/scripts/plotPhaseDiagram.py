import os
import argparse
import numpy as np
import matplotlib.pyplot as plt


# parse command line parameters
parser = argparse.ArgumentParser(description='Plot phase diagram.')
parser.add_argument('spikefiles', type=str, nargs='+', help='input files')
parser.add_argument('plotfile', type=str, help='output file')
args = parser.parse_args()


# calculate CV for all simulation
g_list = []
nu_ex_list = []
CV_list = []
for sf in args.spikefiles:
    # extract name of the file
    fn = os.path.splitext(os.path.basename(sf))[0]

    # extract parameters from filename
    g_list.append(float(fn.split('_')[1]))
    nu_ex_list.append(float(fn.split('_')[2]))

    # load the spike file
    ids, times = np.load(sf)
    ids = ids.astype(np.int)

    # calculate CV for current neuron
    CV = 0.
    unique_ids = set(ids)
    if len(unique_ids) > 0:
        for id in unique_ids:
            ISIs = np.diff(times[ids == id])
            if len(ISIs) > 1:
                CV += np.std(ISIs) / np.mean(ISIs)
        CV /= len(unique_ids)
    CV_list.append(CV)


# make scatter plot, CV indicated by color
plt.scatter(g_list, nu_ex_list, c=CV_list, marker='s', s=500, vmin=0, vmax=1)
# set axis range and label
plt.xlim(0, 8)
plt.xlabel('$g$')
plt.ylim(0, 4)
plt.ylabel('$\\nu_{ext}/\\nu_{thr}$')
# add colorbar and title
plt.colorbar()
plt.title('Coefficient of Variation')
plt.savefig(args.plotfile)
