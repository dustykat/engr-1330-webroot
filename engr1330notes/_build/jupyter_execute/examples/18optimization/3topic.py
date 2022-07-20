#!/usr/bin/env python
# coding: utf-8

# # Gradient Descent Methods
# 
# ## Steepest Descent
# 
# ## Using Packages
# 
# ## Unconstrained Minimization
# 
# Example problem is 
# 
# $$f(x) = \sum_{i = 1}^{N-1} \:100(x_i - x_{i-1}^{2})$$

# ### Nelder-Mead Method
# 
# - Function calls only
# - Needs a starting vector that is non-degenerate

# 

# In[1]:


import numpy as np
from scipy.optimize import minimize



def rosen(x):
    """The Rosenbrock function"""
    return sum(100.0*(x[1:]-x[:-1]**2.0)**2.0 + (1-x[:-1])**2.0)

x0 = np.array([1.3, 0.7, 0.8, 1.9, 1.2])
res = minimize(rosen, x0, method='nelder-mead',options={'disp': True})

print(res.x)


# ### Powell's Direction Set Method
# 
# - Function calls only
# - Needs a starting vector that is non-degenerate

# In[2]:


import numpy as np
from scipy.optimize import minimize



def rosen(x):
    """The Rosenbrock function"""
    return sum(100.0*(x[1:]-x[:-1]**2.0)**2.0 + (1-x[:-1])**2.0)

x0 = np.array([1.3, 0.7, 0.8, 1.9, 1.2])
res = minimize(rosen, x0, method='powell',options={'disp': True})

print(res.x)


# In[3]:


def rosen(x):
    nminus1 = len(x)-1
    acc = 0.0
    for i in range(nminus1):
        acc = acc + 100*(x[i+1]-x[i]**2)
    return acc


# In[4]:


import numpy as np
from scipy.optimize import minimize


#Rosenbrock Function
def fun_rosenbrock(x):
    return np.array([10 * (x[1] - x[0]**2), (1 - x[0])])
   
from scipy.optimize import least_squares
input = np.array([2, 2])
res = least_squares(fun_rosenbrock, input)

print(res)


# In[5]:


def rosen_der(x):

    xm = x[1:-1]

    xm_m1 = x[:-2]

    xm_p1 = x[2:]

    der = np.zeros_like(x)

    der[1:-1] = 200*(xm-xm_m1**2) - 400*(xm_p1 - xm**2)*xm - 2*(1-xm)

    der[0] = -400*x[0]*(x[1]-x[0]**2) - 2*(1-x[0])

    der[-1] = 200*(x[-1]-x[-2]**2)

    return der

from scipy.optimize import Bounds

bounds = Bounds([0, -0.5], [1.0, 2.0])

ineq_cons = {'type': 'ineq',

             'fun' : lambda x: np.array([1 - x[0] - 2*x[1],

                                         1 - x[0]**2 - x[1],

                                         1 - x[0]**2 + x[1]]),

#             'jac' : lambda x: np.array([[-1.0, -2.0],

#                                         [-2*x[0], -1.0],

#                                         [-2*x[0], 1.0]])
            }

eq_cons = {'type': 'eq',

           'fun' : lambda x: np.array([2*x[0] + x[1] - 1]),

#           'jac' : lambda x: np.array([2.0, 1.0])
          }

x0 = np.array([0.5, 0])

res = minimize(rosen, x0, method='SLSQP', jac="2-point",

               constraints=[eq_cons, ineq_cons], options={'ftol': 1e-9, 'disp': True},

               bounds=bounds)


# In[6]:


res


# In[ ]:




