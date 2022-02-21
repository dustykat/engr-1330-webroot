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
# # 15: The `matplotlib` package
# - explore different types of plots
# - user defined functions for specific plotting

# ---
# 
# ## Objectives
# - Demonstrate common plot types and their uses
# - Define how to plot experimental data (observations) and theoretical data (model)
#  1. Marker conventions
#  2. Line conventions
#  3. Legends
# 
# ---
# 
# ### About `matplotlib`
# Quoting from: https://matplotlib.org/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py
# 
# `matplotlib.pyplot` is a collection of functions that make matplotlib work like MATLAB. Each pyplot function makes some change to a figure: e.g., creates a figure, creates a plotting area in a figure, plots some lines in a plotting area, decorates the plot with labels, etc.
# 
# In `matplotlib.pyplot` various states are preserved across function calls, so that it keeps track of things like the current figure and plotting area, and the plotting functions are directed to the current axes (please note that "axes" here and in most places in the documentation refers to the axes part of a figure and not the strict mathematical term for more than one axis).
# 
# **Computational thinking (CT)** concepts involved are:
# 
# - `Decomposition` : Break a problem down into smaller pieces; separating plotting from other parts of analysis simplifies maintenace of scripts
# - `Abstraction` : Pulling out specific differences to make one solution work for multiple problems; wrappers around generic plot calls enhances reuse 
# - `Algorithms` : A list of steps that you can follow to finish a task; Often the last step and most important to make professional graphics to justify the expense (of paying you to do engineering) to the client.

# ## Background
# 
# Data are not always numerical. 
# Data can music (audio files), or places on a map (georeferenced attributes files), images (various imge files, e.g. .png, jpeg)
# 
# They can also be categorical into which you can place individuals:
# - The individuals are cartons of ice-cream, and the category is the flavor in the carton
# - The individuals are professional basketball players, and the category is the player's team.
# 
# ---
# 
# ### Line Charts
# A line chart or line plot or line graph or curve chart is a type of chart which displays information as a series of data points called 'markers' connected by straight line segments.
# 
# It is a basic type of chart common in many fields. It is similar to a scatter plot (below) except that the measurement points are **ordered** (typically by their x-axis value) and joined with straight line segments. 
# 
# A line chart is often used to visualize a trend in data over intervals of time – a time series – thus the line is often drawn chronologically. 
# 
# The x-axis spacing is sometimes tricky, hence line charts can unintentionally decieve - so be careful that it is the appropriate chart for your application.  
# 
# We examined line charts in the prior lesson, so lets move on to other useful charts.
# 
# ---
# 
# ### Bar Graphs
# 
# Bar charts (graphs) are good display tools to graphically represent categorical information.
# The bars are evenly spaced and of constant width. 
# The height/length of each bar is proportional to the `relative frequency` of the corresponding category.
# 
# `Relative frequency` is the ratio of how many things in the category to how many things in the whole collection.
# 
# The example below uses `matplotlib` to create a box plot for the ice cream analogy, the example is adapted from an example at https://www.geeksforgeeks.org/bar-plot-in-matplotlib/

# In[1]:


ice_cream = {'Chocolate':16, 'Strawberry':5, 'Vanilla':9} # build a data model 
import matplotlib.pyplot # the python plotting library

flavors = list(ice_cream.keys()) # make a list object based on flavors
cartons = list(ice_cream.values()) # make a list object based on carton count -- assumes 1:1 association!

myfigure = matplotlib.pyplot.figure(figsize = (10,5)) # generate a object from the figure class, set aspect ratio

# Built the plot
matplotlib.pyplot.bar(flavors, cartons, color ='teal', width = 0.4) 
matplotlib.pyplot.xlabel("Flavors") 
matplotlib.pyplot.ylabel("No. of Cartons in Stock") 
matplotlib.pyplot.title("Current Ice Cream in Storage") 
matplotlib.pyplot.show() 


# ---
# 
# Lets tidy up the script so it is more understandable, a small change in the import statement makes a simpler to read (for humans) script - also changed the bar colors just 'cause!

# In[2]:


ice_cream = {'Chocolate':16, 'Strawberry':5, 'Vanilla':9} # build a data model 
import matplotlib.pyplot as plt # the python plotting library

flavors = list(ice_cream.keys()) # make a list object based on flavors
cartons = list(ice_cream.values()) # make a list object based on carton count -- assumes 1:1 association!

myfigure = plt.figure(figsize = (10,5)) # generate a object from the figure class, set aspect ratio

# Built the plot
plt.bar(flavors, cartons, color ='lightblue', width = 0.4) 
plt.xlabel("Flavors") 
plt.ylabel("No. of Cartons in Stock") 
plt.title("Current Ice Cream in Storage") 
plt.show() 


# ---
# 
# Now lets deconstruct the script a bit:
# 
#     ice_cream = {'Chocolate':16, 'Strawberry':5, 'Vanilla':9} # build a data model 
#     import matplotlib.pyplot as plt # the python plotting library
# 
#     flavors = list(ice_cream.keys()) # make a list object based on flavors
#     cartons = list(ice_cream.values()) # make a list object based on carton count -- assumes 1:1 association!
# 
# This part of the code creates a dictionary object, keys are the flavors, values are the carton counts (not the best way, but good for our learning needs).  Next we import the python plotting library from `matplotlib` and name it **plt** to keep the script a bit easier to read.
# 
# 
# 
# Next we use the list method to create two lists from the dictionary, **flavors** and **cartons**.  Keep this in mind plotting is usually done on lists, so we need to prepare the structures properly.
# 
# The next statement
# 
#     myfigure = plt.figure(figsize = (10,5)) # generate a object from the figure class, set aspect ratio
#     
# Uses the figure class in **pyplot** from **matplotlib** to make a figure object named myfigure, the plot is built into this object.  Every call to a method in `plt` adds content to `myfigure` until we send the instruction to render the plot (`plt.show()`)
# 
# The next portion of the script builds the plot:
#     
#     plt.bar(flavors, cartons, color ='orange', width = 0.4) # Build a bar chart, plot series flavor on x-axis, plot series carton on y-axis.  Make the bars orange, set bar width (units unspecified)
#     plt.xlabel("Flavors") # Label the x-axis as Flavors
#     plt.ylabel("No. of Cartons in Stock") # Label the x-axis as Flavors
#     plt.title("Current Ice Cream in Storage") # Title for the whole plot
#     
# This last statement renders the plot to the graphics device (probably localhost in the web browser)
# 
#     plt.show() 
#     
# ---
# 
# Now lets add another set of categories to the plot and see what happens

# In[3]:


ice_cream = {'Chocolate':16, 'Strawberry':5, 'Vanilla':9} # build a data model 
eaters = {'Cats':6, 'Dogs':5, 'Ferrets':19} # build a data model 
import matplotlib.pyplot as plt # the python plotting library

flavors = list(ice_cream.keys()) # make a list object based on flavors
cartons = list(ice_cream.values()) # make a list object based on carton count -- assumes 1:1 association!

animals = list(eaters.keys()) 
beasts = list(eaters.values()) 
myfigure = plt.figure(figsize = (10,5)) # generate a object from the figure class, set aspect ratio

# Built the plot
plt.bar(flavors, cartons, color ='orange', width = 0.4) 
plt.bar(animals, beasts, color ='green', width = 0.4) 
plt.xlabel("Flavors") 
plt.ylabel("Counts: Cartons and Beasts") 
plt.title("Current Ice Cream in Storage") 
plt.show() 


# ---
# 
# Now suppose we want horizontal bars we can search pyplot for such a thing.  If one types horizontal bar chart into the pyplot search engine there is a link that leads to:
# 
# ![](SearchPyplot.png)
# 
# Which has the right look!  If we examine the script there is a method called `barh` so lets try that.
# 
# ```{note} 
# Use the search engines to find out things you need to accomplish a task.
# ```

# In[4]:


ice_cream = {'Chocolate':16, 'Strawberry':5, 'Vanilla':9} # build a data model 
eaters = {'Cats':6, 'Dogs':5, 'Ferrets':19} # build a data model 
import matplotlib.pyplot as plt # the python plotting library

flavors = list(ice_cream.keys()) # make a list object based on flavors
cartons = list(ice_cream.values()) # make a list object based on carton count -- assumes 1:1 association!

animals = list(eaters.keys()) 
beasts = list(eaters.values()) 
myfigure = plt.figure(figsize = (10,5)) # generate a object from the figure class, set aspect ratio

# Built the plot
plt.barh(flavors, cartons, color ='orange') 
plt.barh(animals, beasts, color ='green') 
plt.xlabel("Flavors") 
plt.ylabel("Counts: Cartons and Beasts") 
plt.title("Current Ice Cream in Storage") 
plt.show() 


# ---
# 
# Now using pandas, we can build bar charts a bit easier.

# In[5]:


import pandas as pd

my_data = {
    "Flavor": ['Chocolate', 'Strawberry', 'Vanilla'],
    "Number of Cartons": [16, 5, 9]
          }
df = pd.DataFrame(my_data)
df.head()


# In[6]:


df.plot.bar(x='Flavor', y='Number of Cartons', color='magenta' )


# In[7]:


df.plot.bar(x='Flavor', y='Number of Cartons', color="red") # rotate the category labels


# In[8]:


import numpy as np 
import matplotlib.pyplot as plt  
  
   
# creating the dataset 
data = {'C':20, 'C++':15, 'Java':30,  
        'Python':35} 
courses = list(data.keys()) 
values = list(data.values()) 
   
fig = plt.figure(figsize = (10, 5)) 
  
# creating the bar plot 
plt.bar(courses, values, color ='maroon',  
        width = 0.4) 
  
plt.xlabel("Courses offered") 
plt.ylabel("No. of students enrolled") 
plt.title("Students enrolled in different courses") 
plt.show() 


# --- 
# 
# ### Scatter Plots
# A scatter plot (also called a scatterplot, scatter graph, scatter chart, scattergram, or scatter diagram) is a type of plot or mathematical diagram using Cartesian coordinates to display values for typically two variables for a set of data. If the points are coded (color/shape/size), one additional variable can be displayed. The data are displayed as a collection of points, each having the value of one variable determining the position on the horizontal axis and the value of the other variable determining the position on the vertical axis.
# 
# A scatter plot can be used either when one continuous variable that is under the control of the experimenter and the other depends on it or when both continuous variables are independent. If a parameter exists that is systematically incremented and/or decremented by the other, it is called the control parameter or independent variable and is customarily plotted along the horizontal axis. The measured or dependent variable is customarily plotted along the vertical axis. If no dependent variable exists, either type of variable can be plotted on either axis and a scatter plot will illustrate only the degree of correlation (not causation) between two variables.
# 
# A scatter plot can suggest various kinds of correlations between variables with a certain confidence interval. For example, weight and height, weight would be on y axis and height would be on the x axis. 
# Correlations may be positive (rising), negative (falling), or null (uncorrelated). 
# If the pattern of dots slopes from lower left to upper right, it indicates a positive correlation between the variables being studied. 
# If the pattern of dots slopes from upper left to lower right, it indicates a negative correlation. 
# 
# A line of best fit (alternatively called 'trendline') can be drawn in order to study the relationship between the variables. An equation for the correlation between the variables can be determined by established best-fit procedures. For a linear correlation, the best-fit procedure is known as linear regression and is guaranteed to generate a correct solution in a finite time. No universal best-fit procedure is guaranteed to generate a  solution for arbitrary relationships. 
# A scatter plot is also very useful when we wish to see how two comparable data sets agree and to show nonlinear relationships between variables.
# 
# Furthermore, if the data are represented by a mixture model of simple relationships, these relationships will be visually evident as superimposed patterns.
# 
# Scatter charts can be built in the form of bubble, marker, or/and line charts.
# 
# Much of the above is verbatim/adapted from: https://en.wikipedia.org/wiki/Scatter_plot
# 
# The example below uses a database table from [galton_subset.csv](http://54.243.252.9/engr-1330-webroot/1-Lessons/Lesson12/galton_subset.csv)

# In[9]:


# Example 1.  A data file containing heights of fathers, mothers, and sons is to be examined
df = pd.read_csv('galton_subset.csv')
df['child']= df['son'] ; df.drop('son', axis=1, inplace = True) # rename son to child - got to imagine there are some daughters
df.head()


# In[10]:


# build some lists
daddy = df['father'] ; mommy = df['mother'] ; baby = df['child']


# In[11]:


myfamily = plt.figure(figsize = (10, 10)) # build a square drawing canvass from figure class
plt.scatter(baby, daddy, c='red') # basic scatter plot
plt.show()


# In[12]:


# Looks lousy, needs some labels
myfamily = plt.figure(figsize = (10, 10)) # build a square drawing canvass from figure class
plt.scatter(baby, daddy, c='red' , label='Father') # one plot series
plt.scatter(baby, mommy, c='blue', label='Mother') # two plot series
plt.xlabel("Child's height")
plt.ylabel("Parents' height")
plt.legend()
plt.show() # render the two plots


# In[ ]:





# In[13]:


# Repeat in pandas - The dataframe already is built
df.plot.scatter(x="child", y="father")


# In[14]:


ax = df.plot.scatter(x="child", y="father", c="red", label='Father')
df.plot.scatter(x="child", y="mother", c="blue", label='Mother', ax=ax)

ax.set_xlabel("Child's height")
ax.set_ylabel("Parents' Height")


# In[15]:


df.plot.scatter(x="child", y="father")


# --- 
# 
# ## Histograms
# 
# Quoting from https://en.wikipedia.org/wiki/Histogram
# 
# "A histogram is an approximate representation of the distribution of numerical data. It was first introduced by Karl Pearson.[1] To construct a histogram, the first step is to "bin" (or "bucket") the range of values—that is, divide the entire range of values into a series of intervals—and then count how many values fall into each interval. The bins are usually specified as consecutive, non-overlapping intervals of a variable. The bins (intervals) must be adjacent, and are often (but not required to be) of equal size.
# 
# If the bins are of equal size, a rectangle is erected over the bin with height proportional to the frequency—the number of cases in each bin. A histogram may also be normalized to display "relative" frequencies. It then shows the proportion of cases that fall into each of several categories, with the sum of the heights equaling 1.
# 
# However, bins need not be of equal width; in that case, the erected rectangle is defined to have its area proportional to the frequency of cases in the bin. The vertical axis is then not the frequency but frequency density—the number of cases per unit of the variable on the horizontal axis. Examples of variable bin width are displayed on Census bureau data below.
# 
# As the adjacent bins leave no gaps, the rectangles of a histogram touch each other to indicate that the original variable is continuous.
# 
# Histograms give a rough sense of the density of the underlying distribution of the data, and often for density estimation: estimating the probability density function of the underlying variable. The total area of a histogram used for probability density is always normalized to 1. If the length of the intervals on the x-axis are all 1, then a histogram is identical to a relative frequency plot.
# 
# A histogram can be thought of as a simplistic kernel density estimation, which uses a kernel to smooth frequencies over the bins. This yields a smoother probability density function, which will in general more accurately reflect distribution of the underlying variable. The density estimate could be plotted as an alternative to the histogram, and is usually drawn as a curve rather than a set of boxes. Histograms are nevertheless preferred in applications, when their statistical properties need to be modeled. The correlated variation of a kernel density estimate is very difficult to describe mathematically, while it is simple for a histogram where each bin varies independently.
# 
# An alternative to kernel density estimation is the average shifted histogram, which is fast to compute and gives a smooth curve estimate of the density without using kernels.
# 
# The histogram is one of the seven basic tools of quality control.
# 
# Histograms are sometimes confused with bar charts. A histogram is used for continuous data, where the bins represent ranges of data, while a bar chart is a plot of categorical variables. Some authors recommend that bar charts have gaps between the rectangles to clarify the distinction."
# 
# The example below uses a database table from [top_movies.csv](http://54.243.252.9/engr-1330-webroot/1-Lessons/Lesson12/top_movies.csv)

# In[16]:


import pandas as pd

df = pd.read_csv('top_movies.csv')
df.head()


# In[17]:


df[["Gross"]].hist()


# In[ ]:





# In[18]:


df[["Gross"]].hist(bins=100)


# In[19]:


df.describe()


# ## Summary
# 
# - line charts (previous lesson)
# - bar charts
# - scatterplots
# - histograms
# 
# ## References
# 
# 1. Grus, Joel (2015-04-14). Data Science from Scratch: First Principles with Python
# (Kindle Locations 1190-1191). O'Reilly Media. Kindle Edition. 
# 
# 2. Call Expressions in "Adhikari, A. and DeNero, J. Computational and Inferential Thinking The Foundations of Data Science" https://www.inferentialthinking.com/chapters/03/3/Calls.html
# 
# 3. Functions and Tables in "Adhikari, A. and DeNero, J. Computational and Inferential Thinking The Foundations of Data Science" https://www.inferentialthinking.com/chapters/08/Functions_and_Tables.html
# 
# 4. Visualization in "Adhikari, A. and DeNero, J. Computational and Inferential Thinking The Foundations of Data Science" https://www.inferentialthinking.com/chapters/07/Visualization.html
# 
# 5. Documentation; The Python Standard Library; 9. Numeric and Mathematical Modules https://docs.python.org/2/library/math.html
# 
# 6. https://matplotlib.org/gallery/lines_bars_and_markers/horizontal_barchart_distribution.html?highlight=horizontal%20bar%20chart
# 
# 7. https://www.geeksforgeeks.org/bar-plot-in-matplotlib/

# ## Addendum (Scripts that are Interactive)
# 
# :::{note}
# The addendum is intended for in-class demonstration
# :::

# In[20]:


# python script to illustrate plotting
# CODE BELOW IS ADAPTED FROM:
# Grus, Joel (2015-04-14). Data Science from Scratch: First Principles with Python
# (Kindle Locations 1190-1191). O'Reilly Media. Kindle Edition. 
#
from matplotlib import pyplot as plt # import the plotting library from matplotlibplt.show()

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]  # define one list for years
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3] # and another one for Gross Domestic Product (GDP)
plt.plot( years, gdp, color ='green', marker ='o', linestyle ='solid') # create a line chart, years on x-axis, gdp on y-axis
                                                                       # what if "^", "P", "*" for marker?
                                                                       # what if "red" for color?  
                                                                       # what if "dashdot", '--' for linestyle?  


plt.title("Nominal GDP")# add a title
plt.ylabel("Billions of $")# add a label to the x and y-axes
plt.xlabel("Year")
plt.show() # display the plot


# Now lets put the plotting script into a function so we can make line charts of any two numeric lists

# In[21]:


def plotAline(list1,list2,strx,stry,strtitle): # plot list1 on x, list2 on y, xlabel, ylabel, title
    from matplotlib import pyplot as plt # import the plotting library from matplotlibplt.show()
    plt.plot( list1, list2, color ='green', marker ='o', linestyle ='solid') # create a line chart, years on x-axis, gdp on y-axis
    plt.title(strtitle)# add a title
    plt.ylabel(stry)# add a label to the x and y-axes
    plt.xlabel(strx)
    plt.show() # display the plot
    return #null return


# In[22]:


# wrapper
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]  # define two lists years and gdp
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]
print(type(years[0]))
print(type(gdp[0]))
plotAline(years,gdp,"Year","Billions of $","Nominal GDP")


# ## Example 
# Use the plotting script and create a function that draws a straight line between two points.

# ```
#     def Line():
#     from matplotlib import pyplot as plt # import the plotting library from matplotlibplt.show()
#     x1 = input('Please enter x value for point 1')
#     y1 = input('Please enter y value for point 1')
#     x2 = input('Please enter x value for point 2')
#     y2 = input('Please enter y value for point 2')
#     xlist = [x1,x2]
#     ylist = [y1,y2]
#     plt.plot( xlist, ylist, color ='orange', marker ='*', linestyle ='solid') 
#     #plt.title(strtitle)# add a title
#     plt.ylabel("Y-axis")# add a label to the x and y-axes
#     plt.xlabel("X-axis")
#     plt.show() # display the plot
#     return #null return
# ```

# ---
# 
# ## Laboratory 15
# 
# **Examine** (click) Laboratory 15 as a webpage at [Laboratory 15.html](http://54.243.252.9/engr-1330-webroot/8-Labs/Lab15/Lab15.html)
# 
# **Download** (right-click, save target as ...) Laboratory 15 as a jupyterlab notebook from [Laboratory 15.ipynb](http://54.243.252.9/engr-1330-webroot/8-Labs/Lab15/Lab15.ipynb)
# 

# <hr><hr>
# 
# ## Exercise Set 15
# 
# **Examine** (click) Exercise Set 15 as a webpage at [Exercise 15.html](http://54.243.252.9/engr-1330-webroot/8-Labs/Lab15/Lab15-TH.html)
# 
# **Download** (right-click, save target as ...) Exercise Set 15 as a jupyterlab notebook at  [Exercise Set 7.1.ipynb](http://54.243.252.9/engr-1330-webroot/8-Labs/Lab15/Lab15-TH.ipynb)
# 
# 

# ## References

# In[ ]:




