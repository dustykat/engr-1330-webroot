#!/usr/bin/env python
# coding: utf-8

# # Nonlinear Systems of Equations
# 
# Non-linear systems are extensions of the linear systems cases except the systems involve products and powers of the unknown variables. Non-linear problems are often quite difficult to manage, especially when the systems are large (many rows and many variables).
# The solution to non-linear systems, if non-trivial or even possible, are usually iterative. Within the iterative steps is a linearization component – these linear systems which are intermediate computations within the overall solution process are treated by an appropriate linear system method (direct or iterative).
# Consider the system below:
# 
# \begin{gather}
# \begin{matrix}
# x^2 & +~y^2  \\
#  e^x & +~y  \\
# \end{matrix}
# \begin{matrix}
# = 4\\
# = 1\\
# \end{matrix}
# \end{gather}
# 
# Suppose we have a solution guess $x_{k},y_{k}$, which of course could be wrong, but we could linearize about that guess as
# 
# \begin{gather}
# \mathbf{A} =
# \begin{pmatrix}
# x_k & + ~y_k  \\
# 0 & + ~1  \\
# \end{pmatrix}
# ~\mathbf{x} = 
# \begin{pmatrix}
# x_{k+1} \\
# y_{k+1} \\
# \end{pmatrix}
# ~ \mathbf{b} = 
# \begin{pmatrix}
# 4\\
# 1 - e^{x_k}\\
# \end{pmatrix}
# \end{gather}
# 
# Now if we assemble the system in the usual fashion, $\mathbf{A} \cdot \mathbf{x_{k+1}} = ~ \mathbf{b}~$ we have a system of linear equations\footnote{Linear in $\mathbf{x_{k+1}}$}, which expanded look like:
# 
# \begin{gather}
# \begin{pmatrix}
# x_k & + ~y_k  \\
# 0 & + ~1  \\
# \end{pmatrix}
# \cdot
# \begin{pmatrix}
# x_{k+1} \\
# y_{k+1} \\
# \end{pmatrix}
# ~ = 
# \begin{pmatrix}
# 4\\
# 1 - e^{x_k}\\
# \end{pmatrix}
# \end{gather}
# 
# Now that the system is linear, and we can solve for $\mathbf{x_{k+1}}$ using our linear system solver for the new guess.
# If the system is convergent (not all are) then if we update, and repeat  we will eventually find a result.
# 
# What one really needs is a way to construct the linear system that has a systematic update method, that is discussed below

# ## Multiple-variable extension of Newton’s Method
# 
# This section presents the Newton-Raphson method as a way to sometimes solve systems of non-linear equations.
# 
# Consider an example where the function \textbf{f} is a vector-valued function of a vector argument.
# 
# \begin{gather}
# \mathbf{f(x)} = 
# \begin{matrix}
# f_1 = & x^2 & +~y^2 & - 4\\
# f_2 = & e^x & +~y  & - 1\\
# \end{matrix}
# \end{gather}
# 
# Let's also recall Newtons method for scalar valued function of a single variable.
# 
# \begin{equation}
# x_{k+1}=x_{k} - \frac{  f(x_{k})  }{   \frac{df}{dx}\rvert_{x_k} } 
# \label{eqn:NewtonFormula}
# \end{equation}
# 
# When extending to higher dimensions, the analog for $x$ is the vector \textbf{x} and the analog for the function $f()$ is the vector function \textbf{f()}.
# What remains is an analog for the first derivative in the denominator (and the concept of division of a matrix).
# 
# The analog to the first derivative is a matrix called the Jacobian which is comprised of the first derivatives of the function \textbf{f} with respect to the arguments \textbf{x}.   
# For example for a 2-value function of 2 arguments (as our example above)
# 
# \begin{equation}
# \frac{df}{dx}\rvert_{x_k} =>
# \begin{pmatrix}
# \frac{\partial f_1}{\partial x_1} & \frac{\partial f_1}{\partial x_2} \\
# ~ & ~ \\
# \frac{\partial f_2}{\partial x_1} & \frac{\partial f_2}{\partial x_2} \\
# \end{pmatrix}
# \label{eqn:Jacobian}
# \end{equation}
# 
# Next recall that division is replaced by matrix multiplication with the multiplicative inverse, so the analogy continues as
# 
# \begin{equation}
# \frac{1}{\frac{df}{dx}\rvert_{x_k}} =>
# {\begin{pmatrix}
# \frac{\partial f_1}{\partial x_1} & \frac{\partial f_1}{\partial x_2} \\
# ~ & ~ \\
# \frac{\partial f_2}{\partial x_1} & \frac{\partial f_2}{\partial x_2} \\
# \end{pmatrix}}^{-1}
# \label{eqn:JacobianInverse}
# \end{equation}
# 
# Let's name the Jacobian \textbf{J(x)}.
# 
# So the multi-variate Newton's method can be written as
# 
# \begin{equation}
# \mathbf{x}_{k+1}=\mathbf{x}_{k} - \mathbf{J(x)}^{-1}\rvert_{x_k} \cdot \mathbf{f(x)}\rvert_{x_k}
# \label{eqn:VectorNewtonFormula}
# \end{equation}

# In the linear systems lessons we did find a way to solve for an inverse, but it's not necessary, and is computationally expensive to invert in these examples -- a series of rearrangement of the system above yields a nice scheme that does not require inversion of a matrix.
# 
# First, move the $\mathbf{x}_{k}$ to the left-hand side.
# 
# \begin{equation}
# \mathbf{x}_{k+1}-\mathbf{x}_{k} = - \mathbf{J(x)}^{-1}\rvert_{x_k} \cdot \mathbf{f(x)}\rvert_{x_k}
# \end{equation}
# 
# Next multiply both sides by the Jacobian (The Jacobian must be non-singular otherwise we are dividing by zero)
# 
# \begin{equation}
# \mathbf{J(x)}\rvert_{x_k} \cdot (\mathbf{x}_{k+1}-\mathbf{x}_{k}) = - \mathbf{J(x)}\rvert_{x_k} \cdot \mathbf{J(x)}^{-1}\rvert_{x_k} \cdot \mathbf{f(x)}\rvert_{x_k}
# \end{equation}
# 
# Recall a matrix multiplied by its inverse returns the identity matrix (the matrix equivalent of unity)
# 
# \begin{equation}
# -\mathbf{J(x)}\rvert_{x_k} \cdot (\mathbf{x}_{k+1}-\mathbf{x}_{k}) = \mathbf{f(x)}\rvert_{x_k}
# \end{equation}
# 
# So we now have an algorithm:
# 
# 1) Start with an initial guess $\mathbf{x}_{k}$, compute $\mathbf{f(x)}\rvert_{x_k}$, and $\mathbf{J(x)}\rvert_{x_k}$.
# 
# 2) Test for stopping.  Is $\mathbf{f(x)}\rvert_{x_k}$ close to zero?  If yes, exit and report results, otherwise continue.
# 
# 3) Solve the linear system $\mathbf{J(x)}\rvert_{x_k} \cdot (\mathbf{x}_{k+1}-\mathbf{x}_{k}) = \mathbf{f(x)}\rvert_{x_k}$.
# 
# 4) Test for stopping.  Is $ (\mathbf{x}_{k+1}-\mathbf{x}_{k})$ close to zero?  If yes, exit and report results, otherwise continue.
# 
# 5) Compute the update $\mathbf{x}_{k+1} = \mathbf{x}_{k} - (\mathbf{x}_{k+1}-\mathbf{x}_{k}) $, then
# 
# 6) Move the update into the guess vector $\mathbf{x}_{k} <=\mathbf{x}_{k+1}$ =and repeat step 1. Stop after too many steps.
# 

# 

# ## Example using Analytical Derivatives
# 
# Now to complete the example we will employ this algorithm.
# 
# The function (repeated)
# 
# \begin{gather}
# \mathbf{f(x)} = 
# \begin{matrix}
# f_1 = & x^2 & +~y^2 & - 4\\
# f_2 = & e^x & +~y  & - 1\\
# \end{matrix}
# \end{gather}
# 
# Then the Jacobian, here we will compute it analytically because we can
# 
# \begin{equation}
# \mathbf{J(x)}=>
# {\begin{pmatrix}
# 2x & 2y \\
# ~ & ~ \\
# e^x & 1 \\
# \end{pmatrix}}
# \end{equation}
# 
# Now for the scripts.
# 
# We will start by defining the two equations, and their derivatives, as well a a vector valued function `func` and its Jacobian `jacob` as below.  Here the two modules `LinearSolverPivot` and `vector_matrix_lib` are just python source code files containing prototype functions.

# In[1]:


#################################################################
# Newton Solver Example -- Analytical Derivatives               #
#################################################################
import math   # This will import math module from python distribution
from LinearSolverPivot import linearsolver # This will import our solver module
from vector_matrix_lib import writeM,writeV,vdotv,vvsub # This will import our vector functions

def eq1(x,y):
    eq1 = x**2 + y**2 - 4.0
    return(eq1)

def eq2(x,y):
    eq2 = math.exp(x) + y - 1.0
    return(eq2)

def ddxeq1(x,y):
    ddxeq1 = 2.0*x
    return(ddxeq1)

def ddyeq1(x,y):
    ddyeq1 = 2.0*y
    return(ddyeq1)

def ddxeq2(x,y):
    ddxeq2 = math.exp(x)
    return(ddxeq2)

def ddyeq2(x,y):
    ddyeq2 = 1.0
    return(ddyeq2)

def func(x,y):
    func  = [0.0 for i in range(2)] # null list
    # build the function
    func[0] = eq1(x,y)
    func[1] = eq2(x,y)
    return(func)

def jacob(x,y):
    jacob = [[0.0 for j in range(2)] for i in range(2)] # constructed list  
    #build the  jacobian
    jacob[0][0]=ddxeq1(x,y)
    jacob[0][1]=ddyeq1(x,y)
    jacob[1][0]=ddxeq2(x,y)
    jacob[1][1]=ddyeq2(x,y)
    return(jacob)


# Next we create vectors to store values, and supply initial guesses to the system, and echo the inputs.

# In[2]:


deltax  = [0.0 for i in range(2)] # null list
xguess  = [0.0 for i in range(2)] # null list
myfunc  = [0.0 for i in range(2)] # null list
myjacob = [[0.0 for j in range(2)] for i in range(2)] # constructed list  
# supply initial guess
xguess[0] = float(input("Value for x : "))
xguess[1] = float(input("Value for y : "))
# build the initial function
myfunc = func(xguess[0],xguess[1])
#build the initial jacobian
myjacob=jacob(xguess[0],xguess[1])
#write initial results
writeV(xguess,2,"Initial X vector ")
writeV(myfunc,2,"Initial FUNC vector ")
writeM(myjacob,2,2,"Initial Jacobian ")
# solver parameters
tolerancef = 1.0e-9
tolerancex = 1.0e-9


# Now we apply the algorithm a few times, here the count is set to 10. So eneter the loop, test for stopping, then update.

# In[3]:


# Newton-Raphson
for iteration in range(10):
    myfunc = func(xguess[0],xguess[1])
    testf = vdotv(myfunc,myfunc,2)
    if testf <= tolerancef :
        print("f(x) close to zero\n test value : ", testf)
        break
    myjacob=jacob(xguess[0],xguess[1])
    deltax=linearsolver(myjacob,myfunc)
    testx = vdotv(deltax,deltax,2)
    if testx <= tolerancex :
        print("solution change small\n test value : ", testx)
        break
    xguess=vvsub(xguess,deltax,2)
##    print("iteration : ",iteration)
##    writeV(xguess,2,"Current X vector ")
##    writeV(myfunc,2,"Current FUNC vector ")
print("Exiting Iteration : ",iteration)
writeV(xguess,2,"Exiting X vector ")
writeV(myfunc,2,"Exiting FUNC vector ")


# ## Quasi-Newton Method using Finite Difference Approximations for the Derivative
# The next variant is to approximate the derivatives -- usually a Finite-Difference approximation is used, either forward, backward, or centered differences -- generally determined based on the actual behavior of the functions themselves or by trial and error. 
# 
# For really huge systems, we usually make the program itself make the adaptions as it proceeds.
# 
# The coding for a finite-difference representation of a Jacobian is shown in Listing that follows 
# In constructing the Jacobian, we observe that each column of the Jacobian is simply the directional derivative of the function with respect to the variable associated with the column.  
# For instance, the first column of the Jacobian in the example is first derivative of the first function (all rows) with respect to the first variable, in this case $x$.  The second column is the first derivative of the second function with respect to the second variable, $y$.  
# This structure is useful to generalize the Jacobian construction method because we could write (yet another) prototype function that can take the directional derivatives for us, and just insert the returns as columns; in the example we simply modified the `ddx` and `ddy` functions from analytical to simple finite differences.
# 
# The example listing is specific to the 2X2 function in the example, but the extension to more general cases is evident.
# 

# In[16]:


#################################################################
# Newton Solver Example -- Numerical Derivatives               #
#################################################################
import math   # This will import math module from python distribution
from LinearSolverPivot import linearsolver # This will import our solver module
from vector_matrix_lib import writeM,writeV,vdotv,vvsub # This will import our vector functions

def eq1(x,y):
    eq1 = x**2 + y**2 - 4.0
    return(eq1)

def eq2(x,y):
    eq2 = math.exp(x) + y - 1.0
    return(eq2)
##############################################################
# This portion is changed for finite-difference method to evaluate derivatives #
##############################################################
def ddxeq1(x,y):
    delta = 1.0e-6
    ddxeq1 = (eq1(x+delta,y)-eq1(x,y))/delta
    return(ddxeq1)

def ddyeq1(x,y):
    delta = 1.0e-6
    ddyeq1 = (eq1(x,y+delta)-eq1(x,y))/delta
    return(ddyeq1)

def ddxeq2(x,y):
    delta = 1.0e-6
    ddxeq2 = (eq2(x+delta,y)-eq2(x,y))/delta
    return(ddxeq2)

def ddyeq2(x,y):
    delta = 1.0e-6
    ddyeq2 = (eq2(x,y+delta)-eq2(x,y))/delta
    return(ddyeq2)
##############################################################
def func(x,y):
    func  = [0.0 for i in range(2)] # null list
    # build the function
    func[0] = eq1(x,y)
    func[1] = eq2(x,y)
    return(func)

def jacob(x,y):
    jacob = [[0.0 for j in range(2)] for i in range(2)] # constructed list  
    #build the  jacobian
    jacob[0][0]=ddxeq1(x,y)
    jacob[0][1]=ddyeq1(x,y)
    jacob[1][0]=ddxeq2(x,y)
    jacob[1][1]=ddyeq2(x,y)
    return(jacob)
deltax  = [0.0 for i in range(2)] # null list
xguess  = [0.0 for i in range(2)] # null list
myfunc  = [0.0 for i in range(2)] # null list
myjacob = [[0.0 for j in range(2)] for i in range(2)] # constructed list  
# supply initial guess
xguess[0] = float(input("Value for x : "))
xguess[1] = float(input("Value for y : "))
# build the initial function
myfunc = func(xguess[0],xguess[1])
#build the initial jacobian
myjacob=jacob(xguess[0],xguess[1])
#write initial results
writeV(xguess,2,"Initial X vector ")
writeV(myfunc,2,"Initial FUNC vector ")
writeM(myjacob,2,2,"Initial Jacobian ")
# solver parameters
tolerancef = 1.0e-9
tolerancex = 1.0e-9
# Newton-Raphson
for iteration in range(10):
    myfunc = func(xguess[0],xguess[1])
    testf = vdotv(myfunc,myfunc,2)
    if testf <= tolerancef :
        print("f(x) close to zero\n test value : ", testf)
        break
    myjacob=jacob(xguess[0],xguess[1])
    deltax=linearsolver(myjacob,myfunc)
    testx = vdotv(deltax,deltax,2)
    if testx <= tolerancex :
        print("solution change small\n test value : ", testx)
        break
    xguess=vvsub(xguess,deltax,2)
##    print("iteration : ",iteration)
##    writeV(xguess,2,"Current X vector ")
##    writeV(myfunc,2,"Current FUNC vector ")
print("Exiting Iteration : ",iteration)
writeV(xguess,2,"Exiting X vector ")
writeV(myfunc,2,"Exiting FUNC vector using Finite-Differences")


# In[ ]:





# ## Exercises
# 
# Write a script that forward defines the multi-variate functions and implements the Newton-Raphson technique.
# Implement the method, using analytical derivatives, and find a solution to:
# \begin{gather}
# \begin{matrix}
#  x^3 & +~3y^2 & = 21\\
# x^2& +~2y  & = -2 \\
# \end{matrix}
# \end{gather}
# 
# Repeat the exercise, except use finite-differences to approximate the derivatives.

# In[ ]:





# Write a script that forward defines the multi-variate functions and implements the Newton-Raphson technique.
# Implement the method, using analytical derivatives, and find a solution to:
# \begin{gather}
# \begin{matrix}
# x^2 & +~ y^2 & +~z^2 & =~ 9\\
# ~ & ~ & xyz & =~ 1\\
# x & +~ y & -z^2 & =~ 0\\
# \end{matrix}
# \end{gather}
# 
# Repeat the exercise, except use finite-differences to approximate the derivatives.

# In[ ]:





# Write a script that forward defines the multi-variate functions and implements the Newton-Raphson technique.
# Implement the method, using analytical derivatives, and find a solution to:
# \begin{gather}
# \begin{matrix}
# xyz & -~ x^2 & +~y^2 & =~ 1.34\\
# ~ & xy &-~z^2 & =~ 0.09\\
# e^x & -~ e^y & +z & =~ 0.41\\
# \end{matrix}
# \end{gather}
# 
# Repeat the exercise, except use finite-differences to approximate the derivatives.

# In[ ]:




