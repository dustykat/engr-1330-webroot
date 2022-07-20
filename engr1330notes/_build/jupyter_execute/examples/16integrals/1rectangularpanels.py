#!/usr/bin/env python
# coding: utf-8

# # Rectangular Panels
# 
# 
# :::{note}
# These instructions .. 
# :::
# 
# 
# 
# 

# The figure below is a schematic of a rectangular panels.  The figure is assuming the function structure is known and can be evaluated at an arbitrary location in the $\Delta x$ dimension.
# 
# ![figure2](rect_panels.png)
# 
# Each panel is treated as a rectangle, as shown by the representative panel whose height $y_m$ is chosen visually so that the small cross-hatched areas are as nearly equal as possible. Thus, we form the sum $\sum y_m$ of the effective heights and multiply by $\Delta x$. For a function known in analytical form, a value for $y_m$ equal to that of the function at the midpoint $x_i + \Delta x /2$ may be calculated and used in the summation.
# 
# For tabulated functions, we have to choose to either take $y_m$ as the value at the left endpoint or right endpoint.    This limitation is often quite handy when we are trying to integrate a function that is integrable, but undefined on one endpoint.
# 
# Lets try some examples in Python.
# 
# Find the area under the curve $y= x\sqrt{1+x^2}$  from $x = 0$ to $x = 2$.
# 
# First lets read in the value for the lowerlimit, we will do some limited error checks to be sure user enters a number, but won't check that the number is non-negative.

# :::{admonition} Interactive Code
# The code below could be used for interactive inputs
# 
# 
#     
#     # RectangularPanels.py
#     # Numerical Integration
#     print ("Program finds area under curve y = x * sqrt(1+x)")
#     # Get input data -- use error checking
#     yes = 0
#     while yes == 0:
#         x_low = input("Enter a lower bound x_low \n")
#         try:
#             x_low = float(x_low)
#             yes = 1
#         except:
#         print ("x_low really needs to be a number, try again \n")
#         
#     # exit the while loop when finally have a valid number
#     
#     
# 
# :::

# Verify that value is indeed what we entered

# In[1]:


x_low = 2.0 # replace with code above in proper use
print(x_low)


# Now do the same for the upper limit, notice how we are using the ``yes`` variable.  We set a "fail" value, and demand input until we get "success".  The structure used here is called a ``try -- exception`` structure and is very common in programming.   Error checking is really important so that garbled input does not hang things up. 

# :::{admonition} Interactive Code
# The code below could be used for interactive inputs
#     
#     yes = 0
#     while yes == 0:
#         x_high = input("Enter an upper bound x_high \n")
#         try:
#             x_high = float(x_high)
#             yes = 1
#         except:
#             print ("x_high really needs to be a number, try again \n")
#     # exit the while loop when finally have a valid number
#     
# :::

# Again verify!

# In[2]:


x_high=4.0 # replace with code above in proper use
print(x_high)


# Now use the try - exception structure to input how many panels we wish to use.  Notice you can enter a negative value which will ultimately break things. Also observe this value is an integer.

# :::{admonition} Interactive Code
# The code below could be used for interactive inputs
#     
#     yes = 0
#     while yes == 0:
#         how_many = input("Enter how many panels \n")
#         try:
#             how_many = int(how_many)
#             yes = 1
#         except:
#             print ("Panels really needs to be a number, try again \n")
#     # exit the while loop when finally have a valid number
#     
# :::

# Again verify!

# In[3]:


how_many=5 # replace with code above in proper use
print(how_many)


# Now we can actually perform the integration by evaluating the function at the panel half-widths.
# In this example we are using primitive arithmetic, so the $\sqrt{}$ is accomplished by exponentation, the syntax is ``c = a ** b`` is the operation $c = a^b$.
# 
# The integration uses an accumulator, which is a memory location where subsquent results are added (accumulated) back into the accumulator.  This structure is so common that there are alternate, compact syntax to perform this task, here it is all out in the open.
# 
# The counting loop where we evaluate the function at different ``x`` values, starts at 1 and ends at ``how_many+1`` because python ``for`` loops use an increment skip if equal structure. When the value in ``range`` equals ``how_many`` the ``for`` loop exits (``break`` is implied.)  A loop control structure starting from 0 is shown in the code as a comment line.  Simply uncomment this line, and comment the line just below to have the structure typical in python scripts.  In the start from 1 case, we want to evaluate at the last value of ``how_many``.  

# In[4]:


# OK we should have the three things we need for evaluating the integral
delta_x = (x_high - x_low)/float(how_many)  # compute panel width
xx = x_low + delta_x/2 # initial value for x
### OK THIS IS THE ACTUAL INTEGRATOR PART ###
accumulated_area = 0.0  # initial value in an accumulator
#for i in range(0,how_many,1): #note we are counting from 0
for i in range(1,how_many+1,1): #note we are counting from 1
    accumulated_area = accumulated_area + ( xx * ( (1+xx**2)**(0.5) ) ) * delta_x
    xx = xx + delta_x
### AND WE ARE DONE INTEGRATING #############


# Finally, we want to report our result

# In[5]:


print ("Area under curve y = x * sqrt(1+x) from x = ",x_low,      " to x = ",x_high,"\n is approximately: ",accumulated_area)
# the backslash \
#       " to x = .....     lets us use multiple lines
# the \n is a "newline" character 


# The code implements rudimentary error checking -- it forces us to enter numeric values for the lower and upper values of $x$ as well as the number of panels to use.  It does not check for undefined ranges and such, but you should get the idea -- notice that a large fraction of the entire program is error trapping; this devotion to error trapping is typical for professional programs where you are going to distribute executable modules and not expect the end user to be a programmer.
# 
# ## Using the `math` package
# 
# The actual computations are done rather crudely -- there is a math package that would give us the ability to compute the square root as a function call rather than exponentiation to a real values exponent.
# 
# That is illustrated below

# In[6]:


# RectangularPanels.py
# Numerical Integration
# Use built-in math functions
import math  # a package of math functions
# we are naming an object "sqrt" that will compute the square root
def sqrt (x):
        return math.sqrt(x)
# saves us having to type math.NAME every time we wish to use a function
# in this program not all that meaningful, but in complex programs handy!
x_low=0 #this is for JB demo only
x_high=2
how_many=6
print ("Program finds area under curve y = x * sqrt(1+x)")
# Get input data -- use error checking
yes = 1  #set to 0 for interacitve input
while yes == 0:
    x_low = input("Enter a lower bound x_low \n")
    try:
        x_low = float(x_low)
        yes = 1
    except:
        print ("x_low really needs to be a number, try again \n")
yes = 1 #set to 0 for interacitve input
while yes == 0:
    x_high = input("Enter an upper bound x_high \n")
    try:
        x_high = float(x_high)
        yes = 1
    except:
        print ("x_high really needs to be a number, try again \n")
yes = 1 #set to 0 for interacitve input
while yes == 0:
    how_many = input("Enter how many panels \n")
    try:
        how_many = int(how_many)
        yes = 1
    except:
        print ("Panels really needs to be a number, try again \n")
        

delta_x = (x_high - x_low)/float(how_many)  # compute panel width
accumulated_area = 0.0  # initial value in an accumulator
xx = x_low + delta_x/2 # initial value for x
for i in range(1,how_many+1,1): #note we are counting from 1
    accumulated_area = accumulated_area + ( xx * sqrt(1+xx**2) ) * delta_x
    xx = xx + delta_x
print ("Area under curve y = x * sqrt(1+x) from x = ",x_low,      " to x = ",x_high,"\n is approximately: ",accumulated_area)

