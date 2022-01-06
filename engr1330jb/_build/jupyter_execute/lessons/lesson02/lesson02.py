#!/usr/bin/env python
# coding: utf-8

# <div class="alert alert-block alert-info">
#     <b><h1>ENGR 1330 Computational Thinking with Data Science </h1></b> 
# </div> 
# 
# Copyright © 2021 Theodore G. Cleveland and Farhang Forghanparast
# 
# Last GitHub Commit Date: 12 August 2021
#     
# # 2: Expressions
# - fundamental operators
# - arithmetic expressions
# - simple output: print()

# ## Programming Fundamentals
# 
# Recall the 5 fundamental CT concepts are:
# 
# 1. **Decomposition**: the process of taking a complex problem and breaking it into more manageable sub-problems. 
# 2. **Pattern Recognition**: finding similarities, or shared characteristics of problems to reuse of solution methods ( **automation** ) for each occurrence of the pattern. 
# 3. **Abstraction** : Determine important characteristics of the problem and use these characteristics to create a representation of the problem. 
# 4. **Algorithms** : Step-by-step instructions of how to solve a problem.
# 5. **System Integration**: the assembly of the parts above into the complete (integrated) solution.  Integration combines parts into a **program** which is the realization of an algorithm using a syntax that the computer can understand. 
# 
# **Programming** is (generally) writing code in a specific programming language to address a certain problem. In the above list it is largely addressed by the algorithms and system integration concepts.
# 
# 
# ### iPython
# The programming language we will use is Python (actually iPython). Python is an example of a high-level language; there are also low-level languages, sometimes referred to as machine languages or assembly languages. Machine language is the encoding of instructions in binary so that they can be directly executed by the computer. Assembly language uses a slightly easier format to refer to the low level instructions. Loosely speaking, computers can only execute programs written in low-level languages. To be exact, computers can actually only execute programs written in machine language. Thus, programs written in a high-level language (and even those in assembly language) have to be processed before they can run. This extra processing takes some time, which is a small disadvantage of high-level languages. However, the advantages to high-level languages are enormous:
# 
# - First, it is much easier to program in a high-level language. Programs written in a high-level language take less time to write, they are shorter and easier to read, and they are more likely to be correct. 
# - Second, high-level languages are portable, meaning that they can run on different kinds of computers with just a  few modifications. 
# - Low-level programs can run on only one kind of computer (chipset-specific for sure, in some cases hardware specific) and have to be rewritten to run on other processors. (e.g. x86-64 vs. arm7 vs. aarch64 vs. PowerPC ...)
# 
# Due to these advantages, almost all programs are written in high-level languages. Low-level languages are used only for a few specialized applications.
# 
# Two kinds of programs process high-level languages into low-level languages: interpreters and compilers. An interpreter reads a high-level program and executes it, meaning that it does what the program says. It processes the program a little at a time, alternately reading lines and performing computations.  Recall how an Excel spreadsheet computes from top to bottom, left to right - an interpreted program is much the same, each line is like a cell in a spreadsheet.
# 
# As a language, python is a formal language that has certain requirements and structure called "syntax." Syntax rules come in two flavors, pertaining to **tokens** and **structure**. **Tokens** are the basic elements of the language, such as words, numbers, and chemical elements. The second type of syntax rule pertains to the **structure of a statement** specifically in the way the tokens are arranged. 

# ## Tokens and Structure
# 
# Consider the relativistic equation relating energy, mass, and the speed of light 
# $ e = m \cdot c^2 $
# 
# In this equation the tokens are $e$,$m$,$c$,$=$,$\cdot$,$~^2$ and the structure is parsed from left to right as into the token named $e$ place the result of the product of the contents of the tokens $m$ and $c \times c$ (this operation on $c$ is what the $~^2$ token means. Given that the speed of light is some universal constant, the only things that can change are the contents of $m$ and the resulting change in $e$.  
# 
# In the above discourse, the tokens $e$,$m$,$c$ are names for things that can have values -- we will call these variables (or constants as appropriate).  The tokens $=$,$\cdot$, and $~^2$ are symbols for various arithmetic operations -- we will call these operators.  The structure of the equation is specific -- we will call it a statement.
# 
# :::{note}
# When we attempt to write and execute python scripts - we will make various mistakes; these will generate warnings and errors, which we will repair to make a working program.
# 
# The next two code blocks do not compile into a JupyterBook, we will see in class why.  The cells can be cut-and-pasted into your Jupyter Notebook
# :::
# 
# Consider our equation:

# ```
# #clear all variables# Example 
# Energy = Mass * SpeedOfLight**2 
# ```

# Notice how the interpreter tells us that Mass is undefined - so a simple fix is to define it and try again

# ```
# # Example 
# Mass = 1000000
# Energy = Mass * SpeedOfLight**2 
# ```

# Notice how the interpreter now tells us that SpeedOfLight is undefined - so a simple fix is to define it and try again

# In[1]:


# Example 
Mass = 1000000  #kilograms
SpeedOfLight = 299792458  #meters per second
Energy = Mass * SpeedOfLight**2 


# Now the script ran without any reported errors, but we have not instructed the program on how to produce output.  To keep the example simple we will just add a generic print statement.

# In[2]:


# Example 
Mass = 1000000  #kilograms
SpeedOfLight = 299792458  #meters per second
Energy = Mass * SpeedOfLight**2 
print("Energy is:", Energy, "Newton meters")


# Now lets examine our program.  Identify the tokens that have values, Identify the tokens that are symbols of operations, identify the structure.

# ## Variables
# 
# Variables are names given to data that we want to store, manipulate, **and change** in programs. A variable has a name and a value. The value representation depends on what type of object the variable represents. The utility of variables comes in when we have a structure that is universal, but values of variables within the structure will change - otherwise it would be simple enough to just hardwire the arithmetic.
# 
# Suppose we want to store the time of concentration for some hydrologic calculation. 
# To do so, we can name a variable `TimeOfConcentration`, and then `assign` a value to the variable,
# for instance:
# 
#     TimeOfConcentration = 0.0
#     
# After this assignment statement the variable is created in the program and has a value of 0.0. 
# The use of a decimal point in the initial assignment establishes the variable as a float (a real variable is called a floating point representation -- or just a float).
# 
# ### Naming Rules
# 
# Variable names in Python can only contain letters (a - z, A - Z), numerals (0 - 9), or underscores. 
# The first character cannot be a number, otherwise there is considerable freedom in naming. 
# The names can be reasonably long. 
# `runTime`, `run_Time`, `_run_Time2`, `_2runTime` are all valid names, but `2runTime` is not valid, and will create an error when you try to use it.

# In[3]:


# Script to illustrate variable names
runTime = 1.
_2runTime = 2 # change to 2runTime = 2 and rerun script
runTime2 = 2
print(type(runTime),type(_2runTime),type(runTime2))


# There are some reserved words that cannot be used as variable names because they have preassigned meaning in Parseltongue. 
# These words include `print`, `input`, `if`, `while`, and `for`. 
# There are several more; the interpreter won't allow you to use these names as variables and will issue an error message when you attempt to run a program with such words used as variables.

# ## Operators
# 
# The `=` sign used in the variable definition is called an assignment operator (or assignment sign). 
# The symbol means that the expression to the right of the symbol is to be evaluated and the result placed into the variable on the left side of the symbol.  The "operation" is assignment, the "=" symbol is the operator name.
# 
# Consider the script below

# In[4]:


# Assignment Operator
x = 5
y = 10
print (x,y)
y=x # reverse order y=x and re-run, what happens?
print (x,y)


# So look at what happened. When we assigned values to the variables named `x` and `y`, they started life as 5 and 10. 
# We then wrote those values to the console, and the program returned 5 and 10. 
# Then we assigned `y` to `x` which took the value in y and replaced the value that was in x with this value. 
# We then wrote the contents again, and both variables have the value 10.

# ## Arithmetic Operators
# 
# In addition to assignment we can also perform arithmetic operations on variables. The
# fundamental arithmetic operators are:
# 
# | Symbol | Meaning | Example |
# |:---|:---|:---|
# | = |Assignment| x=3 Assigns value of 3 to x.|
# | + |Addition| x+y Adds values in x and y.|
# | - |Subtraction| x-y Subtracts values in y from x.|
# | * |Multiplication| x*y Multiplies values in x and y.|
# | / |Division| x/y Divides value in x by value in y.|
# | // |Floor division| x//y Divide x by y, truncate result to whole number.|
# | % |Modulus| x%y Returns remainder when x is divided by y.|
# | ** |Exponentation| x ** y Raises value in x by value in y. ( e.g. x ** y)|
# | += |Additive assignment| x+=2 Equivalent to x = x+2.|
# | -= |Subtractive assignment| x-=2 Equivalent to x = x-2.|
# | *= |Multiplicative assignment| x\*=3 Equivalent to x = x\*3.|
# | /= |Divide assignment| x/=3 Equivalent to x = x/3.|
# 
# Run the script in the next cell for some illustrative results

