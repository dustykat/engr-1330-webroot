**Download** (right-click, save target as ...) this page as a jupyterlab notebook from:

[Lab9](https://atomickitty.ddns.net:8000/user/sensei/files/engr-1330-webroot/engr-1330-webbook/ctds-psuedocourse/docs/8-Labs/Lab8/Lab9_Dev.ipynb?_xsrf=2%7C1b4d47c3%7C0c3aca0c53606a3f4b71c448b09296ae%7C1623531240)

___

# <font color=darkred>Laboratory 9: Matplotlib for Jam! </font>


```python
# Preamble script block to identify host, user, and kernel
import sys
! hostname
! whoami
print(sys.executable)
print(sys.version)
print(sys.version_info)
```

    atomickitty
    sensei
    /opt/jupyterhub/bin/python3
    3.8.5 (default, Jul 28 2020, 12:59:40) 
    [GCC 9.3.0]
    sys.version_info(major=3, minor=8, micro=5, releaselevel='final', serial=0)


## Full name: 
## R#: 
## Title of the notebook:
## Date:
___

![](https://envato-shoebox-0.imgix.net/485c/f17a-904a-4a3d-a3aa-3c09708b07ea/rykibreadsa1.jpg?auto=compress%2Cformat&fit=max&mark=https%3A%2F%2Felements-assets.envato.com%2Fstatic%2Fwatermark2.png&markalign=center%2Cmiddle&markalpha=18&w=700&s=95061aa27f6c3a88147f5c13061cf255)

![](https://matplotlib.org/1.4.2/mpl_examples/api/logo2.hires.png) <br>

## <font color=purple>Matplotlip and Visual Display of Data</font>

This lesson will introduce the `matplotlib` external module package, and examine how to construct
line charts, scatter plots, bar charts, and histograms using methods in `matplotlib` and `pandas`

The theory of histograms will appear in later lessons, here we only show how to construct one using `matplotlib`

### <font color=purple>About `matplotlib`</font>

Quoting from: https://matplotlib.org/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py

`matplotlib.pyplot` is a collection of functions that make matplotlib work like MATLAB. Each pyplot function makes some change to a figure: e.g., creates a figure, creates a plotting area in a figure, plots some lines in a plotting area, decorates the plot with labels, etc.

In `matplotlib.pyplot` various states are preserved across function calls, so that it keeps track of things like the current figure and plotting area, and the plotting functions are directed to the current axes (please note that "axes" here and in most places in the documentation refers to the axes part of a figure and not the strict mathematical term for more than one axis).

### <font color=purple>Background</font>

Data are not always numerical. 
Data can music (audio files), or places on a map (georeferenced attributes files), images (various imge files, e.g. .png, jpeg)

They can also be categorical into which you can place individuals:
- The individuals are cartons of ice-cream, and the category is the flavor in the carton
- The individuals are professional basketball players, and the category is the player's team.

### <font color=purple>Bar Graphs</font>

Bar charts (graphs) are good display tools to graphically represent categorical information.
The bars are evenly spaced and of constant width. 
The height/length of each bar is proportional to the `relative frequency` of the corresponding category.

`Relative frequency` is the ratio of how many things in the category to how many things in the whole collection.

The example below uses `matplotlib` to create a box plot for the ice cream analogy, the example is adapted from an example at https://www.geeksforgeeks.org/bar-plot-in-matplotlib/


```python
ice_cream = {'Chocolate':16, 'Strawberry':5, 'Vanilla':9} # build a data model 
import matplotlib.pyplot # the python plotting library

flavors = list(ice_cream.keys()) # make a list object based on flavors
cartons = list(ice_cream.values()) # make a list object based on carton count -- assumes 1:1 association!

myfigure = matplotlib.pyplot.figure(figsize = (10,5)) # generate a object from the figure class, set aspect ratio

# Built the plot
matplotlib.pyplot.bar(flavors, cartons, color ='maroon', width = 0.4) 
matplotlib.pyplot.xlabel("Flavors") 
matplotlib.pyplot.ylabel("No. of Cartons in Stock") 
matplotlib.pyplot.title("Current Ice Cream in Storage") 
matplotlib.pyplot.show() 
```


    
![png](output_8_0.png)
    


Lets tidy up the script so it is more understandable, a small change in the import statement makes a simpler to read (for humans) script - also changed the bar colors just 'cause!


```python
ice_cream = {'Chocolate':16, 'Strawberry':5, 'Vanilla':9} # build a data model 
import matplotlib.pyplot as plt # the python plotting library

flavors = list(ice_cream.keys()) # make a list object based on flavors
cartons = list(ice_cream.values()) # make a list object based on carton count -- assumes 1:1 association!

myfigure = plt.figure(figsize = (10,5)) # generate a object from the figure class, set aspect ratio

# Built the plot
plt.bar(flavors, cartons, color ='orange', width = 0.4) 
plt.xlabel("Flavors") 
plt.ylabel("No. of Cartons in Stock") 
plt.title("Current Ice Cream in Storage") 
plt.show() 
```


    
![png](output_10_0.png)
    


Using pandas, we can build bar charts a bit easier.


```python
import pandas as pd

my_data = {
    "Flavor": ['Chocolate', 'Strawberry', 'Vanilla'],
    "Number of Cartons": [16, 5, 9]
          }
df = pd.DataFrame(my_data)
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Flavor</th>
      <th>Number of Cartons</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Chocolate</td>
      <td>16</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Strawberry</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Vanilla</td>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.plot.bar(x='Flavor', y='Number of Cartons', color='magenta' )
```




    <AxesSubplot:xlabel='Flavor'>




    
![png](output_13_1.png)
    



```python
df.plot.bar(x='Flavor', y='Number of Cartons', color="red") # rotate the category labels
```




    <AxesSubplot:xlabel='Flavor'>




    
![png](output_14_1.png)
    


<hr>

### Example- Language Bars!

Consider the data set "data" defined as

    data = {'C':20, 'C++':15, 'Java':30, 'Python':35} 
    
which lists student count by programming language in some school.

Produce a bar chart of number of students in each language, where language is the classification, and student count is the variable.



```python
# Code and run your solution here

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

```


    
![png](output_16_0.png)
    


### Plot it as a horizontal bar chart:


```python
# Code and run your solution here

# creating the dataset 
data = {'C':20, 'C++':15, 'Java':30,  
        'Python':35} 
courses = list(data.keys()) 
values = list(data.values()) 
   
fig = plt.figure(figsize = (10, 5)) 
  
# creating the bar plot 
plt.barh(courses, values, color ='maroon',  height = 0.4) 
  
plt.xlabel("Courses offered") 
plt.ylabel("No. of students enrolled") 
plt.title("Students enrolled in different courses") 
plt.show() 
```


    
![png](output_18_0.png)
    


___
### <font color=purple>Line Charts</font>

A line chart or line plot or line graph or curve chart is a type of chart which displays information as a series of data points called 'markers' connected by straight line segments.

It is a basic type of chart common in many fields. It is similar to a scatter plot (below) except that the measurement points are **ordered** (typically by their x-axis value) and joined with straight line segments. 

A line chart is often used to visualize a trend in data over intervals of time – a time series – thus the line is often drawn chronologically. 

The x-axis spacing is sometimes tricky, hence line charts can unintentionally decieve - so be careful that it is the appropriate chart for your application.  

___
### Example- Speed vs Time

Consider the experimental data below

|Elapsed Time (s)|Speed (m/s)|
|---:|---:|
|0 |0|
|1.0 |3|
|2.0 |7|
|3.0 |12|
|4.0 |20|
|5.0 |30|
|6.0 | 45.6| 

Show the relationship between time and speed.  Is the relationship indicating acceleration? How much?


```python
# Create two lists; time  and speed.
time = [0,1.0,2.0,3.0,4.0,5.0,6.0]
speed = [0,3,7,12,20,30,45.6]
```


```python
# Create a line chart of speed on y axis and time on x axis
mydata = plt.figure(figsize = (10,5)) # build a square drawing canvass from figure class
plt.plot(time, speed, c='red', marker='v',linewidth=1) # basic line plot
plt.show()
```


    
![png](output_21_0.png)
    


From examination of  the plot, estimate the speed at time t = 5.0 (eyeball estimate)

<hr>

### Example- Add a linear fit
Using the same series from Exercise 1, Plot the speed vs time (speed on y-axis, time on x-axis) using a line plot. Plot a second line based on the linear model 

$$y = mx + b$$, 

where $$b=0~\text{and}~m=7.6$$.



```python
# Code and run your solution here:
def ymodel(xmodel,slope,intercept):
    ymodel = slope*xmodel+intercept
    return(ymodel)

yseries = []
slope = 7.6
intercept = 0.0

for i in range(0,len(time)):
    yseries.append(ymodel(time[i],slope,intercept))
# Create a markers only line chart
mydata = plt.figure(figsize = (10,5)) # build a square drawing canvass from figure class
plt.plot(time, speed, c='red', marker='^',linewidth=0.5) # basic line plot
plt.plot(time, yseries, c='blue') 
plt.show()
```


    
![png](output_24_0.png)
    


<hr>

### Example- Find a better fit
Using trial and error try to improve the 'fit' of the model, by adjusting values of $$m~\text{and}~b$$.


```python
# Code and run your solution here:
yseries = []
slope = 7.6
intercept = -8.0

for i in range(0,len(time)):
    yseries.append(ymodel(time[i],slope,intercept))
# Create a markers only line chart
mydata = plt.figure(figsize = (10,5)) # build a square drawing canvass from figure class
plt.plot(time, speed, c='red', marker='^',linewidth=0) # basic scatter plot
plt.plot(time, yseries, c='blue') 
plt.show()
```


    
![png](output_26_0.png)
    


___
### <font color=purple>Scatter Plots</font>
 
A scatter plot (also called a scatterplot, scatter graph, scatter chart, scattergram, or scatter diagram) is a type of plot or mathematical diagram using Cartesian coordinates to display values for typically two variables for a set of data. If the points are coded (color/shape/size), one additional variable can be displayed. The data are displayed as a collection of points, each having the value of one variable determining the position on the horizontal axis and the value of the other variable determining the position on the vertical axis.

A scatter plot can be used either when one continuous variable that is under the control of the experimenter and the other depends on it or when both continuous variables are independent. If a parameter exists that is systematically incremented and/or decremented by the other, it is called the control parameter or independent variable and is customarily plotted along the horizontal axis. The measured or dependent variable is customarily plotted along the vertical axis. If no dependent variable exists, either type of variable can be plotted on either axis and a scatter plot will illustrate only the degree of correlation (not causation) between two variables.

A scatter plot can suggest various kinds of correlations between variables with a certain confidence interval. For example, weight and height, weight would be on y axis and height would be on the x axis. 
Correlations may be positive (rising), negative (falling), or null (uncorrelated). 
If the pattern of dots slopes from lower left to upper right, it indicates a positive correlation between the variables being studied. 
If the pattern of dots slopes from upper left to lower right, it indicates a negative correlation. 

A line of best fit (alternatively called 'trendline') can be drawn in order to study the relationship between the variables. An equation for the correlation between the variables can be determined by established best-fit procedures. For a linear correlation, the best-fit procedure is known as linear regression and is guaranteed to generate a correct solution in a finite time. No universal best-fit procedure is guaranteed to generate a  solution for arbitrary relationships. 
A scatter plot is also very useful when we wish to see how two comparable data sets agree and to show nonlinear relationships between variables.

Furthermore, if the data are represented by a mixture model of simple relationships, these relationships will be visually evident as superimposed patterns.

Scatter charts can be built in the form of bubble, marker, or/and line charts.

Much of the above is verbatim/adapted from: https://en.wikipedia.org/wiki/Scatter_plot

___ 
### Example- Examine the dataset with heights of fathers, mothers and sons


```python
df = pd.read_csv('galton_subset.csv')
df['child']= df['son'] ; df.drop('son', axis=1, inplace = True) # rename son to child - got to imagine there are some daughters
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>father</th>
      <th>mother</th>
      <th>child</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>78.5</td>
      <td>67.0</td>
      <td>73.2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>75.5</td>
      <td>66.5</td>
      <td>73.5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>75.0</td>
      <td>64.0</td>
      <td>71.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>75.0</td>
      <td>64.0</td>
      <td>70.5</td>
    </tr>
    <tr>
      <th>4</th>
      <td>75.0</td>
      <td>58.5</td>
      <td>72.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# build some lists
dad = df['father'] ; mom = df['mother'] ; son = df['child']
```


```python
myfamily = plt.figure(figsize = (10, 10)) # build a square drawing canvass from figure class
plt.scatter(son, dad, c='red') # basic scatter plot
plt.show()
```


    
![png](output_31_0.png)
    



```python
# Looks lousy, needs some labels
myfamily = plt.figure(figsize = (10, 10)) # build a square drawing canvass from figure class
plt.scatter(son, dad, c='red' , label='Father') # one plot series
plt.scatter(son, mom, c='blue', label='Mother') # two plot series
plt.xlabel("Child's height")
plt.ylabel("Parents' height")
plt.legend()
plt.show() # render the two plots
```


    
![png](output_32_0.png)
    



```python
# Repeat in pandas - The dataframe already is built
df.plot.scatter(x="child", y="father")
```




    <AxesSubplot:xlabel='child', ylabel='father'>




    
![png](output_33_1.png)
    



```python
ax = df.plot.scatter(x="child", y="father", c="red", label='Father')
df.plot.scatter(x="child", y="mother", c="blue", label='Mother', ax=ax)

ax.set_xlabel("Child's height")
ax.set_ylabel("Parents' Height")
```




    Text(0, 0.5, "Parents' Height")




    
![png](output_34_1.png)
    


___
### <font color=purple>Histograms</font>
 

Quoting from https://en.wikipedia.org/wiki/Histogram

"A histogram is an approximate representation of the distribution of numerical data. It was first introduced by Karl Pearson.[1] To construct a histogram, the first step is to "bin" (or "bucket") the range of values—that is, divide the entire range of values into a series of intervals—and then count how many values fall into each interval. The bins are usually specified as consecutive, non-overlapping intervals of a variable. The bins (intervals) must be adjacent, and are often (but not required to be) of equal size.

If the bins are of equal size, a rectangle is erected over the bin with height proportional to the frequency—the number of cases in each bin. A histogram may also be normalized to display "relative" frequencies. It then shows the proportion of cases that fall into each of several categories, with the sum of the heights equaling 1.

However, bins need not be of equal width; in that case, the erected rectangle is defined to have its area proportional to the frequency of cases in the bin. The vertical axis is then not the frequency but frequency density—the number of cases per unit of the variable on the horizontal axis. Examples of variable bin width are displayed on Census bureau data below.

As the adjacent bins leave no gaps, the rectangles of a histogram touch each other to indicate that the original variable is continuous.

Histograms give a rough sense of the density of the underlying distribution of the data, and often for density estimation: estimating the probability density function of the underlying variable. The total area of a histogram used for probability density is always normalized to 1. If the length of the intervals on the x-axis are all 1, then a histogram is identical to a relative frequency plot.

A histogram can be thought of as a simplistic kernel density estimation, which uses a kernel to smooth frequencies over the bins. This yields a smoother probability density function, which will in general more accurately reflect distribution of the underlying variable. The density estimate could be plotted as an alternative to the histogram, and is usually drawn as a curve rather than a set of boxes. Histograms are nevertheless preferred in applications, when their statistical properties need to be modeled. The correlated variation of a kernel density estimate is very difficult to describe mathematically, while it is simple for a histogram where each bin varies independently.

An alternative to kernel density estimation is the average shifted histogram, which is fast to compute and gives a smooth curve estimate of the density without using kernels.

The histogram is one of the seven basic tools of quality control.

Histograms are sometimes confused with bar charts. A histogram is used for continuous data, where the bins represent ranges of data, while a bar chart is a plot of categorical variables. Some authors recommend that bar charts have gaps between the rectangles to clarify the distinction."

___
### Example- Explore the "top_movies" dataset and draw histograms for Gross and Year.


```python
import pandas as pd

df = pd.read_csv('top_movies.csv')
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Title</th>
      <th>Studio</th>
      <th>Gross</th>
      <th>Gross (Adjusted)</th>
      <th>Year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Star Wars: The Force Awakens</td>
      <td>Buena Vista (Disney)</td>
      <td>906723418</td>
      <td>906723400</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Avatar</td>
      <td>Fox</td>
      <td>760507625</td>
      <td>846120800</td>
      <td>2009</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Titanic</td>
      <td>Paramount</td>
      <td>658672302</td>
      <td>1178627900</td>
      <td>1997</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Jurassic World</td>
      <td>Universal</td>
      <td>652270625</td>
      <td>687728000</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Marvel's The Avengers</td>
      <td>Buena Vista (Disney)</td>
      <td>623357910</td>
      <td>668866600</td>
      <td>2012</td>
    </tr>
  </tbody>
</table>
</div>




```python
df[["Gross"]].hist()
```




    array([[<AxesSubplot:title={'center':'Gross'}>]], dtype=object)




    
![png](output_38_1.png)
    



```python
df[["Year"]].hist()
```




    array([[<AxesSubplot:title={'center':'Year'}>]], dtype=object)




    
![png](output_39_1.png)
    



```python
df[["Gross"]].hist(bins=100)
```




    array([[<AxesSubplot:title={'center':'Gross'}>]], dtype=object)




    
![png](output_40_1.png)
    


___
## <font color=orange>This is a Matplotlib Cheat Sheet</font>

![](https://python-graph-gallery.com/wp-content/uploads/Matplotlib_cheatsheet_datacamp.png)


___
![](https://media2.giphy.com/media/5nj4ZZWl6QwneEaBX4/source.gif) <br>

*Here are some of the resources used for creating this notebook:* 

- __"Discrete distribution as horizontal bar chart"__ available at *https://matplotlib.org/stable/gallery/lines_bars_and_markers/horizontal_barchart_distribution.html<br>
- __"Bar Plot in Matplotlib"__ available at *https://www.geeksforgeeks.org/bar-plot-in-matplotlib/<br>


*Here are some great reads on this topic:* 
- __"Python | Introduction to Matplotlib"__ available at *https://www.geeksforgeeks.org/python-introduction-matplotlib/<br>
- __"Visualization with Matplotlib"__ available at *https://jakevdp.github.io/PythonDataScienceHandbook/04.00-introduction-to-matplotlib.html <br>
- __"Introduction to Matplotlib — Data Visualization in Python"__ by __Ehi Aigiomawu__ available at *https://heartbeat.fritz.ai/introduction-to-matplotlib-data-visualization-in-python-d9143287ae39 <br>
- __"Python Plotting With Matplotlib (Guide)"__ by __Brad Solomon__ available at *https://realpython.com/python-matplotlib-guide/ <br>


*Here are some great videos on these topics:* 
- __"Matplotlib Tutorial (Part 1): Creating and Customizing Our First Plots"__ by __Corey Schafer__ available at *https://www.youtube.com/watch?v=UO98lJQ3QGI <br>
- __"Intro to Data Analysis / Visualization with Python, Matplotlib and Pandas | Matplotlib Tutorial"__ by __CS Dojo__ available at *https://www.youtube.com/watch?v=a9UrKTVEeZA <br>
- __"Intro to Data Visualization in Python with Matplotlib! (line graph, bar chart, title, labels, size)"__ by __Keith Galli__ available at *https://www.youtube.com/watch?v=DAQNHzOcO5A <br>


___
![](https://media.csesoc.org.au/content/images/2019/10/learn11.gif) <br>


## Exercise: Bins, Bins, Bins!  <br>

### Selecting the number of bins is an important decision when working with histograms. Are there any rules or recommendations for choosing the number or width of bins? What happens if we use too many or too few bins?

#### * Make sure to cite any resources that you may use. 


```python

```

![](https://i.pinimg.com/originals/ee/62/06/ee62064e595a225f476e47cf39b9a05d.jpg)
