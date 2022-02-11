#!/usr/bin/env python
# coding: utf-8

# <div class="alert alert-block alert-info">
#     <b><h1>ENGR 1330 Computational Thinking with Data Science </h1></b> 
# </div> 
# 
# Copyright © 2022 Theodore G. Cleveland and Farhang Forghanparast
# 
# Last GitHub Commit Date: Never
#     
# # 10: Vector/Matrix applications (Under Construction)
# - curve-fitting
# - linear heat flow
# - network flow (Optional; Non-linear System of equations)
# 

# In[ ]:





# ## Nonlinear Systems of Equations (Optional)
# 
# Non-linear systems are extensions of the linear systems cases except the systems involve products and powers of the unknown variables. Non-linear problems are often quite difficult to manage, especially when the systems are large (many rows and many variables).
# The solution to non-linear systems, if non-trivial or even possible, are usually iterative. Within the iterative steps is a linearization component – these linear systems which are intermediate computations within the overall solution process are treated by an appropriate linear system method (direct or iterative).
# Consider the system below:
# 
# $
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
# $
# 
# Suppose we have a solution guess $x_{k},y_{k}$, which of course could be wrong, but we could linearize about that guess as
# 
# $
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
# $
# 
# Now if we assemble the system in the usual fashion, $\mathbf{A} \cdot \mathbf{x_{k+1}} = ~ \mathbf{b}~$ we have a system of linear equations (Linear in $\mathbf{x_{k+1}}$}), which expanded look like:
# 
# $
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
# $
# 
# Now that the system is linear, and we can solve for $\mathbf{x_{k+1}}$ using our linear system solver for the new guess.
# If the system is convergent (not all are) then if we update, and repeat  we will eventually find a result.
# 
# What one really needs is a way to construct the linear system that has a systematic update method, that is discussed below

# ```{note}
# The examples below use two user-defined modules listed below.  Use of user-defined modules is discussed in the lesson on functions
# 
# ```
# 
# ```
# > LinearSolverPivot.py
# 
# # SolveLinearSystem.py
# # Code to read A and b
# # Then solve Ax = b for x by Gaussian elimination with back substitution
# #
# ##########
# def linearsolver(A,b):
#     n = len(A)
# #    M = A  #this is object to object equivalence
# # copy A into M element by element
#     M=[[0.0 for jcol in range(n)]for irow in range(n)]
#     for irow in range(n):
#         for jcol in range(n):
#             M[irow][jcol]=A[irow][jcol]
# 
# 
#     i = 0
#     for x in M:
#      x.append(b[i])
#      i += 1
# 
#     for k in range(n):
#      for i in range(k,n):
#        if abs(M[i][k]) > abs(M[k][k]):
#           M[k], M[i] = M[i],M[k]
#        else:
#           pass
# 
#      for j in range(k+1,n):
#          q = float(M[j][k]) / M[k][k]
#          for m in range(k, n+1):
#             M[j][m] -=  q * M[k][m]
# 
#     x = [0 for i in range(n)]
# 
#     x[n-1] =float(M[n-1][n])/M[n-1][n-1]
#     for i in range (n-1,-1,-1):
#       z = 0
#       for j in range(i+1,n):
#           z = z  + float(M[i][j])*x[j]
#       x[i] = float(M[i][n] - z)/M[i][i]
# #    print (x)
#     return(x)
# #
# ```
# 
# ```
# > vector_matrix_lib.py
# 
# # vector_matrix_lib.py
# # useful linear algebra tools
# import math   # This will import math module
# 
# def writeM(M,ir,jc,label):
#     print ("------",label,"------")
#     for i in range(0,ir,1):
#         print (M[i][0:jc])
#     print ("-----------------------------")
#     #return
# 
# def writeV(V,ir,label):
#     print ("------",label,"------")
#     for i in range(0,ir,1):
#         print (V[i])
#     print ("-----------------------------")
#     #return
# 
# def mmmult(amatrix,bmatrix,rowNumA,colNumA,rowNumB,colNumB):
#     AB =[[0.0 for j in range(colNumB)] for i in range(rowNumA)]
#     for i in range(0,rowNumA):
#         for j in range(0,colNumB):
#             for k in range(0,colNumA):
#                 AB[i][j]=AB[i][j]+amatrix[i][k]*bmatrix[k][j]
#     return(AB)
# 
# def mvmult(amatrix,xvector,rowNumA,colNumA):
#     bvector=[0.0 for i in range(rowNumA)]
#     for i in range(0,rowNumA):
#         for j in range(0,1):
#             for k in range(0,colNumA):
#                 bvector[i]=bvector[i]+amatrix[i][k]*xvector[k]
#     return(bvector)
# 
# def vvadd(avector,bvector,length):
#     aplusb=[0.0 for i in range(length)]
#     for i in range(length):
#         aplusb[i] = avector[i] + bvector[i]
#     return(aplusb)
# 
# def vvsub(avector,bvector,length):
#     aminusb=[0.0 for i in range(length)]
#     for i in range(length):
#         aminusb[i] = avector[i] - bvector[i]
#     return(aminusb)
# 
# def vdotv(avector,bvector,length):
#     adotb=0.0
#     for i in range(length):
#         adotb=adotb+avector[i]*bvector[i]
#     return(adotb)
# ```
# 

# ### Multiple-variable extension of Newton’s Method
# 
# This section presents the Newton-Raphson method as a way to sometimes solve systems of non-linear equations.
# 
# Consider an example where the function $\textbf{f}$ is a vector-valued function of a vector argument.
# 
# $
# \begin{gather}
# \mathbf{f(x)} = 
# \begin{matrix}
# f_1 = & x^2 & +~y^2 & - 4\\
# f_2 = & e^x & +~y  & - 1\\
# \end{matrix}
# \end{gather}
# $
# 
# Let's also recall Newtons method for scalar valued function of a single variable.
# 
# $
# \begin{equation}
# x_{k+1}=x_{k} - \frac{  f(x_{k})  }{   \frac{df}{dx}\rvert_{x_k} } 
# \label{eqn:NewtonFormula}
# \end{equation}
# $
# 
# When extending to higher dimensions, the analog for $x$ is the vector $\textbf{x}$ and the analog for the function $f()$ is the vector function $\textbf{f()}$.
# What remains is an analog for the first derivative in the denominator (and the concept of division of a matrix).
# 
# The analog to the first derivative is a matrix called the Jacobian which is comprised of the first derivatives of the function $\textbf{f}$ with respect to the arguments $\textbf{x}$.   
# For example for a 2-value function of 2 arguments (as our example above)
# 
# $
# \begin{equation}
# \frac{df}{dx}\rvert_{x_k} =>
# \begin{pmatrix}
# \frac{\partial f_1}{\partial x_1} & \frac{\partial f_1}{\partial x_2} \\
# ~ & ~ \\
# \frac{\partial f_2}{\partial x_1} & \frac{\partial f_2}{\partial x_2} \\
# \end{pmatrix}
# \label{eqn:Jacobian}
# \end{equation}
# $
# 
# Next recall that division is replaced by matrix multiplication with the multiplicative inverse, so the analogy continues as
# 
# $
# \begin{equation}
# \frac{1}{\frac{df}{dx}\rvert_{x_k}} =>
# {\begin{pmatrix}
# \frac{\partial f_1}{\partial x_1} & \frac{\partial f_1}{\partial x_2} \\
# ~ & ~ \\
# \frac{\partial f_2}{\partial x_1} & \frac{\partial f_2}{\partial x_2} \\
# \end{pmatrix}}^{-1}
# \label{eqn:JacobianInverse}
# \end{equation}
# $
# 
# Let's name the Jacobian $\textbf{J(x)}$.
# 
# So the multi-variate Newton's method can be written as
# 
# $
# \begin{equation}
# \mathbf{x}_{k+1}=\mathbf{x}_{k} - \mathbf{J(x)}^{-1}\rvert_{x_k} \cdot \mathbf{f(x)}\rvert_{x_k}
# \label{eqn:VectorNewtonFormula}
# \end{equation}
# $

