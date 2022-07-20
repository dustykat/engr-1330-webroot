#!/usr/bin/env python
# coding: utf-8

# # Trapezoidal Panels
# 
# The trapezoidal panels are approximated as shown in the figure below. 
# 
# ![](trap_panels.png)
# 
# The area $A_i$ is the average height $(y_i + y_{i+1} )/2$ times $\Delta x$. Adding the areas gives the area approximation as tabulated.   For the example with the curvature shown, the approximation will be on the low side. For the reverse curvature, the approximation will be on the high side.  The trapezoidal approximation is commonly used with tabulated values.
# 
# The script below illustrates the trapezoidal method for approximating an integral.  In the example, the left and right panel endpoints in $x$ are set as separate variables $x_{left}$ and $x_{right}$ and incremented by $\Delta x$ as we step through the count-controlled repetition to accumulate the area.  The corresponding $y$ values are computed within the loop and averaged, then multiplied by $\Delta x$ and added to the accumulator.  Finally the $x$ values are incremented --- for grins, we used the += operator on the accumulator
# 

# In[1]:


# TrapezoidalPanels.py
# Numerical Integration
# Use built-in math functions
import math  # a package of math functions
# we are naming an object "sqrt" that will compute the square root
def sqrt (x):
        return math.sqrt(x)
# saves us having to type math.NAME every time we wish to use a function
# in this program not all that meaningful, but in complex programs handy!
###################################
x_low=0 #this is for JB demo only #
x_high=2                          #
how_many=6                        #
###################################
print ("Program finds area under curve y = x * sqrt(1+x)")
# Get input data -- use error checking
yes = 1 # Set this to 1 to activate interactive inputs
while yes == 0:
    x_low = input("Enter a lower bound x_low \n")
    try:
        x_low = float(x_low)
        yes = 1
    except:
        print ("x_low really needs to be a number, try again \n")
yes = 1
while yes == 0:
    x_high = input("Enter an upper bound x_high \n")
    try:
        x_high = float(x_high)
        yes = 1
    except:
        print ("x_high really needs to be a number, try again \n")
yes = 1
while yes == 0:
    how_many = input("Enter how many panels \n")
    try:
        how_many = int(how_many)
        yes = 1
    except:
        print ("Panels really needs to be a number, try again \n")
delta_x = (x_high - x_low)/float(how_many)  # compute panel width
accumulated_area = 0.0      # initial value in an accumulator
x_left = x_low              # initial value for x_left edge panel
x_right = x_left + delta_x  # initial value for x_right edge panel
for i in range(1,how_many+1,1): #note we are counting from 1
    y_left = ( x_left* sqrt(1+x_left**2) )
    y_right = ( x_right* sqrt(1+x_right**2) )
    accumulated_area += + (1./2.) * ( y_left + y_right ) * delta_x
    x_left += delta_x
    x_right += delta_x
print ("Area under curve y = x * sqrt(1+x) from x = ",x_low,      " to x = ",x_high,"\n is approximately: ",accumulated_area)