# In[5]:


# Uniary Arithmetic Operators
x = 10
y = 5
print(x, y)
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print((x+1)//y)
print((x+1)%y)
print(x**y)


# In[6]:


# Arithmetic assignment operators
x = 1
x += 2
print(type(x),x)
x = 1
x -= 2
print(type(x),x)
x = 1
x *=3
print(type(x),x)
x = 10
x /= 2
print(type(x),x)  # Interesting what division does to variable type


# ## Expressions
# 
# Expressions are the "algebraic" constructions that are evaluated and then placed into a variable.
# Consider
# 
#     x1 = 7 + 3 * 6 / 2 - 1
# 
# The expression is evaluated from the left to right and in words is
# 
# - Into the object named x1 place the result of:
#     
#   integer 7 + (integer 6 divide by integer 2 = float 3 * integer 3 = float 9 - integer 1 = float 8) = float 15
# 
# The division operation by default produces a float result unless forced otherwise.  The result is the variable `x1` is a float with a value of `15.0`

# In[7]:


# Expressions Example
x1 = 7 + 3 * 6 // 2 - 1  # Change / into // and see what happens!
print(type(x1),x1)
## Simple I/O (Input/Output)


# ### Summary
# 
# So far consider our story - a tool to help with problem solving is CT leading to an algorithm.  The tool to implement the algorithm is the program and in our case JupyterLab running iPython interpreter for us.
# 
# As a formal language we introduced:
# - tokens
# - structure
# 
# From these two constructs we further introduced **variables** (a kind of token), **data types** (an abstraction, and arguably a decomposition), and **expressions** (a structure).  We created simple scripts (with errors), examined the errors, corrected our script, and eventually got an answer.  So we are well on our way in CT as it applies in Engineering.

# ## References
# 
# 1. Computational and Inferential Thinking Ani Adhikari and John DeNero, Computational and Inferential Thinking, The Foundations of Data Science, Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND) Chapter 3 [https://www.inferentialthinking.com/chapters/03/programming-in-python.html](https://www.inferentialthinking.com/chapters/03/programming-in-python.html)
# 
# 3. Learn Python in One Day and Learn It Well. Python for Beginners with Hands-on Project. (Learn Coding Fast with Hands-On Project Book -- Kindle Edition by LCF Publishing (Author), Jamie Chan [https://www.amazon.com/Python-2nd-Beginners-Hands-Project-ebook/dp/B071Z2Q6TQ/ref=sr_1_3?dchild=1&keywords=learn+python+in+a+day&qid=1611108340&sr=8-3](https://www.amazon.com/Python-2nd-Beginners-Hands-Project-ebook/dp/B071Z2Q6TQ/ref=sr_1_3?dchild=1&keywords=learn+python+in+a+day&qid=1611108340&sr=8-3)

# ---
# 
# ## Laboratory 2
# 
# **Examine** (click) Laboratory 0 as a webpage at [Laboratory 2.html](http://54.243.252.9/engr-1330-webroot/8-Labs/Lab02/Lab02.html)
# 
# **Download** (right-click, save target as ...) Laboratory 0 as a jupyterlab notebook from [Laboratory 2.ipynb](http://54.243.252.9/engr-1330-webroot/8-Labs/Lab02/Lab02.ipynb)
# 

# <hr><hr>
# 
# ## Exercise Set 2
# 
# **Examine** (click) Exercise Set 0 as a webpage at [Exercise 2.html](http://54.243.252.9/engr-1330-webroot/8-Labs/Lab02/Lab02-TH.html)
# 
# **Download** (right-click, save target as ...) Exercise Set 0 as a jupyterlab notebook at  [Exercise Set 2.ipynb](http://54.243.252.9/engr-1330-webroot/8-Labs/Lab02/Lab02-TH.ipynb)
# 
# 

# In[ ]:




