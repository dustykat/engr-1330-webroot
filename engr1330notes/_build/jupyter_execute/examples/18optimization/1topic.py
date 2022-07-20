#!/usr/bin/env python
# coding: utf-8

# # Scheduling Example
# 
# Suppose you are manufacturing two illegal substances in your dorm room, $\textbf{A}$ and $\textbf{B}$, which can be sold for $\$$120 per unit for substance $\textbf{A}$ and $\$$80 for substance $\textbf{B}$.  The cartel requires that at least 1000 total units be manufactured each month.  Product $\textbf{A}$ requires five hours of labor, product $\textbf{B}$ requires three hours of labor per unit.  The cost of your labor is $\$$12 per hour, and a total of 8000 hours per month of labor is available (basically your whole floor). Determine a production schedule that will maximize the net revenue.  
# 
# The conversion of this description into a mathematical program is the next important step 
# 
# ## Decision Variables
# 
# First we define decision variables (sadly we already made a bad decision working for the cartel, but let's make the best of our remaining time on Earth!)
# 
# $x_1 = \text{units of }A\text{ per month}$ <br>
# $x_1 = \text{units of }B\text{ per month}$ <br>
# 
# ## Objective Function
# 
# Here we wish to define the objective function, which in this example is net revenue
# 
# $y(x_1,x_2) = [120 - (5 \times 12)]x_1 + [80 - (3 \times 12)]x_2$<br>
# 
# In a Jupyter Notebook it would be something like:

# In[1]:


def myobj(x1,x2):
    myobj = (120-5*12)*x1 + (80-3*12)*x2
    return myobj


# ## Constraints
# 
# Next we need to define constraints.  The specific way will depend on the minimization package you choose, we will examine that later on.  Here we will list them and create functions to simply evaluate the constraints.
# 
# ### Minimium Required Production
# 
# $x_1 + x_2 \ge 1000$<br>
# 
# ### Maximum Available Budget for Labrador
# 
# $5 x_1 + 3 x_2 \le 8000$<br>
# 
# ### Non-Negativity
# 
# $x_1 \ge 0; x_2 \ge 0$<br>

# In[2]:


def con1(x1,x2):
    # con1 >= 0 is feasible
    con1 = x1+x2 - 1000
    return con1
def con2(x1,x2):
    # con2 >=0 is feasible
    con2 = 8000 - 5*x1 -3*x2
    return con2


# At this point we can build a model of the problem (no solution technique just yet).  The problem as stated is integer, but we will pretend that real-valued (fractional) units are OK.  
# 
# Our program is below, we can even supply code to test for feasibility.

# In[3]:


def mymodel(x1,x2):
    objvalue = myobj(x1,x2)
    constraint1 = con1(x1,x2)
    constraint2 = con2(x1,x2)
# print current results
    print("Substance A produced = ",x1)
    print("Substance B produced = ",x2)
    print("Objective Function Value = ",objvalue)
    print("Minimun Production Constraint = ",constraint1)
    print("Maximum Labor Budget = ",constraint2)
    if constraint1 < 0 or constraint2 < 0 or x1 < 0 or x2 <0:
        print("Solution is INFEASIBLE")
    else:
        print("Solution is FEASIBLE")
    return
x1=500
x2=500
mymodel(x1,x2)


# Observe our labor budget is still available, so we can increase production and improve our revenue; lets try more $\textbf{B}$

# In[4]:


x1=500
x2=1833
mymodel(x1,x2)


# Now our revenue is over 2 times bigger that our initial guess.  Our next task is to automate the quest for a bestest solution.  
# 
# ### Grid Search Method
# 
# The easiest approach (but computationally very expensive and incredibly slow) is a grid search - we simply specify values of $\textbf{A}$ and $\textbf{B}$ in a repetition structure, and compute the objective value and whether the solution is feasible, and just save the best.  The script below implements a crude search.
# 
# First suppress all the output in the function 

# In[5]:


def mymodel(x1,x2):
    objvalue = myobj(x1,x2)
    constraint1 = con1(x1,x2)
    constraint2 = con2(x1,x2)
# print current results
#    print("Substance A produced = ",x1)
#    print("Substance B produced = ",x2)
#    print("Objective Function Value = ",objvalue)
#    print("Minimun Production Constraint = ",constraint1)
#    print("Maximum Labor Budget = ",constraint2)
    if constraint1 < 0 or constraint2 < 0 or x1 < 0 or x2 < 0:
#        print("Solution is INFEASIBLE")
        returncode = 0
    else:
#       print("Solution is FEASIBLE")
        returncode = 1
    return (objvalue,returncode) # return a tuple


# Now a search code to search all combinations of $x_1$ and $x_2$ in the range [0,3000] (the range is an educated guess of the values to search)

# In[6]:


Avector = [] # empty list to store values of A
Bvector = [] # empty list to store values of B
howmany = 0
for i in range(3000):
    Avector.append(float(i))
    Bvector.append(float(i))
# now the actual search
big = -1 # a negative value, revenue needs to be positive
xbest = -1 # variables to store our best solution
ybest = -1
feasible = 0
for ix1 in range(3000):
    for ix2 in range(3000):
        howmany = howmany+1
        result = mymodel(Avector[ix1],Bvector[ix2])
        if result[1] == 1:
            if result[0] > big:
                feasible = feasible + 1
                big = result[0]
                xbest = Avector[ix1]
                ybest = Bvector[ix2]

print("Search complete ",howmany," Total Combinations")
print("Found ",feasible, "feasible solutions \n --- Best Solution ---")
print("Substance A produced = ",xbest)
print("Substance B produced = ",ybest)
print("Objective Function Value = ",big)
print("Production Above Minimum = ",con1(xbest,ybest))
print("Labor Budget Remaining = ",con2(xbest,ybest))        


# # Unconstrained Minimization
