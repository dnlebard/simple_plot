get_ipython().magic('matplotlib inline')

import matplotlib.pyplot as plt
import numpy as np
import os

def simple_plot(x_col, *y_cols, **kwargs):
    """
    """
    
    # modify the axis labels if necessary
    if 'x_label' in kwargs:
        plt.xlabel(kwargs['x_label'], fontsize=16)
    
    if 'y_label' in kwargs:
        plt.ylabel(kwargs['y_label'], fontsize=16)

    # loop over all columns and plot them in the same plot
    for y_col in y_cols:        
        plt.plot(x_col,y_col)
        
    # setup the plot range
    axes = plt.gca()
    ymin_orig, ymax_orig = axes.get_ylim()
    xmin_orig, xmax_orig = axes.get_xlim()
                
    if 'x_min' in kwargs:
        x_min = float(kwargs['x_min'])
    else:
        x_min = xmin_orig
    
    if 'x_max' in kwargs:
        x_max = float(kwargs['x_max'])
    else:
        x_max = xmax_orig

    if 'y_min' in kwargs:
        y_min = float(kwargs['y_min'])
    else:
        y_min = ymin_orig
    
    if 'y_max' in kwargs:
        y_max = float(kwargs['y_max'])
    else:
        y_max = ymax_orig
        
    axes.set_xlim([x_min,x_max])
    axes.set_ylim([y_min,y_max])
        
    plt.show()