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
# # 12: Databases and PANDAS
# - Advanced data acquisition (files from a URL)
# - Examples of manual download vs automated
# 

# ---
# ## Objectives
# 1. Additional practice with **dataframe abstraction** as implemented in the Pandas library(module).
#   1. To be able to access and manipulate data within a dataframe
#   2. To be able to obtain basic statistical measures of data within a dataframe
# 2. Access files directly from a URL (ordinary http://... )
#   1. Using a wget-type function
#   2. Using a curl-type function
#   3. Using API keys (future versions)
# 3. Access files directly from a URL (encrypted https://... CA and self signed certificates)
#   1. Using a wget-type function (future versions)
#   2. Using a curl-type function (future versions)
#   3. Using API keys (future versions)

# ---
# 
# ## Access files directly from a URL (ordinary http://... )
# 
# This lesson shows how to get files from a remote computer.   There are several ways to get the files, most importantly  you need the FQDN to the file.

# ### Method: Get the actual file from a remote web server (unencrypted)
# 
# > - You know the FQDN to the file it will be in structure of "http://server-name/.../filename.ext"
# > - The server is running ordinary (unencrypted) web services, i.e. `http://...`
# 
# We will need a module to interface with the remote server. Here we will use ``requests`` , so first we load the module
# 
# > You may need to install the module into your anaconda environment using the anaconda power shell, on my computer the commands are:
# > - sudo -H /opt/jupyterhub/bin/python3 -m pip install requests 
# >
# > Or:
# > - sudo -H /opt/conda/envs/python/bin/python -m pip install requests
# >
# > You will have to do some reading, but with any luck something similar will work for you. 

# In[1]:


import pandas
import requests # Module to process http/https requests


# Now we will generate a ``GET`` request to the remote http server.  I chose to do so using a variable to store the remote URL so I can reuse code in future projects.  The ``GET`` request (an http/https method) is generated with the requests method ``get`` and assigned to an object named ``rget`` -- the name is arbitrary.  Next we extract the file from the ``rget`` object and write it to a local file with the name of the remote file - esentially automating the download process. Then we import the ``pandas`` module.

# In[2]:


remote_url="http://54.243.252.9/engr-1330-webroot/4-Databases/all_quads_gross_evaporation.csv"  # set the url
rget = requests.get(remote_url, allow_redirects=True)  # get the remote resource, follow imbedded links
open('all_quads_gross_evaporation.csv','wb').write(rget.content) # extract from the remote the contents, assign to a local file same name
import pandas as pd # Module to process dataframes (not absolutely needed but somewhat easier than using primatives, and gives graphing tools)


# Now we can read the file contents and check its structure, before proceeding.

# In[3]:


#evapdf = pd.read_csv("all_quads_gross_evaporation.csv",parse_dates=["YYYY-MM"]) # Read the file as a .CSV assign to a dataframe evapdf
evapdf = pandas.read_csv("all_quads_gross_evaporation.csv")
evapdf.head() # check structure


# Structure looks like a spreadsheet as expected; lets plot the time series for cell '911'

# In[4]:


evapdf.plot.line(x='YYYY-MM',y='911') # Plot quadrant 911 evaporation time series 


# In[5]:


evapdf[['911','912']] # pull out columns


# In[6]:


evapdf[evapdf['YYYY-MM'] == "1993-01"][['911','912']]  # get 2 columns from 1993-01 date in YYYY-MM


# ---
# 
# ## Access files directly from a URL (encrypted https://... )(Future Semesters)
# 
# This section shows how to get files from a remote computer that is serving web requests using encryption.  The key indicator is that the remote website is running the `https:\\...` protocol. Most such websites use a 3-rd party certificate authority (CA) and the method is essentially the same as above.  But small-time websites (like ours) use a self-signed certificate which requires us to modify the request to circumvent our computer's security settings.  **Obviously only do so if you know the remote website is legitimate.**    
# 
# Other things to consider:
# - The remote is running `https:\\...` using a self-signed certificate
# - You know the remote is a correct source of the file you desire
# - The file is not executible (you want to verify the file is ASCII UTF-8 or some other similar encoding) if its binary, grab a small portion of the file from your browser and inspect using a hex-editor
# - 

# ---
# 
# ## References
# Overland, B. (2018). Python Without Fear. Addison-Wesley 
# ISBN 978-0-13-468747-6. 
# 
# Grus, Joel (2015). Data Science from Scratch: First Principles with Python O’Reilly
# Media. Kindle Edition.
# 
# Precord, C. (2010) wxPython 2.8 Application Development Cookbook Packt Publishing Ltd. Birmingham , B27 6PA, UK 
# ISBN 978-1-849511-78-0.
# 
# Johnson, J. (2020). Python Numpy Tutorial (with Jupyter and Colab). Retrieved September 15, 2020, from https://cs231n.github.io/python-numpy-tutorial/ 
# 
# Willems, K. (2019). (Tutorial) Python NUMPY Array TUTORIAL. Retrieved September 15, 2020, from https://www.datacamp.com/community/tutorials/python-numpy-tutorial?utm_source=adwords_ppc
# 
# Willems, K. (2017). NumPy Cheat Sheet: Data Analysis in Python. Retrieved September 15, 2020, from https://www.datacamp.com/community/blog/python-numpy-cheat-sheet
# 
# W3resource. (2020). NumPy: Compare two given arrays. Retrieved September 15, 2020, from https://www.w3resource.com/python-exercises/numpy/python-numpy-exercise-28.php
# 
# Sorting https://www.programiz.com/python-programming/methods/list/sort
# 
# 
# https://www.oreilly.com/library/view/relational-theory-for/9781449365431/ch01.html
# 
# https://realpython.com/pandas-read-write-files/#using-pandas-to-write-and-read-excel-files

# In[ ]:




