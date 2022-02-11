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
# # 7.1: Files from the Web (`requests.get ...`)
# - Download files from a remote server
# 
# 

# In[ ]:





# ---
# ## Objectives
# 1. Apply packages to directly obtain a file from a remote server
# 

# ---
# 
# ### Downloading files from websites 
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

# In[1]:


import requests # Module to process http/https requests


# Assuming the requests module loads, lets next clear any existing local (to our machine) copies of the file, in this example, we already have the name, so will just send a system command to delete the file.  This step is mostly for the classroom demonstration - the script will happily clobber existing files.
# 
# > The system command below may be different on windoze!  What's here works on MacOS and Linux.

# In[2]:


import sys # Module to process commands to/from the OS using a shell-type syntax
get_ipython().system(' rm -rf all_quads_gross_evaporation.csv # delete file if it exists')


# Now we will generate a ``GET`` request to the remote http server.  I chose to do so using a variable to store the remote URL so I can reuse code in future projects.  The ``GET`` request (an http/https method) is generated with the requests method ``get`` and assigned to an object named ``rget`` -- the name is arbitrary.  Next we extract the file from the ``rget`` object and write it to a local file with the name of the remote file - esentially automating the download process. 

# In[3]:


remote_url="http://54.243.252.9/engr-1330-webroot/4-Databases/all_quads_gross_evaporation.csv"  # set the url
rget = requests.get(remote_url, allow_redirects=True)  # get the remote resource, follow imbedded links
localfile = open('all_quads_gross_evaporation.csv','wb') # open connection to a local file same name as remote
localfile.write(rget.content) # extract from the remote the contents,insert into the local file same name
localfile.close() # close connection to the local file


# In[4]:


print(type(localfile)) # verify object is an I/O object


# In[5]:


# verify file exists
get_ipython().system(' pwd # list absolute path to script directory')
get_ipython().system(' ls -lah # list directory contents, owner, file sizes ...')


# Now we can list the file contents and check its structure, before proceeding.

# In[6]:


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
# 
# ** Links to URLs with explaination in future revision **
# :::
# 
# Now lets actually read the file into a list for some processing.  We will read it into a null list, and split on the commas (so we will be building a matrix of strings). Then we will print the first few rows and columns.

# In[7]:


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

# In[8]:


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
# 
# #### Reading data from a file.
# 
# Recall earlier we manually downlopaded files for reading as in :
# 
# > To continue our exploration, suppose we want to read from a file, and we know it is a data file - in this section the files we will use are `A.txt`, `B.txt`, and `x.txt` all located > at http://54.243.252.9/engr-1330-webroot/4-Databases/ to follow along download these files to the directory where your script is running.
# >
# > Our task is to determine if $x$ is a solution to $A \cdot x = B$
# >
# >From our problem solving protocol the algorithmic task is
# >
# > 1. Allocate objects to store file contents;
# > 1. Read in A,B, and x from respective files;
# > 2. Echo the inputs (pedagogical in this case);
# > 2. Perform the matrix arithmetic Ax = RHS;
# > 3. Test if RHS == B;
# > 4. Report results;

# Here we will insert the necessary script to automate the process.
# 

# In[9]:


import requests # Module to process http/https requests
remote_url="http://54.243.252.9/engr-1330-webroot/4-Databases/A.txt"  # set the url
rget = requests.get(remote_url, allow_redirects=True)  # get the remote resource, follow imbedded links
localfile = open('A.txt','wb') # open connection to a local file same name as remote
localfile.write(rget.content) # extract from the remote the contents,insert into the local file same name
localfile.close() # close connection to the local file


# Now we read the file contents in a script

# In[10]:


# Code to read A, X, and b - Notice we need somewhere for the data to go, hence the null lists
amatrix = [] # null list to store matrix read
rowNumA = 0
localfile = open("A.txt","r") # connect and read file for MATRIX A
for line in localfile:
    amatrix.append([float(n) for n in line.strip().split()])
    rowNumA += 1
localfile.close() # Disconnect the file
colNumA = len(amatrix[0]) # get the column count


# In[11]:


print('A matrix')
for i in range(0,rowNumA,1):
    print ( (amatrix[i][0:colNumA]))


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
# ## Laboratory 7.1
# 
# **Examine** (click) Laboratory 7 as a webpage at [Laboratory 7.1.html](http://54.243.252.9/engr-1330-webroot/8-Labs/Lab071/Lab071.html)
# 
# **Download** (right-click, save target as ...) Laboratory 7 as a jupyterlab notebook from [Laboratory 7.1.ipynb](http://54.243.252.9/engr-1330-webroot/8-Labs/Lab071/Lab071.ipynb)
# 

# <hr><hr>
# 
# ## Exercise Set 7.1
# 
# **Examine** (click) Exercise Set 7 as a webpage at [Exercise 7.1.html](http://54.243.252.9/engr-1330-webroot/8-Labs/Lab071/Lab071-TH.html)
# 
# **Download** (right-click, save target as ...) Exercise Set 7 as a jupyterlab notebook at  [Exercise Set 7.1.ipynb](http://54.243.252.9/engr-1330-webroot/8-Labs/Lab071/Lab071-TH.ipynb)
# 
# 

# In[ ]:




