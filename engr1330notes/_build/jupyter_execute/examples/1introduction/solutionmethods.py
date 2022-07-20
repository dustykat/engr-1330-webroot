#!/usr/bin/env python
# coding: utf-8

# # Solution/Analysis Methods
# 
# Once the problem is defined and formulated (sketch, knowns/unknowns, governing principles) it must be solved for the unknown quantities.  Often (a lot!) this step will require a particular mathematical procedure appropriate for the problem under consideration, as such familarity with commonly used methods is vital as is an ability to identify which procedure may fit your problem.  
# 
# Some of the more common/frequent Engineering Problem Solving methods are listed below:
# 
# 1. *Data analysis techniques*.  Simple (to complex) statistical techniques to analyze data (e.g. means, medians, modes, standard deviations, quantiles, and histograms)  Their use allows an engineer to make meaningful conclusions about information contained in a set of data.
# 2. *Curve-fitting techniques*.  Called data modeling herein. Here we are trying to pass a curve (model) through an aggregate of data rather than through individual data points.  It is a systematic way to "eyeball" a curve through a set of data points.  The resulting curve is of more value than individual points especially when the points are subject to scatter.  The resulting data model can be differentiated and integrated whereas the data cannot (usually).  The model can extrapolate beyond the observed set.
# 3. *Interpolation techniques*. Methods to allow an engineer to obtain accurate estimates for a dependent variable when the corresponding independent variable falls within a set of tabulated (and accurate) data points.  These kinds of problems arise frequently when working with measurements.
# 4. *Single algebraic equations* frequently appear in all areas of engineering - being able to solve them quickly and efficiently is vital; elegance is not always sought - brute force is quite appropriate.
# 5. *Simultaneous linear algebraic equations* also frequently appear in similar situations as the single equations above either by added complexity to the problem conditions, or added dimensionality of the problem.  Many very complicated problems in engineering analysis and design are represented as a set of simultaneous equations.
# 6. *Single and Simultaneous Non-linear algebraic equations* also frequently appear in engineering.  As a category these are quite a bit harder to solve, but many useful cases are solvable.
# 7. *Evaluating intergrals*  In calculus the interpretation of an integral as area under a curve is leveraged in engineering to determine avarages of cumulative effect of some process that varies with time or distance.
# 8. *Engineering economic analysis*  Most engineering problems have multiple solutions.  The end decision is often based on economic considerations.  Engineering economic analysis provides criteria and methods for comparing different solutions on some common basis.
# 9. *Optimization Tools* If a problem has multiple solutions finding a best solution may involve tedious and lengthy search procuedures.  Optimization methods are systematic ways to speed up these searches.
# 10. *Probability Estimation Models*  A subclass of curve fitting in a sense, used to estimate magnitudes of rare occurances based on limited sets of observations.  
# 
# Computational Thinking/ Data Science Problem Solving:
# 
# 11. *Regression Modeling* A machine learning topic, curve-fitting (above) is closely related
# 12. *Classification* Another machine learning topic.  A legitimate engineering application is in manufacturing quality control.  Logistic regression is related to this category, regression modeling (above), probability and curve-fitting
# 

# In[ ]:




