# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 17:28:53 2021

@author: Snorlax
"""

import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

def fourinone(res,y_pred2, x):
    ### Residual check
    ### Set up Quad graph
    fig = plt.figure()
    fig.suptitle('Residual Summary', fontsize=16)
    fig.set_facecolor('tan')
    
    
    ### QQ-plot
    ax = fig.add_subplot(2, 2, 1)
    sm.qqplot(res,line='s', ax = ax)
    plt.title('QQ plot')
    
    
    ### Res vs fitted value
    ax = fig.add_subplot(2, 2, 2)
    ###Horizontal line
    horiz_line_data = np.array([0,0])
    min_max = np.array([y_pred2.min(),y_pred2.max()])
    ax.plot(min_max, horiz_line_data, 'k--') 
    ### Data
    ax.plot(y_pred2, res, 'o', label="data") # Data
    ax.set_ylabel('Residual')
    ax.set_xlabel('Fitted Value')
    ax.set_title('Residual vs Fitted Value')
    
    ### Histogram of residuals
    ax = fig.add_subplot(2, 2, 3)
    bins = 12
    plt.hist(res, bins, edgecolor="k", alpha=1)
    #plt.xticks(bins)
    ax.set_ylabel('Frequency')
    ax.set_xlabel('Residual')
    ax.set_title('Histogram')
    
    ### Residual vs Observation Order
    ax = fig.add_subplot(2, 2, 4)
    horiz_line_data = np.array([0,0])
    min_max = np.array([x.min(),x.max()])
    ax.plot(min_max, horiz_line_data, 'k--') 
    ax.plot(x, res, '-o', label="data") # Data
    ax.set_ylabel('Residual')
    ax.set_xlabel('Observation Order')
    ax.set_title('Residual vs Observation Order')
    
    fig.tight_layout()
    fig.show()
    return