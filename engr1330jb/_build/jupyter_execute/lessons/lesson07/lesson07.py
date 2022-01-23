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
# # 7: Files
# - Files and Filesystems
# - Opening and reading text (ascii) files
# - Using loops to read text files
# - Writing to text files
# - Download files from a remote server
# - Creating and deleting files from your notebook
# 

# In[ ]:





# ---
# ## Objectives
# 1. Describe files, file types, and search paths 
# 2. Demonstrate file creation, and deletion in a script
# 3. Demonstrate create, open, read from a file
# 4. Demonstrate open, write to a file
# 5. Apply packages to directly obtain a file from a remote server
# 

# ## Files and Filesystems
# 
# A computer file is a computer resource for recording data discretely (not in the secretive context, but specifically somewhere on a piece of hardware) in a computer storage device. Just as words can be written to paper, so can information be written to a computer file. Files can be edited and transferred through the internet on that particular computer system.
# 
# There are different types of computer files, designed for different purposes. A file may be designed to store a picture, a written message, a video, a computer program, or a wide variety of other kinds of data. Some types of files can store several types of information at once.
# 
# By using computer programs, a person can open, read, change, save, and close a computer file. Computer files may be reopened, modified, and copied an arbitrary number of times.
# 
# Typically, files are organised in a file system, which keeps track of where the files are located on disk and enables user access. 

# ---
# 
# ### File system
# In computing, a file system or filesystem, controls how data is stored and retrieved. 
# Without a file system, data placed in a storage medium would be one large body of data with no way to tell where one piece of data stops and the next begins. 
# By separating the data into pieces and giving each piece a name, the data is isolated and identified. 
# Taking its name from the way paper-based data management system is named, each group of data is called a “file”. 
# The structure and logic rules used to manage the groups of data and their names is called a “file system”.  
# 
# The figure below is a graphical representation of the filesystem on my office computer.  I have the file browser listing the contants of a directory named `/src`.  It is contained in a directory named `/final_report`, which is contained in a higher level directory all the way up to `/Users` (`/` is aliased to `Macintosh HD` in the figure)
# 
# <img src="http://54.243.252.9/engr-1330-webroot/engr1330jb/lessons/lesson07/Filesystem-graphic.png" width="700">
# 
# An equivalent representation, in a `bash` shell is shown in the figure below which is a capture of a terminal window.
# 
# <img src="http://54.243.252.9/engr-1330-webroot/engr1330jb/lessons/lesson07/Filesystem-shell.png" width="700">

# ---
# 
# ### Path
# A path, the general form of the name of a file or directory, specifies a unique location in a file system. A path points to a file system location by following the directory tree hierarchy expressed in a string of characters in which path components, separated by a delimiting character, represent each directory. The delimiting character is most commonly the slash (`/`), the backslash character (`\`), or colon (`:`), though some operating systems may use a different delimiter.
# Paths are used extensively in computing to represent the directory/file relationships common in modern operating systems, and are essential in the construction of Uniform Resource Locators (URLs). Resources can be represented by either absolute or relative paths.
# As an example consider the following two files:
# 
# 1. /Users/theodore/MyGit/@atomickitty/hurri-sensors/.git/Guest.conf 
# 2. /etc/apache2/users/Guest.conf
# 
# They both have the same file name, but are located on different paths. 
# Failure to provide the path when addressing the file can be a problem. 
# Another way to interpret is that the two unique files actually have different names, and only part of those names is common (Guest.conf)
# The two names above (including the path) are called fully qualified filenames (or absolute names), a relative path (usually relative to the file or program of interest depends on where in the directory structure the file lives. 
# If we are currently in the .git directory (the first file) the path to the file is just the filename.

# ---
# 
# ### File Types
# 
# 1. Text Files. Text files are regular files that contain information readable by the user. This information is usually stored as ASCII with various encoding extensions (to handle other alphabets and emojis). You can display and print these files. The lines of a text file must not contain NULL characters, and none can exceed a prescribed (by architecture) length, including the new-line character.  The term text file does not prevent the inclusion of control or other nonprintable characters (other than NUL). Therefore, standard utilities that list text files as inputs or outputs are either able to process the special characters gracefully or they explicitly describe their limitations within their individual sections.
# 
# 2. Binary Files. Binary files are regular files that contain information readable by the computer. Binary files may be executable files that instruct the system to accomplish a job. Commands and programs are stored in executable, binary files. Special compiling programs translate ASCII text into binary code.  The only real difference between text and binary files is that text files have lines of some prescribed length, with no NULL characters, each terminated by a new-line character.
# 
# 3. Directory Files. Directory files contain information the system needs to access all types of files, but they do not contain the actual file data. As a result, directories occupy less space than a regular file and give the file system structure flexibility and depth. Each directory entry represents either a file or a subdirectory. Each entry contains the name of the file and the file's index node reference number (i-node). The i-node points to the unique index node assigned to the file. The i-node describes the location of the data associated with the file. Directories are created and controlled by a separate set of commands.

# ---
# 
# ### File Manipulation
# 
# For this lesson we examine just a handfull of file manipulations which are quite useful. Files can be "created","read","updated", or "deleted" (CRUD). 

# #### Example: Examine our local directory
# First will use some system commands to view the contents of the local directory.  
# > The code blocks below are for Linux systems, and the instructions may not execute correctly on a windows machine

# In[1]:


import sys
get_ipython().system(' rm -rf myfirstfile.txt # delete file if it exists')
get_ipython().system(' pwd # list name of working directory, note it includes path, so it is an absolute path')
get_ipython().system(' ls -la')


# In[2]:


# In windows
# import sys
#! del myfirstfile.txt # delete file if it exists
#! echo %cd% # list name of working directory, note it includes path, so it is an absolute path


# In[3]:


get_ipython().system(' ls -l # list contents of working directory')


# #### Example: Create a file, write to it. 
# Below is an example of creating a file that does not yet exist.
# The script is a bit pendandic on purpose.

# In[4]:


# create file example
externalfile = open("myfirstfile.txt",'w') # create connection to file, set to write (w), file does not need to exist
mymessage = 'message in a bottle' #some object to write, in this case a string
externalfile.write(mymessage)# write the contents of mymessage to the file
externalfile.close() # close the file connection


# At this point our new file should exist, lets list the directory and see if that is so

# In[5]:


get_ipython().system(' ls -l # list contents of working directory')


# Sure enough, its there, 
# > We will use a Linux shell command `cat` to look at the contents of the file.

# In[6]:


get_ipython().system(' cat myfirstfile.txt')


# #### Example: Read from an existing file. 
# 
# We will continue using the file we just made, and read from it the example is below

# In[7]:


# read file example
externalfile = open("myfirstfile.txt",'r') # create connection to file, set to read (r), file must exist
silly_string = externalfile.read() # read the contents
externalfile.close() # close the file connection
print(silly_string)


# These first two examples are supremely simple, but illustrate important points:
# 
# 1. The program establishes a connection to the file
# 2. One connection exists, then read from, write to the file
# 3. Close the connection (to clear the I/O buffer and release the connection thread)
# 

# ```
# # write without a connection -- observe the error message
# mymessage = 'message in a bottle' #some object to write, in this case a string
# externalfile.write(mymessage)# write the contents of mymessage to the file
# ```

# ```
# # read without a connection -- observe the error message
# silly_string = externalfile.read() # read the contents
# print(silly_string)
# ```

# #### Example: Update a file.
# 
# This example continues with our same file, but we will now add contents without destroying existing contents. The keyword is `append`

# In[8]:


externalfile = open("myfirstfile.txt",'a') # create connection to file, set to append (a), file does not need to exist
externalfile.write('\n') # adds a newline character
what_to_add = 'I love rock-and-roll, put another dime in the jukebox baby ... \n' 
externalfile.write(what_to_add) # add a string including the linefeed
what_to_add = '... the waiting is the hardest part \n' 
externalfile.write(what_to_add) # add a string including the linefeed
mylist = [1,2,3,4,5] # a list of numbers
what_to_add = ','.join(map(repr, mylist)) + "\n" # one way to write the list
externalfile.write(what_to_add)
what_to_add = ','.join(map(repr, mylist[0:len(mylist)])) + "\n" # another way to write the list
externalfile.write(what_to_add)
externalfile.close()


# In[9]:


externalfile = open("myfirstfile.txt",'a') # create connection to file, set to append (a), file does not need to exist
externalfile.write('\n') # adds a newline character
what_to_add = 'I love rock-and-roll, put another dime in the jukebox baby ... \n' 
externalfile.write(what_to_add) # add a string including the linefeed
externalfile.close()


# As before we can examine the contents using a shell command sent from the notebook.

# In[10]:


get_ipython().system(' cat myfirstfile.txt')


# #### Example: Delete a file
# 
# Delete can be done by a system call as we did above to clear the local directory
# 
# In a JupyterLab notebook, we can either use
# 
#     import sys
#     ! rm -rf myfirstfile.txt # delete file if it exists
# 
# or
# 
#     import os
#     os.remove("myfirstfile.txt")
# 
# they both have same effect, both equally dangerous to your filesystem.
# 
# 
# Learn more about CRUD with text files at https://www.guru99.com/reading-and-writing-files-in-python.html
# 
# Learn more about file delete at https://www.dummies.com/programming/python/how-to-delete-a-file-in-python/
#     

# In[11]:


import os
file2kill = "myfirstfile.txt"
try:
    os.remove(file2kill) # file must exist or will generate an exception
except:
    pass # example of using pass to improve readability
print(file2kill, " missing or deleted !")


# A little discussion on the part where we wrote numbers
# 
#     what_to_add = ','.join(map(repr, mylist[0:len(mylist)])) + "\n"
# 
# Here are descriptions of the two functions `map` and `repr`
# 
# `map(function, iterable, ...)` Apply `function` to every item of iterable and return a list of the results. 
# If additional iterable arguments are passed, function must take that many arguments and is applied to the items from all iterables in parallel. 
# If one iterable is shorter than another it is assumed to be extended with None items. 
# If function is None, the identity function is assumed; if there are multiple arguments, `map()` returns a list consisting of tuples containing the corresponding items from all iterables (a kind of transpose operation). 
# The iterable arguments may be a sequence or any iterable object; the result is always a list.
# 
# `repr(object)` Return a string containing a printable representation of an object. 
# This is the same value yielded by conversions (reverse quotes). 
# It is sometimes useful to be able to access this operation as an ordinary function. 
# For many types, this function makes an attempt to return a string that would yield an object with the same value when passed to `eval()`, otherwise the representation is a string enclosed in angle brackets that contains the name of the type of the object together with additional information often including the name and address of the object. 
# A class can control what this function returns for its instances by defining a `repr()` method.
# 
# What they do in this script is important. 
# The statement:
# 
#     what_to_add = ’,’.join(map(repr, mylist[0:len(mylist)])) + "\n"
#     
# is building a string that will be comprised of elements of mylist[0:len(mylist)].
# The `repr()` function gets these elements as they are represented in the computer, the delimiter a comma is added using the join method in Python, and because everything is now a string the
# 
#     ... + "\n"
#     
# puts a linefeed character at the end of the string so the output will start a new line the next time something is written.

# ### Example
# 
# - create a text file, name it __"MyFavoriteQuotation"__.
# - Write __your favorite quotation__ in the file.
# - Read the file.
# - Add this string to it in a new line : "And that's something I wish I had said..."
# - Show the final outcome.

# In[12]:


# create the "My Favorite Quotation" file:
externalfile = open("MyFavoriteQuotation.txt",'w')         # create connection to file, set to write (w)
myquotation = 'The path of the righteous man is beset on all sides by the inequities of the selfish and the tyranny of evil men. Blessed is he who, in the name of charity and good will, shepherds the weak through the valley of darkness. For he is truly his brother’s keeper and the finder of lost children. And I will strike down upon thee with great vengeance and furious anger those who attempt to poison and destroy my brothers. And you will know my name is the Lord when I lay my vengeance upon you.' #My choice: quotation from Pulp Fiction
externalfile.write(myquotation)# write the contents of mymessage to the file
externalfile.close() # close the file connection
#Let's read the file
#! cat MyFavoriteQuotation.txt 
# Let's add the string
externalfile = open("MyFavoriteQuotation.txt",'a')  #create connection to file, set to append (a)
externalfile.write('\n') # adds a newline character
what_to_add = "And that's something I wish I had said ... \n"
externalfile.write(what_to_add)
externalfile.close()
#Let's read the file one last time
get_ipython().system(' cat MyFavoriteQuotation.txt ')


# ---
# 
# #### Reading data from a file.
# 
# To continue our exploration, suppose we want to read from a file, and we know it is a data file - in this section the files we will use are `A.txt`, `B.txt`, and `x.txt` all located at http://54.243.252.9/engr-1330-webroot/4-Databases/ to follow along download these files to the directory where your script is running.
# 
# Our task is to determine if $x$ is a solution to $A \cdot x = B$
# 
# From our problem solving protocol the algorithmic task is
# 
# > 1. Allocate objects to store file contents;
# > 1. Read in A,B, and x from respective files;
# > 2. Echo the inputs (pedagogical in this case);
# > 2. Perform the matrix arithmetic Ax = RHS;
# > 3. Test if RHS == B;
# > 4. Report results;

# In[13]:


get_ipython().system(' pwd')
# Lets look at the files using shell commands (may need to adapt for windoze)
get_ipython().system(" echo '--- A.txt ---'")
get_ipython().system(' cat A.txt')
get_ipython().system(' echo')
get_ipython().system(" echo '--- x.txt ---'")
get_ipython().system(' cat x.txt')
get_ipython().system(' echo')
get_ipython().system(" echo '--- B.txt ---'")
get_ipython().system(' cat B.txt')


# First we make room for the data

# In[14]:


# Code to read A, X, and b - Notice we need somewhere for the data to go, hence the null lists
amatrix = [] # null list to store matrix read
xvector = [] # null list to store vector read
bvector = [] # null list to store vector read
rowNumA = 0
colNumA = 0
rowNumB = 0
rowNumX = 0


# Next read in A

# In[15]:


localfile = open("A.txt","r") # connect and read file for MATRIX A
for line in localfile:
    amatrix.append([float(n) for n in line.strip().split()])
    rowNumA += 1
localfile.close() # Disconnect the file
colNumA = len(amatrix[0]) # get the column count


# Echo the input

# In[16]:


print('A matrix')
for i in range(0,rowNumA,1):
    print ( (amatrix[i][0:colNumA]))


# Next read in x

# In[17]:


localfile = open("x.txt","r") # connect and read file for VECTOR x
for line in localfile:
    xvector.append(float(line))  # vector read different -- just float the line
    rowNumX += 1
localfile.close() # Disconnect the file


# Echo the input

# In[18]:


print('x vector')
for i in range(0,rowNumX,1):
    print ( (xvector[i]))


# Read in B

# In[19]:


localfile = open("B.txt","r") # connect and read file for VECTOR B
for line in localfile:
    bvector.append(float(line))  # vector read different -- just float the line
    rowNumB += 1
localfile.close() # Disconnect the file


# Echo the input

# In[20]:


print('B vector')
for i in range(0,rowNumB,1):
    print ( (bvector[i]))


# Now we need to perform the arithmetic.  

# In[21]:


rhs = [0 for i in range(rowNumX)] # here we will store Ax = rhs
for i in range(0,rowNumA): # select row
    for j in range(0,colNumA): # dot product current row*xvector
            rhs[i]=rhs[i]+amatrix[i][j]*xvector[j]
for i in range(0,rowNumA,1): # print out the result
    print (rhs[i])


# Now we need to compare the results, visually they are close and the floating point arithmetic using truncated inputs cannot ever be exact, so lets use our selection methods; or just print them

# In[22]:


tolerance = 1.0e-04 # decide that 1 part in 10,000 is enough
same = True # here is our flag, as we compare element by element if we find one that is not close enough we quit and declare we dont have an answer
for i in range(0,rowNumA,1): # just march through the lists
    if abs(rhs[i]-bvector[i]) > tolerance: # too far apart
        same = False
        break # we can exit the loop, 
    else:
        continue # keep checking
if same == True:
    print('The two vectors are the same, so x solves Ax=B')
else:
    print('The two vectors are different, so x does not solve Ax=B')  
    
print('---Ax---','---B---')
for i in range(0,rowNumA,1):
    print (' ',round(rhs[i],3),'    ',round(bvector[i],3))


# ---
# 
# ### Downloading files from websites (optional)
# 
# This section shows how to get files from a remote computer.  In the previous example, we can avoid the tedious select-right-click-save target .... step.   There are several ways to get files here we examine just one.  
# 
# The most important part is you need the FQDN (URL) to the file.

# ---
# 
# ### A Method to get the actual file from a remote web server (unencrypted)
# 
# > - You know the FQDN to the file it will be in structure of "http://server-name/.../filename.ext"
# > - The server is running ordinary (unencrypted) web services, i.e. `http://...`
# 
# We will need a module to interface with the remote server. Here we will use ``requests`` , so first we load the module
# 
# > You may need to install the module into your anaconda environment using the anaconda power shell, on my computer the commands are:
# > - **sudo -H /opt/jupyterhub/bin/python3 -m pip install requests** 
# >
# > Or:
# > - **sudo -H /opt/conda/envs/python/bin/python -m pip install requests**
# >
# > You will have to do some reading, but with any luck something similar will work for you. 
# 
# The example below will get a copy of a file named `all_quads_gross_evaporation.csv` that is stored on the class server, the FQDN/URL is http://54.243.252.9/engr-1330-webroot/4-Databases/all_quads_gross_evaporation.csv.  Here we can observe that the website is unencrypted `http` instead of `https`.  If we visit the URL we can confirm that the file exists (or get a 404 error, if there is no file).

# First we will import the requests module.

# In[23]:


import requests # Module to process http/https requests


# Assuming the requests module loads, lets next clear any existing local (to our machine) copies of the file, in this example, we already have the name, so will just send a system command to delete the file.  This step is mostly for the classroom demonstration - the script will happily clobber existing files.
# 
# > The system command below may be different on windoze!  What's here works on MacOS and Linux.

# In[24]:


import sys # Module to process commands to/from the OS using a shell-type syntax
get_ipython().system(' rm -rf all_quads_gross_evaporation.csv # delete file if it exists')


# Now we will generate a ``GET`` request to the remote http server.  I chose to do so using a variable to store the remote URL so I can reuse code in future projects.  The ``GET`` request (an http/https method) is generated with the requests method ``get`` and assigned to an object named ``rget`` -- the name is arbitrary.  Next we extract the file from the ``rget`` object and write it to a local file with the name of the remote file - esentially automating the download process. 

# In[25]:


remote_url="http://54.243.252.9/engr-1330-webroot/4-Databases/all_quads_gross_evaporation.csv"  # set the url
rget = requests.get(remote_url, allow_redirects=True)  # get the remote resource, follow imbedded links
localfile = open('all_quads_gross_evaporation.csv','wb') # open connection to a local file same name as remote
localfile.write(rget.content) # extract from the remote the contents,insert into the local file same name
localfile.close() # close connection to the local file


# In[26]:


print(type(localfile)) # verify object is an I/O object


# In[27]:


# verify file exists
get_ipython().system(' pwd # list absolute path to script directory')
get_ipython().system(' ls -lah # list directory contents, owner, file sizes ...')


# Now we can list the file contents and check its structure, before proceeding.

# In[28]:


get_ipython().system(' cat all_quads_gross_evaporation.csv')


# Structure kind of looks like a spreadsheet as expected; notice the unsuual character `^M`; this unprintable character is the *carriage return+line feed* control character for MS DOS (Windows) architecture.  The script below will actually strip and linefeed correctly, but sometimes all that is needed is to make a quick conversion using the system shell.
# 
# :::{note}
# > Here are some simple system commands (on a Linux or MacOS) to handle the conversion for ASCII files
# > - `sed -e 's/$/\r/' inputfile > outputfile`                # UNIX to DOS  (adding CRs)
# > - `sed -e 's/\r$//' inputfile > outputfile`                # DOS  to UNIX (removing CRs)
# > - `perl -pe 's/\r\n|\n|\r/\r\n/g' inputfile > outputfile`  # Convert to DOS
# > - `perl -pe 's/\r\n|\n|\r/\n/g'   inputfile > outputfile`  # Convert to UNIX
# > - `perl -pe 's/\r\n|\n|\r/\r/g'   inputfile > outputfile`  # Convert to old Mac
# ** Probably need to just put links to working scripts in future revision **
# :::
# 
# Now lets actually read the file into a list for some processing.  We will read it into a null list, and split on the commas (so we will be building a matrix of strings). Then we will print the first few rows and columns.

# In[29]:


# now lets process the file
localfile = open('all_quads_gross_evaporation.csv','r') # open a connection for reading
aList = [] # null list to store read
rowNumA = 0 # counter to keep track of rows, 
for line in localfile:
    #aList.append([str(n) for n in line.strip().split()])
    aList.append([str(n) for n in line.strip().split(",")]) # process each line, strip whitespace, split on ","
    rowNumA += 1 # increment the counter
localfile.close() #close the connection - amatrix contains the file contents
# print((aList[0])) # print 1st row
for irow in range(0,10):
    print([aList[irow][jcol] for jcol in range(0,10)])  # implied loop constructor syntax


# Now suppose we are interested in column with the label 910, we need to find the position of the column, and lets just print the dates (column 0) and the evaporation values for cell 910 (column unknown).
# 
# We know the first row contains the column headings, so we can use a while loop to find the position like:

# In[30]:


flag = True
c910 = 0
while flag:
    try:
        if aList[0][c910] == '910': # test if header is 910
            flag = False # switch flag to exit loop
        else :
            c910 += 1 # increment counter if not right header
    except:
        print('No column position found, resetting to 0')
        c910 = 0
        break
    
if c910 != 0:
    for irow in range(0,10): # activate to show first few rows
#    for irow in range(0,rowNumA): # activate to print entire list
        print(aList[irow][0],aList[irow][c910])  # implied loop constructor syntax    


# ---
# 
# ### A Method to get the actual file from a remote web server (SSL/TLS encrypted)
# 
# > - You know the FQDN to the file it will be in structure of "https://server-name/.../filename.ext"
# > - The server is running SSL/TLS web services, i.e. `https://...`
# > - The server has a CA certificate that is valid or possibly a self-signed certificate
# 
# **This section is saved for future semesters**

# ---
# ## References
# 1. Learn Python in One Day and Learn It Well. Python for Beginners with Hands-on Project. (Learn Coding Fast with Hands-On Project Book -- Kindle Edition by LCF Publishing (Author), Jamie Chan [https://www.amazon.com/Python-2nd-Beginners-Hands-Project-ebook/dp/B071Z2Q6TQ/ref=sr_1_3?dchild=1&keywords=learn+python+in+a+day&qid=1611108340&sr=8-3](https://www.amazon.com/Python-2nd-Beginners-Hands-Project-ebook/dp/B071Z2Q6TQ/ref=sr_1_3?dchild=1&keywords=learn+python+in+a+day&qid=1611108340&sr=8-3)
# 
# ---
# 
# 2. Read a file line by line [https://www.geeksforgeeks.org/read-a-file-line-by-line-in-python/](https://www.geeksforgeeks.org/read-a-file-line-by-line-in-python/)
# 
# 3. Read a file line by line (PLR approach) [https://www.pythonforbeginners.com/files/4-ways-to-read-a-text-file-line-by-line-in-python](https://www.pythonforbeginners.com/files/4-ways-to-read-a-text-file-line-by-line-in-python)
# 
# 4. Reading and writing files [https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python](https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python)
# 
# 5. Python Files I/O [https://www.tutorialspoint.com/python/python_files_io.htm](https://www.tutorialspoint.com/python/python_files_io.htm)
# 
# 6. Working with files in Python [https://realpython.com/working-with-files-in-python/](https://realpython.com/working-with-files-in-python/)
# 
# 7. File handling in Python [https://www.geeksforgeeks.org/file-handling-python/](https://www.geeksforgeeks.org/file-handling-python/)
# 
# 8. File operations in Python [https://www.programiz.com/python-programming/file-operation](https://www.programiz.com/python-programming/file-operation)
# 
# ---
# 
# 9. How to read a text file from a URL in Python [https://www.kite.com/python/answers/how-to-read-a-text-file-from-a-url-in-python](https://www.kite.com/python/answers/how-to-read-a-text-file-from-a-url-in-python)
# 
# 10. Downloading files from web using Python [https://www.tutorialspoint.com/downloading-files-from-web-using-python](https://www.tutorialspoint.com/downloading-files-from-web-using-python)
# 
# 11. An Efficient Way to Read Data from the Web Directly into Python without having to download it to your hard drive [https://towardsdatascience.com/an-efficient-way-to-read-data-from-the-web-directly-into-python-a526a0b4f4cb](https://towardsdatascience.com/an-efficient-way-to-read-data-from-the-web-directly-into-python-a526a0b4f4cb)
# 
# ---
# 
# 12. Web Requests with Python (using http and/or https) [https://www.pluralsight.com/guides/web-scraping-with-request-python](https://www.pluralsight.com/guides/web-scraping-with-request-python)
# 
# 13. Troubleshooting certificate errors (really common with https requests) [https://stackoverflow.com/questions/27835619/urllib-and-ssl-certificate-verify-failed-error](https://stackoverflow.com/questions/27835619/urllib-and-ssl-certificate-verify-failed-error)

# ---
# 
# ## Laboratory 7
# 
# **Examine** (click) Laboratory 0 as a webpage at [Laboratory 7.html](http://54.243.252.9/engr-1330-webroot/8-Labs/Lab07/Lab07.html)
# 
# **Download** (right-click, save target as ...) Laboratory 6 as a jupyterlab notebook from [Laboratory 7.ipynb](http://54.243.252.9/engr-1330-webroot/8-Labs/Lab07/Lab07.ipynb)
# 

# <hr><hr>
# 
# ## Exercise Set 7
# 
# **Examine** (click) Exercise Set 6 as a webpage at [Exercise 7.html](http://54.243.252.9/engr-1330-webroot/8-Labs/Lab07/Lab07-TH.html)
# 
# **Download** (right-click, save target as ...) Exercise Set 6 as a jupyterlab notebook at  [Exercise Set 7.ipynb](http://54.243.252.9/engr-1330-webroot/8-Labs/Lab07/Lab07-TH.ipynb)
# 
# 

# In[ ]:




