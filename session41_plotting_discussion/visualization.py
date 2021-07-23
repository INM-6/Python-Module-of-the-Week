'''
This script defines colors and rcParams for matplotlib.pyplot .
It is imported by the figure generation scripts to set the general style of the plots.
'''

import matplotlib.pyplot as plt



# define some gray levels
black = (0.0,0.0,0.0)
darkgray = (0.25, 0.25, 0.25)
midgray = (0.5, 0.5, 0.5)
lightgray = (0.75, 0.75, 0.75)
white = (1.0, 1.0, 1.0)

# define some red levels
darkred = (0.3, 0., 0.)
midred = (0.5, 0., 0.)
lightred = (0.7, 0., 0.)
red = (1., 0., 0.)

# INM colors 
myblue = (0., 64./255., 192./255.)
myred = (192./255., 64./255., 0.)
mygreen = (0., 192./255., 64./255.)
myorange = (0.5, 0.25, 0.25)
mypink = (0.75, 0.25, 0.75)
myblue2 = (0., 128./255., 192./255.)
myred2 = (245./255., 157./255., 115./255.)

# coolers colors
myred_hex =   '#931621'
myyellow_hex ='#B67431'
myblue1_hex = '#2B4162'
myblue2_hex = '#2C8C99'
mygreen_hex = '#0B6E4F'

# Sanzo Wanda's collection 264
sw_pink = '#ffa6d9'
sw_red = '#e81900'
sw_light_green = '#b3d9a3'
sw_dark_green = '#29bdad'

# Okabe and Ito's colorblind-friendly palette
oi_black = (0., 0., 0.)
oi_orange = (230./255, 159./255, 0.)
oi_light_blue = (86./255, 180./255, 233./255)
oi_green = (0., 158./255, 115./255)
oi_yellow = (240./255, 228./255, 66./255)
oi_blue = (0., 114./255, 178./255)
oi_dark_orange = (213./255, 94./255, 0.)
oi_purple = (204./255, 121./255, 167./255)


# custom densely dashed linestyle
densely_dashed = (0, (5, 1))


#panel_wh_ratio = (1. + np.sqrt(5)) / 2. # golden ratio

class visualization():

    def __init__(self):
        '''
        Initialize an instance of this class to set the pyplot rcParams.
        '''
        # figure dims
        self.SCIwidth = 5.5  # in inches
        self.SCIheight2row= 5.5  
        self.SCIheight1row= 2.75 
        #self.inchpercm = 2.54
    
        width = self.SCIwidth
        height = self.SCIheight2row # width / panel_wh_ratio

        scale = 1.2

        plt.rcParams['figure.figsize'] = (width, height)

        # resolution of figures in dpi
        # does not influence eps output
        plt.rcParams['figure.dpi'] = 600

        # font
        plt.rcParams['font.size'] = scale*8
        plt.rcParams['axes.titlesize'] = scale*8
        plt.rcParams['legend.fontsize'] = scale*6
        plt.rcParams['font.family'] = "helvetica"

        plt.rcParams['lines.linewidth'] = scale*1.0

        # size of markers (points in point plots)
        plt.rcParams['lines.markersize'] = scale * 1. #2.5
        plt.rcParams['patch.linewidth'] = scale * 1.0
        plt.rcParams['axes.linewidth'] = scale * 0.2     # edge linewidth

        # ticks distances
        plt.rcParams['xtick.major.size'] = scale * 1.5      # major tick size in points
        plt.rcParams['xtick.minor.size'] = scale * 1.5      # minor tick size in points
        plt.rcParams['lines.markeredgewidth'] = scale * 0.5  # line width of ticks
        plt.rcParams['grid.linewidth'] = scale * 0.5
        plt.rcParams['xtick.major.pad'] = scale * 2      # distance to major tick label in points
        plt.rcParams['xtick.minor.pad'] = scale * 2      # distance to the minor tick label in points
        plt.rcParams['ytick.major.size'] = scale * 1.5      # major tick size in points
        plt.rcParams['ytick.minor.size'] = scale * 1.5      # minor tick size in points
        plt.rcParams['ytick.major.width'] = scale * 0.2      # major tick size in points
        plt.rcParams['ytick.minor.width'] = scale * 0.2      # minor tick size in points
        plt.rcParams['xtick.major.width'] = scale * 0.2      # major tick size in points
        plt.rcParams['xtick.minor.width'] = scale * 0.2      # minor tick size in points
        plt.rcParams['ytick.major.pad'] = scale * 2      # distance to major tick label in points
        plt.rcParams['ytick.minor.pad'] = scale * 2      # distance to the minor tick label in points

        # ticks textsize
        plt.rcParams['ytick.labelsize'] = scale * 8
        plt.rcParams['xtick.labelsize'] = scale * 8

        # use latex to generate the labels in plots
        # not needed anymore in newer versions
        # using this, font detection fails on adobe illustrator 2010-07-20 
        plt.rcParams['text.usetex'] = True
        plt.rcParams['ps.useafm'] = False   # use of afm fonts, results in small files
        plt.rcParams['ps.fonttype'] = 3    # Output Type 3 (Type3) or Type 42 (TrueType)
  

    ##################
    ### DIMENSIONS ###
    ##################

    def set_SCI_1row_fig_style(self): #, ratio=panel_wh_ratio):
        '''figure size corresponding to one row of usually 3 panels'''
        plt.rcParams.update({
            'figure.figsize' : [self.SCIwidth,self.SCIheight1row],
        })


    def set_SCI_2row_fig_style(self):
        '''figure size corresponding to two rows of usually 3 panels'''
        plt.rcParams.update({
            'figure.figsize' : [self.SCIwidth,self.SCIheight2row],
        })
        
        


    ############
    ### MISC ###
    ############
    
    
    def remove_ticks(ax):
        ''' small function to remove all ticks from a panel '''
        ax.set_yticks([])
        ax.set_xticks([])


    def remove_axis_junk(self, ax, which=['right', 'top']):
        '''remove upper and right axis'''
        # for loc, spine in ax.spines.iteritems():
        #     if loc in which:
        #         spine.set_color('none')                          
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
    
    def make_axis_cross(self,ax):
        # Move left y-axis and bottim x-axis to centre, passing through (0,0)
        ax.spines['left'].set_position('center')
        #ax.spines['bottom'].set_position('center')
        
        # Eliminate upper and right axes
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')

        # Show ticks in the left and lower axes only
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        return ax

    def legend(self, ax, on=True, loc=1):
        plt.sca(ax)
        if on:
            plt.legend(loc=loc)
        return ax

    def title(self, ax, title='', verticalalignment='top'):
        plt.sca(ax)
        plt.suptitle(title)
        return ax
  
