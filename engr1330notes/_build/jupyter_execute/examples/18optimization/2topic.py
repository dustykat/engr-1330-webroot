#!/usr/bin/env python
# coding: utf-8

# # Grid Search Methods
# 
# Grid search methods are simple to conceptualize and can provide useful starting values for more elaborate tools.  The substance manufacturing example used a simplistic grid search method that implicitly searched integer space only, here another example will use sequential searches - a first to get close to a region where good solutions exist, and a second refinement search.
# 
# ## Minimum-Weight Structure
# 
# Consider a structure that is comprosed of two cylindrical load bearing columns whose diameter in feet are $r_1$ and $r_2$.  The weight of the structure in pounds is given by the expression:
# 
# $ y = 1000*(10+(r_1 - 0.5)^2+(r_2-0.5)^2 ~)$<br>

# In[1]:


def weight(r1,r2):
    weight = 1000*(10 + (r1-0.5)**2 + (r2-0.5)**2)
    return weight


# The goal is to determine the values of $r_1$ and $r_2$ that minimize the weight and satisfy the additional constraints below:
# 
# 1. The combined cross-sectional area of the two columns must be at least 10 square feet;<br>$\pi (r_1^2 + r_2^2) \ge 10$
# 2. The radius of one column may not exceed 1.25 the radius of the other column;<br>
# $r_1 \le 1.25r_2$
# 3. Nonnegativity; <br>$r_1 \ge 0; r_2 \ge 0$
# 
# Expressed as scripted functions (which are to be larger than zero if feasible)

# In[2]:


def con1(r1,r2):
    import math
    con1 = math.pi*(r1**2 + r2**2)-10
    return con1

def con2(r1,r2):
    con2 = 1.25*r2-r1
    return con2


# As before we make a test script to convert into our optimization model

# In[3]:


r1=1.262
r2=1.262
objective = weight(r1,r2)
constraint1 = con1(r1,r2)
constraint2 = con2(r1,r2)
print("Current Solution r1 = ",r1," r2 = ",r2)
print("Objective Value = ",objective)
print("Constraint 1 Value = ",constraint1)
print("Constraint 2 Value = ",constraint2)
if constraint1 >= 0 and constraint2 >=0 and r1 >=0 and r2 >= 0:
    print("All constraints satisfied solution is FEASIBLE")
else:
    print("One or more constraints violated solution is INFEASIBLE")


# Now put it into a model function that computes the objective value and a feasibility code (0=feasible, 1=not feasible) and put remaining logic into the search algorithm.

# In[4]:


def mymodel(r1,r2):
    objective = weight(r1,r2)
    constraint1 = con1(r1,r2)
    constraint2 = con2(r1,r2)
    if constraint1 >= 0 and constraint2 >=0 and r1 >=0 and r2 >= 0:
        returncode = 0
    else:
        returncode = 1
    return (objective,returncode) # return a tuple


# Here we make the search, notice is practically the same code as before, with only some minor changes in variable names, and repetition counting.

# In[5]:


Avector = [] # empty list to store values of r1
Bvector = [] # empty list to store values of r2
stepsize = 0.01 # coarse step size
r1value = 1.0-stepsize
r2value = 1.0-stepsize
howmanysteps = 1000
for i in range(howmanysteps):
    r1value = r1value+stepsize #rescales the region from 0 to 3 in steps of 0.001
    r2value = r2value+stepsize
    Avector.append(r1value)
    Bvector.append(r2value)
# now the actual search
howmany = 0 # keep count of how many combinations
small   = 1e99 # a big value, we are minimizing
xbest   = -1 # variables to store our best solution
ybest   = -1
feasible = 0 #keep count of feasible combinations
for ix1 in range(howmanysteps):
    for ix2 in range(howmanysteps):
        howmany = howmany+1
        result = mymodel(Avector[ix1],Bvector[ix2])
        if result[1] == 0:
            if result[0] < small:
                feasible = feasible + 1
                small = result[0]
                xbest = Avector[ix1]
                ybest = Bvector[ix2]

print("Search Complete ",howmany," Total Combinations Examined")
print("Found ",feasible, "Feasible Solutions \n --- Best Solution ---")
print("Radius 1 = ",xbest)
print("Radius 2 = ",ybest)
print("Objective Function Value = ",small)
print("Constraint 1 Value = ",con1(xbest,ybest))
print("Constraint 2 Value = ",con2(xbest,ybest))   


# And we now have an initial guess to work with, we can make another search over a smaller region starting from here

# In[6]:


Avector = [] # empty list to store values of r1
Bvector = [] # empty list to store values of r2
stepsize = 0.001 # fine stepsize, start near last solution
r1value = 1.1-stepsize
r2value = 1.1-stepsize
howmanysteps = 1000
for i in range(howmanysteps):
    r1value = r1value+stepsize #rescales the region from 0 to 3 in steps of 0.001
    r2value = r2value+stepsize
    Avector.append(r1value)
    Bvector.append(r2value)
# now the actual search
howmany = 0 # keep count of how many combinations
small   = 1e99 # a big value, we are minimizing
xbest   = -1 # variables to store our best solution
ybest   = -1
feasible = 0 #keep count of feasible combinations
for ix1 in range(howmanysteps):
    for ix2 in range(howmanysteps):
        howmany = howmany+1
        result = mymodel(Avector[ix1],Bvector[ix2])
        if result[1] == 0:
            if result[0] < small:
                feasible = feasible + 1
                small = result[0]
                xbest = Avector[ix1]
                ybest = Bvector[ix2]

print("Search Complete ",howmany," Total Combinations Examined")
print("Found ",feasible, "Feasible Solutions \n --- Best Solution ---")
print("Radius 1 = ",xbest)
print("Radius 2 = ",ybest)
print("Objective Function Value = ",small)
print("Constraint 1 Value = ",con1(xbest,ybest))
print("Constraint 2 Value = ",con2(xbest,ybest)) 


# From here we could refine further to try to get closer to an optimal solution, but given that we are close to constraint 1 ($\ge 0$) we could probably stop, also observe we only have 70 feasible solutions out of 1 million combinations. But because its easy in this problem, lest trys a finer search just cause.

# In[7]:


Avector = [] # empty list to store values of r1
Bvector = [] # empty list to store values of r2
stepsize = 0.0001 # really fine stepsize, start near last solution
r1value = 1.23-stepsize
r2value = 1.26-stepsize
howmanysteps = 1000
for i in range(howmanysteps):
    r1value = r1value+stepsize #rescales the region from 0 to 3 in steps of 0.001
    r2value = r2value+stepsize
    Avector.append(r1value)
    Bvector.append(r2value)
# now the actual search
howmany = 0 # keep count of how many combinations
small   = 1e99 # a big value, we are minimizing
xbest   = -1 # variables to store our best solution
ybest   = -1
feasible = 0 #keep count of feasible combinations
for ix1 in range(howmanysteps):
    for ix2 in range(howmanysteps):
        howmany = howmany+1
        result = mymodel(Avector[ix1],Bvector[ix2])
        if result[1] == 0:
            if result[0] < small:
                feasible = feasible + 1
                small = result[0]
                xbest = Avector[ix1]
                ybest = Bvector[ix2]

print("Search Complete ",howmany," Total Combinations Examined")
print("Found ",feasible, "Feasible Solutions \n --- Best Solution ---")
print("Radius 1 = ",xbest)
print("Radius 2 = ",ybest)
print("Objective Function Value = ",small)
print("Constraint 1 Value = ",con1(xbest,ybest))
print("Constraint 2 Value = ",con2(xbest,ybest)) 


# Here we should just stop, we are at the constraint 1 limit, and have a workable solution.
# 
# ## Classical Grid Search
# 
# To summarize a classical grid search process requires:
# 
# 1. A model function that determines the objective value and feasibility when supplied with design variables
# 2. An algorithm that identifies values of design variables to search, if you imagine each variable as an axis in an orthogonal hyperplane, then we are secrhing a pre-selected region.
# 3. A tabulating algorithm that only records feasible, non-inferior (improving objective value).
# 4. Clock cycles.  This technique is quite slow and makes a lot of function calls.  It is not elegant, but might be valuable for initial conditions, or crude estimates.  Notice in the last example we made 3 million function evaluations - if each evaluation takes a second to complete, the process would take almost 35 days to find a whopping 197 feasible solutions!
# 
# :::{admonition} Get Started
# :class: tip
# 
# Even though grid search is slow, its robust.  It is a good place to start because you may be able to get a code up and running in a week.  You can then set it on its hopeless search while you pursue more elegant methods.  If these methods fail, you always have the grid search running in the background guarenteeing (hopefully) at least one feasible solution.  
# 
# Don't let elegance get in the way of getting things done!
# :::
# 
# <!-- ## Method-of-Darts (Future) -->

# ## Solving using `scipy`
# 
# Setting up the same problem in scipy requires some reading of the [scipy.optimization](https://docs.scipy.org/doc/scipy/tutorial/optimize.html#sequential-least-squares-programming-slsqp-algorithm-method-slsqp) documentation.  Here I wanted to avoid having to define the derivatives, Jacobian, and Hessian.  The method that seems to fit this problem is called the *Sequential Least SQuares Programming (SLSQP) Algorithm (method=`SLSQP`)*  Below is the same problem setup using the package.
# 
# 

# In[8]:


import numpy as np
from scipy.optimize import minimize
from scipy.optimize import Bounds
import math

def objfn(x):
    return 1000*(10 + (x[0]-0.5)**2 + (x[1]-0.5)**2) # our objective function
bounds = Bounds([0.0, 0.0], [3.0, 3.0]) # define the search region
ineq_cons = {'type': 'ineq','fun' : lambda x: np.array([(math.pi*(x[0]**2 + x[1]**2)-10),(1.25*x[1]-x[0])])} # set the inequality constraints
eq_cons = {'type': 'eq',} # null equality constraints - not used this example
x0 = np.array([1.0, 1.0]) # initial guess
res = minimize(objfn, x0, method='SLSQP', jac="2-point", constraints=[ineq_cons], options={'ftol': 1e-9},bounds=bounds)
# report results
print("Return Code ",res["status"])
print(" Function Evaluations ",res["nfev"])
print(" Jacobian Evaluations ",res["njev"])
print(" --- Objective Function Value --- \n   ",round(res["fun"],2)," pounds")
print(" Current Solution Vector \n  ",res["x"])


# Observe in this case far quicker and fewer function evaluations (62 if we assume the Jacobian needs 4 evaluations per its evaluation + the 30 in the linesearch).  Still way fewer than 3 million.  Now lets check the solution using our code:

# In[9]:


r1=1.261567
r2=1.261567
objective = weight(r1,r2)
constraint1 = con1(r1,r2)
constraint2 = con2(r1,r2)
print("Current Solution r1 = ",r1," r2 = ",r2)
print("Objective Value = ",objective)
print("Constraint 1 Value = ",constraint1)
print("Constraint 2 Value = ",constraint2)
if constraint1 >= 0 and constraint2 >=0 and r1 >=0 and r2 >= 0:
    print("All constraints satisfied solution is FEASIBLE")
else:
    print("One or more constraints violated solution is INFEASIBLE")


# Yep, the 'scipy' solution is correct and better than our best from a grid search.  

# ## Labor allocation using `scipy`
# 
# Lets revisit the labor allocation problem using the same tool with a caveat.  The labor allocation is an integer problem, and `SLSQP` is a real number solver, so we may not get the exact same answer, but partial substance is encouraged by the cartel, after all we are making illegal substances, so what if we cheat our customers a little bit (it is the Amazonian way!)

# In[10]:


def con1(x1,x2):
    # con1 >= 0 is feasible
    con1 = x1+x2 - 1000
    return con1
def con2(x1,x2):
    # con2 >=0 is feasible
    con2 = 8000.0 - 5.0*x1 -3.0*x2
    return con2
def myobj(xvec):
    myobj = ((5*12-120)*xvec[0] + (3*12-80)*xvec[1]) # change sense for minimization
    return myobj

import numpy as np
from scipy.optimize import minimize
from scipy.optimize import Bounds
import math

bounds = Bounds([0.0, 0.0], [3000.0, 3000.0]) # define the search region
ineq_cons = {'type': 'ineq','fun' : lambda x: np.array([con1(x[0],x[1]),con2(x[0],x[1])])} # set the inequality constraints
eq_cons = {'type': 'eq',} # null equality constraints - not used this example
x0 = np.array([500, 1500]) # initial guess
res = minimize(myobj, x0, method='SLSQP', jac="2-point", constraints=[ineq_cons], options={'ftol': 1e-9},bounds=bounds)
# report results
print("Return Code ",res["success"])
print("Message ",res["message"])
print(" Function Evaluations ",res["nfev"])
print(" Jacobian Evaluations ",res["njev"])
print(" --- Objective Function Value --- \n   ",-1*round(res["fun"],2)," dollars")
print(" Current Solution Vector \n  ",res["x"])


# Here we have typical result for an integer model solved in continuous real space.  The program exited in a failed linesearch, but did return its last best value, which if we round down and apply in our own script we discover the answer is close to our lineseacrh result.  Further if we use the `scipy` result to inform our homebrew we can quickly experiment to find an integer solution that is better than the `scipy` solution.

# In[11]:


def mymodel(x1,x2):
    xvec=[x1,x2]
    objvalue = myobj(xvec)
    constraint1 = con1(x1,x2)
    constraint2 = con2(x1,x2)
# print current results
    print("Substance A produced = ",x1)
    print("Substance B produced = ",x2)
    print("Objective Function Value = ",-1*objvalue)
    print("Minimun Production Constraint = ",constraint1)
    print("Maximum Labor Budget = ",constraint2)
    if constraint1 < 0 or constraint2 < 0 or x1 < 0 or x2 <0:
        print("Solution is INFEASIBLE")
    else:
        print("Solution is FEASIBLE")
    return
x1=0
x2=2666
mymodel(x1,x2)


# In[12]:


mymodel(1,2665)


# In[ ]:




