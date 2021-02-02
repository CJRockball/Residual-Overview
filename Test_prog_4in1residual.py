# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 17:26:22 2021

@author: Snorlax
"""

import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

from fourinone_residual import fourinone


# ### Creat dummy dataset
# for y make 100 numb varied around y=x
y = np.linspace(0,100,100)
# add some wiggle
for i in range(100):
    # any random numbers from -10 and 10
    y[i] = y[i] + 10*np.random.normal(0,1)
#X is just a count
X = np.linspace(0,100,100)


### Fit Regression
model = sm.OLS(y, X)
results = model.fit()

# Summary & prediction
y_pred = results.fittedvalues
res = results.resid


# Regression line data
y_regline_data = results.get_prediction(X).summary_frame(alpha = 0.05)
y_regline = y_regline_data['mean']
plt.plot(X, y_regline,color='black')
plt.scatter(X,y)


#The residuals analysis needs residual data, prediction and 
#order of the data (which is the same as X in this case)

fourinone(res,y_pred, X)




























