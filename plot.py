get_ipython().magic('matplotlib inline')

import matplotlib.pyplot as plt
import numpy as np
import os

from matplotlib.ticker import ScalarFormatter


def simple_plot(x_col, *y_cols, **kwargs):
    """
    """
    
    if 'fig_size' in kwargs:
        fig= plt.figure(figsize=kwargs['fig_size'])

    # modify the axis labels if necessary
    if 'x_label' in kwargs:
        plt.xlabel(kwargs['x_label'], fontsize=20)
    
    if 'y_label' in kwargs:
        plt.ylabel(kwargs['y_label'], fontsize=20)

    has_labels = True if 'labels' in kwargs else False
    label_data = kwargs['labels'] if has_labels else [None]*len(y_cols)
    
    rotation_type = kwargs['rotation'] if 'rotation' in kwargs else 'vertical'

    # loop over all columns and plot them in the same plot
    for y_col, label_txt in zip(y_cols, label_data):
        if 'semilog' in kwargs:
            plt.semilogy(x_col, y_col, marker='o', label=label_txt)
        else:
            plt.plot(x_col, y_col, label=label_txt)
        if 'xticks' in kwargs:
#             x_col = [1, 2, 3, 4]
            labels = kwargs['xticks']
            plt.xticks(x_col, labels, rotation=rotation_type)
        
    # setup the plot range
    axes = plt.gca()
    ymin_orig, ymax_orig = axes.get_ylim()
    xmin_orig, xmax_orig = axes.get_xlim()
                
    x_min = float(kwargs['x_min']) if 'x_min' in kwargs else xmin_orig
    x_max = float(kwargs['x_max']) if 'x_max' in kwargs else xmax_orig
    y_min = float(kwargs['y_min']) if 'y_min' in kwargs else ymin_orig
    y_max = float(kwargs['y_max']) if 'y_max' in kwargs else ymax_orig
 
    if 'semilog' in kwargs:
        fmt = ScalarFormatter()
        fmt.set_scientific(False)
        axes.yaxis.set_major_formatter(fmt)  
        
        for tick in axes.xaxis.get_major_ticks():
            tick.label.set_fontsize(14) 

#         for axis in [axes.xaxis, axes.yaxis]:
#             axis.set_major_formatter(ScalarFormatter())
#         axes.yaxis.set_major_formatter(ScalarFormatter())           
    axes.set_xlim([x_min,x_max])
    axes.set_ylim([y_min,y_max])
    
#     for ytick, xtick in zip(axes.yaxis.get_major_ticks(), axes.xaxis.get_major_ticks()):
#         for tick in [ytick, xtick]:
#             tick.label.set_fontsize(14) 
#     plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0., prop={'size': 12})
    fig = plt.gcf()
    plt.show()
    if 'file' in kwargs:
        fig.savefig(kwargs['file'], bbox_inches='tight')
