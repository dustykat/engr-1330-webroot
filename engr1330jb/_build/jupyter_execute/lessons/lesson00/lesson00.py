#!/usr/bin/env python
# coding: utf-8

# <div class="alert alert-block alert-info">
#     <b><h1>ENGR 1330 Computational Thinking with Data Science </h1></b> 
# </div> 
# 
# Copyright © 2021 Theodore G. Cleveland and Farhang Forghanparast
#     
# # 0: Introduction
# - Introduction to Course and Web-enabled content
# - Computational thinking concepts 
# - JupyterLab Environment for ENGR 1330 

# ---
# ## Course Content
# 
# The course content is hosted at [http://54.243.252.9/engr-1330-webroot/](http://54.243.252.9/engr-1330-webroot/).  Direct access is not the intended way to get the content, as the web-site is comparatively unstructured.  Instead use the links in the syllabus located at [http://54.243.252.9/engr-1330-webroot/0-Syllabus/ENGR-1330-2022-1-Syllabus.html](http://54.243.252.9/engr-1330-webroot/0-Syllabus/ENGR-1330-2022-1-Syllabus.html) .  
# 
# 

# ---
# 
# ## Computational Thinking Concepts
# 
# Computational thinking (CT) refers to the thought processes involved in expressing solutions as computational steps or algorithms that can be carried out by a computer. Data science is one of several applications of CT.
# 
# Much of what follows is borrowed from (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2696102/).
# 
# Computational thinking is taking an approach to solving problems, designing systems and understanding human behaviour that draws on concepts fundamental to computing (http://www.cs.cmu.edu/~15110-s13/Wing06-ct.pdf).
# 
# Computational thinking is a kind of analytical thinking:
# 
# - It shares with mathematical thinking in the general ways in which we might approach solving a problem. 
# - It shares with engineering thinking in the general ways in which we might approach designing and evaluating a large, complex system that operates within the constraints of the real world. - It shares with scientific thinking in the general ways in which we might approach understanding computability, intelligence, the mind and human behaviour.
# 
# The essence of computational thinking is **abstraction** and **automation**. 
# In computing, we abstract notions beyond the physical dimensions of time and space. Our abstractions are extremely general because they are symbolic, where numeric abstractions are just a special case.
# 
# ### CT Foundations
# 
# CT is literally a process for breaking down a problem into smaller parts, looking for patterns in the problems, identifying what kind of information is needed, developing a step-by-step solution, and implementing that solution. 
# 
# 1. Decomposition
# 2. Pattern Recognition
# 3. Abstraction
# 4. Algorithms
# 5. System Integration (implementation)
# 
# #### Decomposition
# Decomposition is the process of taking a complex problem and breaking it into more manageable sub-problems. Examples include:  
# - Writing a paper:  
#  - Introduction 
#  - Body 
#  - Conclusion 
#  
# - Wide-viewed (Panorama) image: 
#  - Taking multiple overlapped photos 
#  - Stitch them
#  
# Decomposition often leaves a **framework** of sub-problems that later have to be **assembled (system integration)** to produce a desired solution.
#  
# #### Pattern Recognition
# Refers to finding similarities, or shared characteristics of problems.  Allows a complex problem to become easier to solve. Allows use of same solution method for each occurrence of the pattern. 
# 
# Pattern recognition allows use of **automation** to process things - its a fundamental drilled shaft of CT.  It also provides a way to use analogs from old problems to address new situations; it also will require **assembly (system integration)** to produce a desired solution.
# 
# #### Abstraction
# 
# Determine important characteristics of the problem and ignore characteristics that are not important. Use these characteristics to create a representation of what we are trying to solve. 
# 
# Books in an online bookstore
# 
# |Important| NOT important| 
# |:--------|:-------------|
# |title    | Cover color  |
# |ISBN     |Author’s hometown| 
# |Authors  | ... |
# |...      | ... |
# 
# 
# #### Algorithms
# Step-by-step instructions of how to solve a problem (https://en.wikipedia.org/wiki/Algorithm). 
# Identifies what is to be done, and the order in which they should be done.
# 
# ```{figure} algorithm.png
# ---
# width: 400px
# name: algorithm
# ---
# Humorous "algorithm". Image from [https://www.newyorker.com/magazine/2021/01/18/whats-wrong-with-the-way-we-work?utm_source=pocket-newtab](https://www.newyorker.com/magazine/2021/01/18/whats-wrong-with-the-way-we-work?utm_source=pocket-newtab)
# ```
# {numref}`algorithm`
# 
# <!--![](algorithm.png) 
# 
# ||Image from [https://www.newyorker.com/magazine/2021/01/18/whats-wrong-with-the-way-we-work?utm_source=pocket-newtab](https://www.newyorker.com/magazine/2021/01/18/whats-wrong-with-the-way-we-work?utm_source=pocket-newtab)||
# |---|------------|---| -->
# 
# An algorithm is a **finite** sequence of defined, instructions, typically to solve a class of problems or to perform a computation. Algorithms are unambiguous and are used as specifications for performing calculations, data processing, automated reasoning, and other tasks. Starting from an initial state and initial input (perhaps empty), the instructions describe a computation that, when executed, proceeds through a finite number of defined successive states, eventually producing "output" and terminating at a final ending state. The transition from one state to the next is not necessarily deterministic; some algorithms, known as randomized algorithms, can incorporate random input.
# 
# #### System Integration (implementation)
# 
# System integration is the assembly of the parts above into the complete (integrated) solution.  Integration combines parts into a program which is the realization of an algorithm using a syntax that the computer can understand. 

# ## JupyterLab Environment

# ## References
# 
# 1. Driscoll, M. (2021) *Jupyter Notebook: An Introduction*, [https://realpython.com/jupyter-notebook-introduction/](https://realpython.com/jupyter-notebook-introduction/) 
# 
# 2. Computational and Inferential Thinking Ani Adhikari and John DeNero, Computational and Inferential Thinking, The Foundations of Data Science, Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND) Chapter 1 [https://www.inferentialthinking.com/chapters/01/what-is-data-science.html](https://www.inferentialthinking.com/chapters/01/what-is-data-science.html)
# 
# 3. Learn Python the Hard Way (Online Book) [https://learnpythonthehardway.org/book/](https://learnpythonthehardway.org/book/)  Recommended for beginners who want a complete course in programming with Python.
# 
# 4. LearnPython.org (Interactive Tutorial) [https://www.learnpython.org/](https://www.learnpython.org/)  Short, interactive tutorial for those who just need a quick way to pick up Python syntax.
# 
# 5. How to Think Like a Computer Scientist (Interactive Book) [https://runestone.academy/runestone/books/published/thinkcspy/index.html](https://runestone.academy/runestone/books/published/thinkcspy/index.html) Interactive "CS 101" course taught in Python that really focuses on the art of problem solving. 
# 
# 6. Beginning Programming with Python® For Dummies®, John Wiley & Sons, Inc., 111 River Street, Hoboken, NJ 07030-5774 [https://we.riseup.net/assets/345912/Beginning+Programming+with+Python+For+Dummies+Mueller%2C+John+Paul+%5BSRG%5D.pdf](https://we.riseup.net/assets/345912/Beginning+Programming+with+Python+For+Dummies+Mueller%2C+John+Paul+%5BSRG%5D.pdf)
# 
# <!--
# [http://54.243.252.9/engr-1330-webroot/3-Readings/BeginningProgrammingwithPythonForDummiesMuellerJohnPaul[SRG].pdf](http://54.243.252.9/engr-1330-webroot/3-Readings/BeginningProgrammingwithPythonForDummiesMuellerJohnPaul[SRG].pdf)
# -->

# ---
# 
# ## Laboratory 0
# 
# **Examine** (click) Laboratory 0 as a webpage at [Laboratory 0.html](http://54.243.252.9/engr-1330-webroot/8-Labs/Lab00/Lab00.html)
# 
# **Download** (right-click, save target as ...) Laboratory 0 as a jupyterlab notebook from [Laboratory 0.ipynb](http://54.243.252.9/engr-1330-webroot/8-Labs/Lab00/Lab00.ipynb)
# 

# <hr><hr>
# 
# ## Exercise Set 0
# 
# **Examine** (click) Exercise Set 0 as a webpage at [Exercise 0.html](http://54.243.252.9/engr-1330-webroot/8-Labs/Lab00/Lab00-TH.html)
# 
# **Download** (right-click, save target as ...) Exercise Set 0 as a jupyterlab notebook at  [Exercise Set 0.ipynb](http://54.243.252.9/engr-1330-webroot/8-Labs/Lab00/Lab00-TH.ipynb)
# 
# 

# In[ ]:




