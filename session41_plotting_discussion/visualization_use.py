
"""
figure skeleton using the rcParams from visualization.py 
"""

import matplotlib.pyplot as plt
from matplotlib import gridspec
import visualization as vis


figpath = 'figures/'
filename = 'fig99'



### prepare figure skeleton with two rows,
### 3 equal panels in the first row and two panels in the second, of which the first consists of 8 small panels.

visualization = vis.visualization()
fig = plt.figure(figsize=(5.5, 4.)) #1.375
plt.clf()

widths = [1, 1, 1 , 1, 1, 1]
heights =[1, 1, 1, 1]
gs = gridspec.GridSpec(nrows=4, ncols=6, width_ratios=widths, height_ratios=heights, figure=fig)

axA = fig.add_subplot(gs[:2,:2])
axA.set_title(r'\textbf{a}',loc='left')

axB = fig.add_subplot(gs[:2,2:4])
axB.set_title(r'\textbf{b}',loc='left')

axC = fig.add_subplot(gs[:2,4:])
axC.set_title(r'\textbf{c}',loc='left')

axD1 = fig.add_subplot(gs[2,0])
axD1.set_title(r'\textbf{d}',loc='left')
axD2 = fig.add_subplot(gs[2,1])
axD3 = fig.add_subplot(gs[2,2])
axD4 = fig.add_subplot(gs[2,3])
axD5 = fig.add_subplot(gs[3,0])
axD6 = fig.add_subplot(gs[3,1])
axD7 = fig.add_subplot(gs[3,2])
axD8 = fig.add_subplot(gs[3,3])

axE = fig.add_subplot(gs[2:,4:])
axE.set_title(r'\textbf{e}',loc='left')


## render and save figure

plt.tight_layout()
#pl.savefig(figpath + filename +'.svg')
plt.show()