# In the linear systems lessons we did find a way to solve for an inverse, but it's not necessary, and is computationally expensive to invert in these examples -- a series of rearrangement of the system above yields a nice scheme that does not require inversion of a matrix.
# 
# First, move the $\mathbf{x}_{k}$ to the left-hand side.
# 
# $
# \begin{equation}
# \mathbf{x}_{k+1}-\mathbf{x}_{k} = - \mathbf{J(x)}^{-1}\rvert_{x_k} \cdot \mathbf{f(x)}\rvert_{x_k}
# \end{equation}
# $
# 
# Next multiply both sides by the Jacobian (The Jacobian must be non-singular otherwise we are dividing by zero)
# 
# $
# \begin{equation}
# \mathbf{J(x)}\rvert_{x_k} \cdot (\mathbf{x}_{k+1}-\mathbf{x}_{k}) = - \mathbf{J(x)}\rvert_{x_k} \cdot \mathbf{J(x)}^{-1}\rvert_{x_k} \cdot \mathbf{f(x)}\rvert_{x_k}
# \end{equation}
# $
# 
# Recall a matrix multiplied by its inverse returns the identity matrix (the matrix equivalent of unity)
# 
# $
# \begin{equation}
# -\mathbf{J(x)}\rvert_{x_k} \cdot (\mathbf{x}_{k+1}-\mathbf{x}_{k}) = \mathbf{f(x)}\rvert_{x_k}
# \end{equation}
# $
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

# ### Example using Analytical Derivatives
# 
# Now to complete the example we will employ this algorithm.
# 
# The function (repeated)
# 
# $
# \begin{gather}
# \mathbf{f(x)} = 
# \begin{matrix}
# f_1 = & x^2 & +~y^2 & - 4\\
# f_2 = & e^x & +~y  & - 1\\
# \end{matrix}
# \end{gather}
# $
# 
# Then the Jacobian, here we will compute it analytically because we can
# 
# $
# \begin{equation}
# \mathbf{J(x)}=>
# {\begin{pmatrix}
# 2x & 2y \\
# ~ & ~ \\
# e^x & 1 \\
# \end{pmatrix}}
# \end{equation}
# $
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
xguess[0]=1.0 ; xguess[1]=0.0
#xguess[0] = float(input("Value for x : "))
#xguess[1] = float(input("Value for y : "))
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


# ### Quasi-Newton Method using Finite Difference Approximations for the Derivative
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

# In[4]:



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
# xguess[0] = float(input("Value for x : "))
# xguess[1] = float(input("Value for y : "))
xguess[0]=1.0 ; xguess[1]=0.0
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





# ### Exercises
# 
# Write a script that forward defines the multi-variate functions and implements the Newton-Raphson technique.
# Implement the method, using analytical derivatives, and find a solution to:
# 
# $
# \begin{gather}
# \begin{matrix}
#  x^3 & +~3y^2 & = 21\\
# x^2& +~2y  & = -2 \\
# \end{matrix}
# \end{gather}
# $
# 
# Repeat the exercise, except use finite-differences to approximate the derivatives.

# In[ ]:





# Write a script that forward defines the multi-variate functions and implements the Newton-Raphson technique.
# Implement the method, using analytical derivatives, and find a solution to:
# 
# $
# \begin{gather}
# \begin{matrix}
# x^2 & +~ y^2 & +~z^2 & =~ 9\\
# ~ & ~ & xyz & =~ 1\\
# x & +~ y & -z^2 & =~ 0\\
# \end{matrix}
# \end{gather}
# $
# 
# Repeat the exercise, except use finite-differences to approximate the derivatives.

# In[ ]:





# Write a script that forward defines the multi-variate functions and implements the Newton-Raphson technique.
# Implement the method, using analytical derivatives, and find a solution to:
# 
# $
# \begin{gather}
# \begin{matrix}
# xyz & -~ x^2 & +~y^2 & =~ 1.34\\
# ~ & xy &-~z^2 & =~ 0.09\\
# e^x & -~ e^y & +z & =~ 0.41\\
# \end{matrix}
# \end{gather}
# $
# 
# Repeat the exercise, except use finite-differences to approximate the derivatives.

# ## Application of Non-Linear Solvers:  Pipeline Network Simulation
# 
# ```{note}
# The network simulator uses input files to convey the network to the program These files are listed below.
# ```
# 
# > PipeNetwork.txt
# ```
# 8
# 11
# 200 200 200 200 200 200 200 200
# 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 
# 300 300 300 300 150 300 150 150 300 150 300
# 0.00001 0.00001 0.00001 0.00001 0.00001 0.00001 0.00001 0.00001 0.00001 0.00001 0.00001
# 0.000011
# 1 1 1 1 1 1 1 1 1 1 1
# -1 0 0 0 0 -1 0 0 0 0 1
# 1 -1 0 -1 0 0 0 0 0 0 0
# 0 1 -1 0 0 0 0 0 0 0 0
# 0 0 0 0 1 1 -1 0 0 0 0
# 0 0 0 1 -1 0 0 0 -1 0 0
# 0 0 0 0 0 0 1 -1 0 0 0
# 0 0 0 0 0 0 0 1 1 1 0
# 0 0 1 0 0 0 0 0 0 -1 0
# 0 0 0 0 0 0 0 10 0 0 0 0 0 0 0 0 0 0 -300
# 
# ```

# In[5]:


#Pipe Network Simulation


# In[6]:


# Hydraulic Functions


# In[7]:


# hydraulic elements prototype functions
# Jain Friction Factor Function -- Tested OK 23SEP16
import math   # This will import math module

def friction_factor(roughness,diameter,reynolds):
    temp1 = roughness/(3.7*diameter)
    temp2 = 5.74/(reynolds**(0.9))
    temp3 = math.log10(temp1+temp2)
    temp3 = temp3**2
    friction_factor = 0.25/temp3
    return(friction_factor)

# Velocity Function
def velocity(diameter,discharge):
    velocity=discharge/(0.25*math.pi*diameter**2)
    return(velocity)

# Reynolds Number Function  
def reynolds_number(velocity,diameter,mu):
    reynolds_number = abs(velocity)*diameter/mu
    return(reynolds_number)

# Geometric factor function
def k_factor(howlong,diameter,gravity):
    k_factor = (16*howlong)/(2.0*gravity*math.pi**2*diameter**5)
    return(k_factor)


# In[8]:


# Linear Solver with Pivoting 


# In[9]:


# SolveLinearSystem.py
# Code to read A and b
# Then solve Ax = b for x by Gaussian elimination with back substitution
#
##########
def linearsolver(A,b):
    n = len(A)
#    M = A  #this is object to object equivalence
# copy A into M element by element - to operate on M without destroying A
    M=[[0.0 for jcol in range(n)]for irow in range(n)]
    for irow in range(n):
        for jcol in range(n):
            M[irow][jcol]=A[irow][jcol]

#
    i = 0
    for x in M:
     x.append(b[i])
     i += 1

    for k in range(n):
     for i in range(k,n):
       if abs(M[i][k]) > abs(M[k][k]):
          M[k], M[i] = M[i],M[k]
       else:
          pass

     for j in range(k+1,n):
         q = float(M[j][k]) / M[k][k]
         for m in range(k, n+1):
            M[j][m] -=  q * M[k][m]

    x = [0 for i in range(n)]

    x[n-1] =float(M[n-1][n])/M[n-1][n-1]
    for i in range (n-1,-1,-1):
      z = 0
      for j in range(i+1,n):
          z = z  + float(M[i][j])*x[j]
      x[i] = float(M[i][n] - z)/M[i][i]
#    print (x)
    return(x)
#


# In[10]:


# Vector and Matrix Operations Support 


# In[11]:


def writeM(M,ir,jc,label):
    print ("------",label,"------")
    for i in range(0,ir,1):
        print (M[i][0:jc])
    print ("-----------------------------")
    return()

