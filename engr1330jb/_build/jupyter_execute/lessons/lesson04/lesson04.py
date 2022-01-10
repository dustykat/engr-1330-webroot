#!/usr/bin/env python
# coding: utf-8

# <div class="alert alert-block alert-info">
#     <b><h1>ENGR 1330 Computational Thinking with Data Science </h1></b> 
# </div> 
# 
# Copyright © 2021 Theodore G. Cleveland and Farhang Forghanparast
# 
# Last GitHub Commit Date: 
#     
# # 4: Data Structures
# - what are variables?
# - naming conventions
# - the assignment symbol

# In[ ]:





# ---
# ## Objectives
# 
# 1. Awareness of data structures available in Python to store and manipulate data 
# 2. Implement arrays (lists), dictionaries, and tuples
# 2. Address contents of lists , dictionaries, and tuples

# ---
# ## Data Structures and Conditional Statements
# 
# **Computational thinking (CT)** concepts involved are:
# 
# - `Decomposition` : Data interpretation, manipulation, and analysis of NumPy arrays
# - `Abstraction` : Data structures; Arrays, lists, tuples, sets, and dictionaries
# - `Algorithms` : Conditional statements
# 
# ## What is a data structure?
# 
# Data Structures are a specialized means of organizing and storing data in computers in such a way that we can perform operations on the stored data more efficiently.
# 
# ```{figure} image-data-structures.png
# ---
# width: 500px
# name: image-data-structures
# ---
# Data structures in Python
# ```
# {numref}`image-data-structures` depicts most of the common data structures we encounter.  A reasonable mental model is that a data structure is like a variable that has multiple parts, the structure allows reference by name, then the part.
# 

# ### Lists
# 
# A list is a collection of data that are somehow related. It is a convenient way to refer to a
# collection of similar things by a single name, and using an index (like a subscript in math)
# to identify a particular item.
# 
# Consider the "math-like" variable $x$ below:
# 
# $
# \begin{gather}
# x_0= 7 \\
# x_1= 11 \\
# x_2= 5 \\
# x_3= 9 \\
# x_4= 13 \\
# \dots \\
# x_N= 223 \\
# \end{gather}
# $
#     
# The variable name is $x$ and the subscripts correspond to different values. 
# Thus the `value` of the variable named $x$ associated with subscript $3$ is the number $9$.
# 
# 
# ```{figure} image-array-image.png
# ---
# width: 500px
# name: image-array-image
# ---
# List visualization as a collection of adjacent cells with a common name, and different position indices to locate a particular cell
# ```
# {numref}`image-array-image` is a visual representation of a the concept that treats a variable as a collection of cells. 
# 
# In the figure, the variable name is `MyList`, the subscripts are replaced by an index
# which identifies which cell is being referenced. 
# The value is the cell content at the particular index. 
# 
# So in the figure the value of `MyList` at Index = 3 is the number 9.'
# 
# In engineering and data science we use lists a lot - we often call them vectors, arrays, matrices and such, but they are ultimately just lists.
# 
# To declare a list you can write the list name and assign it values. 
# The square brackets are used to identify that the variable is a list. 
# Like:
# 
#     MyList = [7,11,5,9,13,66,99,223]
# 
# One can also declare a null list and use the `append()` method to fill it as needed.
# 
#     MyOtherList = [ ]
#     
# Python indices start at **ZERO**. 
# A lot of other languages start at ONE. 
# It's just the convention. 
# 
# The first element in a list has an index of 0, the second an index of 1, and so on.
# We access the contents of a list by referring to its name and index. 
# For example 
# 
#     MyList[3] has a value of the number 9.

