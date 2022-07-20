#!/usr/bin/env python
# coding: utf-8

# # Integration of Tabular Data
# 
# This section is going to work with tabular data -- different from function evaluation, but
# similar. To be really useful, we need to learn how to read data from a file; manually
# entering tabular data is really time consuming, error prone, and just plain idiotic.
# 
# So in this chapter we will learn how to read data from a file into a list, then we can process
# the list as if it were a function and integrate its contents.
# 
# ## Reading from a file --- open, read, close files
# 
# First, lets consider a file named ``MyFile.txt``.   The extension is important so that the Shell does not think it is a Python script.
# The contents of ``MyFile.txt`` are:
# 
#     1  1
#     2  4
#     3  9
#     4  16
#     5  25
# 
# The code fragment below, will let us look at the file (already existing in our local directory)

#     

# In[1]:


import subprocess # lets us run "shell" commands and recover stdio stream
usefull_cat_call = subprocess.run(["cat","MyFile.txt"], stdout=subprocess.PIPE, text=True) # this is the call to run the bash command "cat MyFile.txt" which will display the contents of the file if it exists.
print(usefull_cat_call.stdout)


# Now that we know that the file exists,to read the contents into a Python script we have to do the following:
# 
# - Open a connection to the file --- this is a concept common to all languages, it might be called something different, but the program needs to somehow know the location and name of the file.
#     
# - Read the contents into an object --- we have a lot of control on how this gets done, for the time being we won't exercise much control yet.  When you do substantial programs, you will depend on the control of the reads (and writes).
#     
# - Disconnect the file --- this too is common to all languages.  Its a really easy step to forget.  Not a big deal if the program ends as planned but terrible if there is a error in the program and the connection is still open.  Usually nothing bad happens, but with an open connection it is possible for the file to get damaged.   If that file represents millions of customers credit card numbers, that's kind of a problem, and time to go work on your resume, or get your passport collection out and choose a country without extradition.
#     
# The code fragment below performs these three tasks and prints the things we read

# In[2]:


Afile = open("MyFile.txt","r") # open a connection to the file; set to "read"
# read the five lines
line1 = Afile.readline()
line2 = Afile.readline()
line3 = Afile.readline()
line4 = Afile.readline()
line5 = Afile.readline()
Afile.close() # disconnect from the file
# echo the input
print(line1,end="")
print(line2,end="")
print(line3,end="")
print(line4,end="")
print(line5,end="")


# ### Read into a list
# A far more useful and elegant way to read from a file is to use a ``for`` loop.   The attribute ``line`` within a file is an iterable, hence construction the loop is pretty straightforward.   
# 
# A script fragment below does the same thing as the example above, but uses a ``for`` loop to accomplish stepping through the file.   
# 
# Additionally, I have added a counter to keep track of how many lines were read --- in a lot of engineering programs, the number of things read becomes important later in a program, hence it is usually a good idea to capture the count when the data are first read.
# 
# First lets work out if we can automatically detect the end of the file.  So this script just reads and prints the attribute ``line`` from object ``Afile``.  
# Notice how the print statement is changed, to suppress the extra line feed.

# In[3]:


Afile = open("MyFile.txt","r") # open a connection to the file; set to "read"
# read using a for loop, exit when at end of file  and report line count
how_many_lines = 0 # start our counter!
for line in Afile:
    print(line,end="")
    how_many_lines += 1
Afile.close() # disconnect from the file
print("\nFile has ",how_many_lines," records (lines)")


# Now we will add a list to receive the input, here it reads the file above as a string into a list ``xy``, then splits that list and places the contents into two other lists, ``x`` and ``y``.  The script has several parts to discuss.   First, the destination variables (lists) must be created -- I used the null list concept here because I don't know how big the list is until I read the list.  
# Next I used the ``.append()`` method which operates on the ``xy`` list.  
# The arguments of the method ``[str(n) for n in line.strip().split()]`` tells the program that the elements are to be interpreted as a string, and to split (split) the line into sub-strings based on a null delimiter (whitespace), and to remove all the whitespace (strip) characters.   
# 
# Once the line is split, the strings are appended into the ``xy`` list.  The ``xy`` list is printed to show that it is a list of 5 things, each thing being a string comprised of two sets of characters separated by a comma.   ``xy`` is a list of strings.
# 
# The next section of the code then uses the ``pair`` function within another ``.append()`` method to break the character sets in each element of ``xy`` into two parts ``x`` and ``y``.  
# Lastly during the pair operation, the code also converts the data into real values (float) and then prints the data in two columns.    
# This seems like a lot of work, but we could easily get this code to be super reliable, then save it as a function and never have to write it again.   That too comes later -- suffice to say for now we can read a file, parse its contents into two lists $x$ and $y$.  Thus we are now able to integrate tabular data.

# In[4]:


xy = [] # null list to store the lines
x  = [] # a null list for the first column
y  = [] # a null list for the second column
Afile = open("MyFile.txt","r") # open a connection to the file; set to "read"
# read using a for loop, exit when at end of file  and report line count
how_many_lines = 0 # start our counter!
for line in Afile:
    print(line,end="")
    xy.append([str(n) for n in line.strip().split()]) # append line to xy, split the line on whitespace, strip out whitespace
    how_many_lines += 1
Afile.close() # disconnect from the file
print("\nFile has ",how_many_lines," records (lines)")
print("The list is: ",end="")
print(xy) # the list
for pair in xy:  # parse into x and y
    x.append(float(pair[0]))
    y.append(float(pair[1]))
# verify parsed
for i in range (0,how_many_lines,1):
    print("x = ",x[i]," y = ",y[i])


# ## Integrating the Tabular Data
# Suppose instead of a function we only have tabulations and wist to estimate the area under the curve represented by the tabular values.  Then our integration rules from the prior chapter still work more or less, except the rectangular panels will have to be shifted to either the left edge or right edge of a panel (where the tabulation exists).   
# 
# Lets just examine an example.  Suppose some measurement technology produced a table of related values.   
# The excitation variable is ``x`` and ``f(x)`` is the response. 
# 
#         x    f(x) 
#        1.0  1.543 
#        1.1  1.668 
#        1.2  1.811 
#        1.3  1.971 
#        1.4  2.151 
#        1.5  2.352 
#        1.6  2.577 
#        1.7  2.828 
#        1.8  3.107
#        
# To integrate this table using the trapezoidal method is straightforward.  
# We will modify our earlier code to read the table (which we put into a file), and compute the integral. 

# In[5]:


# My Tabular Integration
# Integrate a table of values using Trapezoidal Panels
xy = [] # null list to store the lines
x  = [] # a null list for the first column
y  = [] # a null list for the second column
Afile = open("MyTableOfData.txt","r") # open a connection to the file; set to "read"
# read using a for loop, exit when at end of file  and report line count
how_many_lines = 0 # start our counter!
for line in Afile:
    print(line,end="")
    xy.append([str(n) for n in line.strip().split()]) # append line to xy, split the line on whitespace, strip out whitespace
    how_many_lines += 1
Afile.close() # disconnect from the file
print("\nFile has ",how_many_lines," records (lines)")
print("The list is: ",end="")
print(xy) # the list
for pair in xy:  # parse into x and y
    x.append(float(pair[0]))
    y.append(float(pair[1]))
# verify parsed
for i in range (0,how_many_lines,1):
    print("x = ",x[i]," y = ",y[i])
# now the actual integration
accumulated_area = 0 # an accumulator
for i in range(0,how_many_lines-1,1): #index stops at n-1 things because each panel evaluated at both ends
    delta_x = x[i+1]-x[i]
    height =(y[i+1]+y[i])/2.0
    accumulated_area += height*delta_x
print("Area = ",accumulated_area)  # report the result


# Cool, it seems to work -- now tidy the code a bit by suppressing extra outputs

# In[6]:


# My Tabular Integration
# Integrate a table of values using Trapezoidal Panels
xy = [] # null list to store the lines
x  = [] # a null list for the first column
y  = [] # a null list for the second column
Afile = open("MyTableOfData.txt","r") # open a connection to the file; set to "read"
# read using a for loop, exit when at end of file  and report line count
how_many_lines = 0 # start our counter!
for line in Afile:
    ##print(line,end="")
    xy.append([str(n) for n in line.strip().split()]) # append line to xy, split the line on whitespace, strip out whitespace
    how_many_lines += 1
Afile.close() # disconnect from the file
print("\nRecords read =: ",how_many_lines)
##print("The list is: ",end="")
##print(xy) # the list
for pair in xy:  # parse into x and y
    x.append(float(pair[0]))
    y.append(float(pair[1]))
# verify parsed
for i in range (0,how_many_lines,1):
    print("x = ",x[i]," y = ",y[i])
# now the actual integration
accumulated_area = 0 # an accumulator
for i in range(0,how_many_lines-1,1): #index stops at n-1 things because each panel evaluated at both ends
    delta_x = x[i+1]-x[i]
    height =(y[i+1]+y[i])/2.0
    accumulated_area += height*delta_x
print("Area = ",accumulated_area)  # report the result


# Realistically the only other simple integration method for tabular data is the rectangular rule, either using the left edge of a panel or the right edge of a panel (and I suppose you could do both and average the result which would be the trapezoidal method).