def writeV(V,ir,label):
    print ("------",label,"------")
    for i in range(0,ir,1):
        print (V[i])
    print ("-----------------------------")
    return()

def matrixmatrixmult(amatrix,bmatrix,rowNumA,colNumA,rowNumB,colNumB):
    AB =[[0.0 for j in range(colNumB)] for i in range(rowNumA)]
    for i in range(0,rowNumA):
        for j in range(0,colNumB):
            for k in range(0,colNumA):
                AB[i][j]=AB[i][j]+amatrix[i][k]*bmatrix[k][j]
    return(AB)

def matrixvectormult(amatrix,xvector,rowNumA,colNumA):
    bvector=[0.0 for i in range(rowNumA)]
    for i in range(0,rowNumA):
        for j in range(0,1):
            for k in range(0,colNumA):
                bvector[i]=bvector[i]+amatrix[i][k]*xvector[k]
    return(bvector)

def vectoradd(avector,bvector,length):
    cvector=[]
    for i in range(length):
        cvector.append(avector[i]+bvector[i])
    return(cvector)

def vectorsub(avector,bvector,length):
    cvector=[]
    for i in range(length):
        cvector.append(avector[i]-bvector[i])
    return(cvector)
             
def vdotv(avector,bvector,length):
    adotb=0.0
    for i in range(length):
        adotb=adotb+avector[i]*bvector[i]
    return(adotb)


# In[ ]:





# In[12]:


bvector = []
rowNumA = 0
colNumA = 0
rowNumB = 0
verbose = 'false'
#############################################

elevation = [] # null list node elevations
diameter =  [] # null list pipe diameters
distance =  [] # null list pipe lengths
roughness = [] # null list pipe roughness
flowguess = [] # null list pipe flow rates
nodearcs =  [] # node-arc incidence matrix
rhs_true =  [] # null list for nodal demands
tempvect = []

##############################################
# connect and read file for Pipeline Network #
##############################################
afile = open("PipeNetwork.txt","r")
nnodes = int(afile.readline())
npipes = int(afile.readline())
# read elevation vector
tempvect.append([float(n) for n in afile.readline().strip().split()])
for i in range(0,nnodes,1):
    elevation.append(float(tempvect[0][i]))
tempvect = [] # reset vector
# read diameter vector
tempvect.append([float(n) for n in afile.readline().strip().split()])
for i in range(0,npipes,1):
    diameter.append(float(tempvect[0][i]))
tempvect = [] # reset vector
# read length vector
tempvect.append([float(n) for n in afile.readline().strip().split()])
for i in range(0,npipes,1):
    distance.append(float(tempvect[0][i]))
tempvect = [] # reset vector
# read roughness vector
tempvect.append([float(n) for n in afile.readline().strip().split()])
for i in range(0,npipes,1):
    roughness.append(float(tempvect[0][i]))
tempvect = [] # reset vector
# read viscosity (scalar)
viscosity = float(afile.readline())
# read current flow guess
tempvect.append([float(n) for n in afile.readline().strip().split()])
for i in range(0,npipes,1):
    flowguess.append(float(tempvect[0][i]))
tempvect = [] # reset vector
# read nodearc incidence matrix
## future revisions read directly into augmented matrix, or find way to release nodearc from stack
for irow in range(0,nnodes,1):  # then read each row
    nodearcs.append([float(n) for n in afile.readline().strip().split()])
# read demands guess
tempvect.append([float(n) for n in afile.readline().strip().split()])
for i in range(0,nnodes+npipes,1):
    rhs_true.append(float(tempvect[0][i]))
tempvect = [] # reset vector      
######################################
# end file read ,disconnect file     #
######################################
afile.close() # Disconnect the file
######################################
# echo the input in human readable   #
######################################
print('number of nodes : ',nnodes)
print('number of pipes : ',npipes)
print('viscosity       : ',viscosity)
print ("-----------------------------")
for irow in range(0,nnodes):
    print('node id:',irow, ', elevation :',elevation[irow],' head :',rhs_true[irow+npipes])
print ("-----------------------------")
for jcol in range(0,npipes):
    print('pipe id:',jcol,', diameter : ' ,diameter[jcol],', distance : ',distance[jcol],
          ', roughness : ',roughness[jcol],', flow  : ',flowguess[jcol])
print ("-----------------------------")
##for jcol in range(0,nnodes+npipes):
##    print('irow :',jcol,' RHS True :',rhs_true[jcol])
##print ("-----------------------------")
print("node-arc incidence matrix")
for i in range(0,nnodes,1):
    print (nodearcs[i][0:npipes])
print ("-----------------------------")


# In[ ]:





# In[13]:


# create augmented matrix
colNumA = npipes+nnodes
rowNumA = nnodes+npipes
augmentedMat = [] # null list to store augmented matrix

#######################################################################################
augmentedMat = [[0.0 for j in range(colNumA)]for i in range(rowNumA)] #fill with zeroes
#build upper left partition -- from nodearcs
for ir in range(0,nnodes):
    for jc in range (0,npipes):
        augmentedMat[ir][jc] = nodearcs[ir][jc]
istart=nnodes
iend=nnodes+npipes
jstart=npipes
jend=npipes+nnodes
for ir in range(istart,iend):
    for jc in range (jstart,jend):
        augmentedMat[ir][jc] = -1.0*nodearcs[jc-jstart][ir-istart] + 0.0
if verbose == 'true' :
    print("augmented matrix before loss factors")
    writeM(augmentedMat,rowNumA,colNumA,"augmented matrix")


# In[ ]:





# In[14]:


#######################################################################################
howmany=50 #iterations max
tolerance1 = 1e-24
tolerance2 = 1e-24
velocity_pipe = [0 for i in range(npipes)]  # null list velocities
reynolds      = [0 for i in range(npipes)]  # null list reynolds numbers
friction      = [0 for i in range(npipes)]  # null list friction 
geometry      = [0 for i in range(npipes)]  # null list geometry
lossfactor    = [0 for i in range(npipes)]  # null list loss
jacbMat = [] # null list to store jacobian matrix
jacbMat = [[0.0 for j in range(colNumA)]for i in range(rowNumA)] #fill with zeroes


solvecguess =[ 0.0 for i in range(rowNumA)] 
solvecnew =[ 0.0 for i in range(rowNumA)]
for i in range(0,npipes,1):
    solvecguess[i] = flowguess[i]
    geometry[i] = k_factor(distance[i],diameter[i],32.2)
#solvecguess is a current guess -- wonder if more pythonic way for this assignment
##    print('irow :',i,' Geometry Factor :',geometry[i])
##print ("-----------------------------")


# In[ ]:





# In[15]:


###############################################################
## ITERATION LOOP                                             #
###############################################################
for iteration in range(howmany): # iteration outer loop
    if verbose == 'true' :
        print("solutions at begin of iteration",iteration)
        for jcol in range(0,nnodes+npipes):
            print('irow :',jcol,' solvecnew :',solvecnew[jcol]," solvecguess ",solvecguess[jcol])
        print ("-----------------------------")
    for i in range(0,npipes,1):
        velocity_pipe[i] = velocity(diameter[i],flowguess[i])    
        reynolds[i]=reynolds_number(velocity_pipe[i],diameter[i],viscosity)
        friction[i]=friction_factor(roughness[i],diameter[i],reynolds[i])
        lossfactor[i]=friction[i]*geometry[i]*abs(flowguess[i])
    if verbose == 'true' :
        for jcol in range(0,npipes):
            print('pipe id:',jcol,', velocity : ' ,velocity_pipe[jcol],', reynolds : ',reynolds[jcol],
          ', friction : ',friction[jcol],', loss factor : ',lossfactor[jcol],'flow guess',flowguess[jcol])
################################################################
# BUILD AUGMENTED MATRIX CURRENT Q+H SOLUTION                  #
################################################################
    augmentedMat = [[0.0 for j in range(colNumA)]for i in range(rowNumA)] #fill with zeroes
    #build upper left partition -- from nodearcs
    for ir in range(0,nnodes):
        for jc in range (0,npipes):
            augmentedMat[ir][jc] = nodearcs[ir][jc]
    #build lower right == transpose of upper left
    istart=nnodes
    iend=nnodes+npipes
    jstart=npipes
    jend=npipes+nnodes
    for ir in range(istart,iend):
        for jc in range (jstart,jend):
            augmentedMat[ir][jc] = -1.0*nodearcs[jc-jstart][ir-istart] + 0.0
    # build lower left partition of the matrix
    istart = nnodes
    iend = nnodes+npipes
    jstart = 0
    jend = npipes
    for i in range(istart,iend ):
        for j in range(jstart,jend ):
    #        print('i =',i,'j=',j)
            if (i-istart) == j :
    #            print('i =',i,'j=',j)
                augmentedMat[i][j] = -1.0*lossfactor[j] + 0.0
    if verbose == 'true' :
        print("updated augmented matrix in iteration",iteration)
        writeM(augmentedMat,rowNumA,colNumA,"augmented matrix")
################################################################
# BUILD JACOBIAN MATRIX CURRENT Q+H SOLUTION                   #
################################################################        
    # now build current jacobian
    for i in range(rowNumA):
        for j in range(colNumA):
            jacbMat[i][j] = augmentedMat[i][j]
    # modify lower left partition
    istart = nnodes
    iend = nnodes+npipes
    jstart = 0
    jend = npipes
    for i in range(istart,iend ):
        for j in range(jstart,jend ):
    #        print('i =',i,'j=',j)
            if (i-istart) == j :
    #            print('i =',i,'j=',j)
                jacbMat[i][j] = 2.0*jacbMat[i][j]
##        for jcol in range(0,nnodes+npipes):
##            print('irow :',jcol,' solvecnew :',solvecnew[jcol]," solvecguess ",solvecguess[jcol])
##        print ("-----------------------------")
# matrix multiply augmentedMat*solvecguess to get current g(Q)
#    gq = [0.0 for i in range(rowNumA)] # zero gradient vector
##    if verbose == 'true' :
##        print("augmented matrix in iteration",iteration)
##        writeM(augmentedMat,rowNumA,colNumA,"augmented matrix before mmult")
    gq = matrixvectormult(augmentedMat,solvecguess,rowNumA,colNumA)
##    if verbose == 'true' :
##        writeV(gq,rowNumA,"gq vectorbefore subtract rhs_true")
# subtract rhs
#    for i in range(rowNumA):
    gq = vectorsub(gq,rhs_true,rowNumA)#vector subtract
    if verbose == 'true' :
        print("computed g(q) in iteration",iteration)
        writeV(gq,rowNumA,"gq vector")
        print("compare current and new guess")
        for jcol in range(0,nnodes+npipes):
            print('irow :',jcol,' solvecnew :',solvecnew[jcol]," solvecguess ",solvecguess[jcol])
        print ("-----------------------------")
    dq = [0.0 for i in range(rowNumA)] # zero update vector
    if verbose == 'true' :
        writeV(dq,rowNumA,"dq vector before linear solve")
    if verbose == 'true' :
        print("jacobian before linearsolve in iteration",iteration)
        writeM(jacbMat,rowNumA,colNumA,"jabobian matrix")
    dq = linearsolver(jacbMat,gq) # memory leak after this call - linearsolve clobbers input lists
#    dq = np.linalg.solve(jacbMat,gq)
    if verbose == 'true' :
        print("jacobian after linearsolve in iteration",iteration)
        writeM(jacbMat,rowNumA,colNumA,"jabobian matrix")

    if verbose == 'true' :
        writeV(dq,rowNumA,"dq vector -after linear solve")
    solvecnew = vectorsub(solvecguess,dq,rowNumA)#vector subtract
    if verbose == 'true' :
        print("Q_new = Q_old - DQ")
        writeV(solvecnew,rowNumA,"new guess vector")
#    tempvect =[ 0.0 for i in range(rowNumA)]
##        tempvect = matrixvectormult(jacbMat,dq,rowNumA,colNumA)
##        writeV(tempvect,rowNumA,"J*dq vector")
##        tempvect = vectorsub(tempvect,gq,rowNumA)
##        writeV(tempvect,rowNumA,"J*dq - gq vector")
        print("just after computing new guess, should be different")
        for jcol in range(0,nnodes+npipes):
            print('irow :',jcol,' solvecnew :',solvecnew[jcol]," solvecguess ",solvecguess[jcol])
        print ("-----------------------------")
#test for stopping
    tempvect =[ 0.0 for i in range(rowNumA)]
    for i in range(rowNumA):
        tempvect[i] = abs(solvecnew[i] - solvecguess[i])
    test1 = vdotv(tempvect,tempvect,rowNumA)
    if verbose == 'true' :
        print('test1',test1)
    tempvect =[ 0.0 for i in range(rowNumA)]
    for i in range(rowNumA):
        tempvect[i] = abs(gq[i])
    test2 = vdotv(tempvect,tempvect,rowNumA)
    if verbose == 'true' :
        print('test2',test2)
    if test1 < tolerance1 :
        print("update not changing --exit and report current update")
        print("iteration",iteration)
# update guess
        solvecguess[:] = solvecnew[:]
        for i in range(0,npipes,1):
            flowguess[i] = solvecguess[i]
        break
    if test2 < tolerance2 :
        print("gradient near zero --exit and report current update")
        print("iteration",iteration)
# update guess
        solvecguess[:] = solvecnew[:]
        for i in range(0,npipes,1):
            flowguess[i] = solvecguess[i]
        break
    if verbose == 'true' :
        print("solution continuing")
        print("iteration",iteration)
    # update guess
    solvecguess[:] = solvecnew[:]
    if verbose == 'true' :
        for i in range(0,npipes,1):
            flowguess[i] = solvecguess[i]
        print('number of nodes : ',nnodes)
        print('number of pipes : ',npipes)
        print('viscosity       : ',viscosity)
        print ("-----------------------------")
        for irow in range(0,nnodes):
            print('node id:',irow, ', elevation :',elevation[irow])
        print ("-----------------------------")
        for jcol in range(0,npipes):
            print('pipe id:',jcol,', diameter : ' ,diameter[jcol],', distance : ',distance[jcol],
          ', roughness : ',roughness[jcol],', flow guess : ',flowguess[jcol])
        print ("-----------------------------")
        for jcol in range(0,nnodes+npipes):
            print('irow :',jcol,' RHS True :',rhs_true[jcol],"RHS Current",gq[jcol])
        print ("-----------------------------")
        for jcol in range(0,nnodes+npipes):
            print('irow :',jcol,' solvecnew :',solvecnew[jcol]," solvecguess ",solvecguess[jcol])
        print ("-----------------------------")
# end of outer loop


# In[ ]:





# In[16]:


print("results at iteration = :",iteration)
for i in range(0,npipes,1):
    flowguess[i] = solvecguess[i]
print('number of nodes : ',nnodes)
print('number of pipes : ',npipes)
print('viscosity       : ',viscosity)
print ("-----------------------------")
istart = int(npipes)
for irow in range(0,nnodes):
    print('node id:',irow, ', elevation :',elevation[irow],' head :',solvecnew[irow+npipes])
print ("-----------------------------")
for jcol in range(0,npipes):
    print('pipe id:',jcol,', diameter : ' ,diameter[jcol],', distance : ',distance[jcol],
  ', roughness : ',roughness[jcol],', flow  : ',flowguess[jcol])
print ("-----------------------------")
if verbose == 'true' :
    for jcol in range(0,nnodes+npipes):
        print('irow :',jcol,' RHS True :',rhs_true[jcol],"RHS Current",gq[jcol])
    print ("-----------------------------")
    for jcol in range(0,nnodes+npipes):
        print('irow :',jcol,' solvecnew :',solvecnew[jcol]," solvecguess ",solvecguess[jcol])
    print ("-----------------------------")


# ## References

# In[ ]:




