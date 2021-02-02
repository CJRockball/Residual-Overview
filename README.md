# Residual-Overview
Residual Overview

The fourinone_residual plots four graphs to check your residuals. It is a based on the 4in1 from MINITAB.

The residual analysis and plot is in a function in the file fourinone_residual. The Test_prog_4in1residual is just a small test program that can be used for testing. For the residual to work it needs to be called with residual data (I use statsmodels but that can be modified as wanted), prediction and the data order (in the test program called X)

The analysis has four graphs.
 
 ![plot](Residual-Overview/Images/4in1.png)
 
QQ plot: Shows normality of the residual.
Residuals vs Fitted Value: Will show if there is heteroskedasticity.
Histogram: Shows normality, you might need to adjust binning.
Residual vs Observation Order: Shows if there is drift in the data.