# ### Arrays
# 
# Arrays are special lists that are used to store only elements of a specific data type, and require use of an external dependency (package) named **array**.  The package is installed with core python, so other than importing it into a script nothing else special is needed.
# 
# Arrays are:
# -  Ordered: Elements in an array can be indexed
# -  Mutable: Elements in an array can be altered
# 
# ```{figure} image-python-arrays-index-local.png
# ---
# width: 500px
# name: image-python-arrays-index-local
# ---
# List visualization as a collection of adjacent cells with a common name, and different position indices to locate a particular cell.  The image is linked from [https://pi.lbbcdn.com/wp-content/uploads/2020/01/Python-Arrays-Index-example-diagram.png](https://pi.lbbcdn.com/wp-content/uploads/2020/01/Python-Arrays-Index-example-diagram.png)
# ```
# {numref}`image-python-arrays-index-local` is a depiction of an array (a list of numbers), detailing forward and backward indexing that is used to slice (select a subset) the array.  Identical in concept to slicing a string (which itself is a list of string values).
# 
# Data type that an array must hold is specified using the type code when it is created
# - ‘f’ for float
# - ‘d’ for double
# - ‘i’ for signed int
# - ‘I’ for unsigned int
# 
# More types are listed below
# 
# 
# |Type Code|C Data Type|Python Data Type|Minimum Size in Bytes|
# |:---|---|---|---:|
# |'b'|	signed char|int	|1|
# |'B'|	unsigned char	|int	|1|
# |'h'|	signed short	|int	|2|
# |'H'|	unsigned short	|int	|2|
# |'i'|	signed int	|int	|2|
# |'I'|	unsigned int	|int	|2|
# |'l'|	signed long	|int	|4|
# |'L'|	unsigned long	|int	|4|
# |'q'|	signed long long	|int	|8|
# |'Q'|	unsigned long long	|int	|8|
# |'f'|	float	|float	|4|
# |'d'|	double	|float	|8|
# 
# To use arrays, a library named ‘array’ must be imported. The libary is available in an ordinary python install, so you should not need to use `conda ...` or `pip3 ...`

# In[1]:


import array 


# Creating an array that contains signed integer numbers

# In[2]:


myarray = array.array('i', [1, 2, 4, 8, 16, 32])


# In[3]:


myarray[0] #1-st element, 0-th position


# In[4]:


import array as arr #import using an alias so the calls don't look so funny


# In[5]:


myarray = arr.array('i', [1, 2, 4, 8, 16, 32])
myarray[0] #1-st element, 0-th position


# Lists: Can store elements of different data types; like arrays they are (arrays are lists, but lists are not quite arrays!)
# - Ordered: Elements in a list can be indexed
# - Mutable: Elements in a list can be altered
# - Mathematical	operations	must	be	applied	to	each element	of	the	list	

# ### Tuple - A special list
# 
# A tuple is a special kind of list where the **values cannot be changed** after the list is created.
# Such a property is called `immutable`
# It is useful for list-like things that are static - like days in a week, or months of a year.
# You declare a tuple like a list, except use round brackets instead of square brackets.
# 
#     MyTupleName = ("Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec")
#     
# Tuples are often created as output from packages and functions.
# 
# Removing individual tuple elements is not possible. There is, of course, nothing wrong with putting together another tuple with the undesired elements discarded.
# 
# To explicitly remove an entire tuple, just use the del statement.

# In[6]:


a_tuple = ("a", "b")
print(a_tuple)
added_value = "c"
added_value_tuple = (added_value,) # notice the dangling comma
short_tuple =(a_tuple[1],) # notice the dangling comma
new_tuple = short_tuple + added_value_tuple
del(a_tuple) # kill the original
print(new_tuple)


# 
# ### Dictionary - A special list
# 
# A dictionary is a special kind of list where the items are related data `PAIRS`. 
# It is a lot like a relational database (it probably is one in fact) where the first item in the pair is called the key, and must be unique in a dictionary, and the second item in the pair is the data.
# The second item could itself be a list, so a dictionary would be a meaningful way to build a
# database in Python.
# 
# To declare a dictionary using `curly` brackets
# 
#     MyPetsNamesAndMass = { "Dusty":7.8 , "Aspen":6.3, "Merrimee":0.03}
# 
# To declare a dictionary using the `dict()` method
# 
#     MyPetsNamesAndMassToo = dict(Dusty = 7.8 , Aspen = 6.3, Merrimee = 0.03)
#     
# Dictionary properties
# - Unordered: Elements in a dictionary cannot be
# - Mutable elements: Elements in a dictionary can be altered
# - Immutable keys: Keys in a dictionary cannot be altered

# In[7]:


MyPetsNamesAndMass = { "Dusty":7.8 , "Aspen":6.3, "Merrimee":0.03}
MyPetsNamesAndMassToo = dict(Dusty = 7.8 , Aspen = 6.3, Merrimee = 0.03)
print(MyPetsNamesAndMass)
print(MyPetsNamesAndMassToo)


# ### Sets - A special list
# 
# Sets: Are used to store elements of different data types
# - Unordered: Elements in a set cannot be indexed
# - Mutable: Elements in a set can be altered
# - Non-repetition: Elements in a set are unique
# 
# Elements of a set are enclosed in curly brackets { }
# - Creating sets that contains different data types
# - Sets cannot be nested

# ### Example of a Dictionary
# A dictionary, using natural numbers as keys

# In[8]:


myset = {1:'one',2:'two',3:{1:'one',2:'two',3:'seven of nine'}}
type(myset)


# In[9]:


(myset.get(3)).get(3) # get element from key 3 of key 3 set


# ### Example of a Set (no explicit keys)
# A set, three elements, no explicit keys

# In[10]:


myset = {1,2,77}
type(myset)


# Another set

# In[11]:


urset={'apple','cat','rock',77,'sunset strip'}
type(urset)


# #### Union and Intersection of two sets 
# - Union joins all unique elements (null return only if all sets are empty)
# - Intersection extracts all common elements (null returns possible)

# In[12]:


# union (join) sets
print('union is : ' ,myset | urset)
# intersection of sets (shared elements)
print('intersection is : ' ,myset & urset)


# Set constructor method is another way to create a set.

# In[13]:


thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset) 


# #### What's the difference between a set and dictionary? 
# A set is like a dictionary where the keys themselves are the values; the keys are unique (duplicates are not allowed).  You can construct sets with duplicates and the constructor will drop duplicates - try it with the first set above.
# 
# Another comparison from [https://stackoverflow.com/questions/34370599/difference-between-dict-and-set-python](https://stackoverflow.com/questions/34370599/difference-between-dict-and-set-python) is
# "Well, a set is like a dict with keys but no values, and they're both implemented using a hash table. But yes, it's a little annoying that the {} notation denotes an empty dict rather than an empty set, but that's a historical artifact."
# 
# In the example below, we look at empty versions of each.

# In[14]:


# Empty dictionary
webster = {}
print(type(webster))
# Empty set
empty = set(())
print(type(empty))


# ## References
# 1. Computational and Inferential Thinking Ani Adhikari and John DeNero, Computational and Inferential Thinking, The Foundations of Data Science, Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND) Chapter 4 Subpart 3 [https://www.inferentialthinking.com/chapters/04/3/Comparison.html](https://www.inferentialthinking.com/chapters/04/3/Comparison.html)
# 
# 2. Computational and Inferential Thinking Ani Adhikari and John DeNero, Computational and Inferential Thinking, The Foundations of Data Science, Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND) Chapter 4 
# [https://www.inferentialthinking.com/chapters/04/Data_Types.html](https://www.inferentialthinking.com/chapters/04/Data_Types.html)
# 
# 3. Learn Python in One Day and Learn It Well. Python for Beginners with Hands-on Project. (Learn Coding Fast with Hands-On Project Book -- Kindle Edition by LCF Publishing (Author), Jamie Chan [https://www.amazon.com/Python-2nd-Beginners-Hands-Project-ebook/dp/B071Z2Q6TQ/ref=sr_1_3?dchild=1&keywords=learn+python+in+a+day&qid=1611108340&sr=8-3](https://www.amazon.com/Python-2nd-Beginners-Hands-Project-ebook/dp/B071Z2Q6TQ/ref=sr_1_3?dchild=1&keywords=learn+python+in+a+day&qid=1611108340&sr=8-3)
# 
# 5. Sets (tutorial) [https://realpython.com/python-sets/](https://realpython.com/python-sets/)
# 
# 6. Arrays (tutorial) [https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/](https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/)
# 
