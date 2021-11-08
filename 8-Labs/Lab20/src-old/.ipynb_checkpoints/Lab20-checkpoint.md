**Download** (right-click, save target as ...) this page as a jupyterlab notebook from: (LINK NEEDS FIXING!)

[Lab20](https://atomickitty.ddns.net:8000/user/sensei/files/engr-1330-webroot/engr-1330-webbook/ctds-psuedocourse/docs/8-Labs/Lab8/Lab9_Dev.ipynb?_xsrf=2%7C1b4d47c3%7C0c3aca0c53606a3f4b71c448b09296ae%7C1623531240)

___

# <font color=darkred>Laboratory 20: On Precognition and Other Sins of the Human Brain </font>


```python
# Preamble script block to identify host, user, and kernel
import sys
! hostname
! whoami
print(sys.executable)
print(sys.version)
print(sys.version_info)
```

    DESKTOP-EH6HD63
    desktop-eh6hd63\farha
    C:\Users\Farha\Anaconda3\python.exe
    3.7.4 (default, Aug  9 2019, 18:34:13) [MSC v.1915 64 bit (AMD64)]
    sys.version_info(major=3, minor=7, micro=4, releaselevel='final', serial=0)
    

## Full name: 
## R#: 
## Title of the notebook
## Date: 

![](https://i.pinimg.com/originals/5f/d5/58/5fd558f8b7a4f9e2138709cbe63c7052.gif) <br>


#### The human brain is amazing and mysterious in many ways. Have a look at these sequences. You, with the assistance of your brain, can guess the next item in each sequence, right? <br>

- A,B,C,D,E, ____ ?
- 5,10,15,20,25, ____ ?
- 2,4,8,16,32 ____ ?
- 0,1,1,2,3, ____ ?
- 1, 11, 21, 1211,111221, ____ ?

![](https://3.bp.blogspot.com/-cZXhOB-3MCI/U8zCNevhDUI/AAAAAAAABd4/HK-3xKM_SlQ/s1600/The+Golden+Ratio+Spiral+.jpg) <br>
![](https://i.pinimg.com/originals/80/50/e5/8050e54fd2b4ceb033c8b98586a12972.jpg) <br>
![](https://eternallivinghome.files.wordpress.com/2019/11/image-4.png?w=409) <br>
![](https://eternallivinghome.files.wordpress.com/2019/11/image-2.png) <br>
![](https://eternallivinghome.files.wordpress.com/2019/11/image-1.png?w=414) <br>
![](https://eternallivinghome.files.wordpress.com/2019/11/image-6.png?w=507) <br>
![](https://eternallivinghome.files.wordpress.com/2019/11/image-20.png?w=506) <br>
![](https://eternallivinghome.files.wordpress.com/2019/11/image-8.png) <br>
![](https://eternallivinghome.files.wordpress.com/2019/11/image-22.png?w=1024) <br>


#### But how does our brain do this? How do we 'guess | predict' the next step? Is it that there is only one possible option? is it that we have the previous items? or is it the relationship between the items?<br>

#### What if we have more than a single sequence? Maybe two sets of numbers? How can we predict the next "item" in a situation like that? <br>
![](https://media.makeameme.org/created/ring-that-bell-ws9mb9.jpg) <br>
#### Blue Points? Red Line? Fit? Does it ring any bells? <br>

![](https://38.media.tumblr.com/d51a8aa16dd9e4d40b718b1af803b9be/tumblr_n9kohlL3AR1tofduqo1_500.gif) <br>

---
---
---
# 3 Problem 2 (8 pts)
The table below contains some experimental observations.

|Elapsed Time (s)|Speed (m/s)|
|---:|---:|
|0 |0|
|1.0 |3|
|2.0 |7|
|3.0 |12|
|4.0 |20|
|5.0 |30|
|6.0 | 45.6| 
|7.0 | 60.3 |
|8.0 | 77.7 |
|9.0 | 97.3 |
|10.0| 121.1|

1. Plot the speed vs time (speed on y-axis, time on x-axis) using a scatter plot.  Use blue markers. 
2. Plot a red line on the scatterplot based on the linear model $f(x) = mx + b$ 
3. By trial-and-error find values of $m$ and $b$ that provide a good visual fit (i.e. makes the red line explain the blue markers).
4. Using this data model estimate the speed at $t = 15~\texttt{sec.}$
---
---
---
![](https://media1.tenor.com/images/e43d77dca4b2096cad8226e150ae072f/tenor.gif?itemid=17107650) <br>





### Let's go over some important terminology:

    Linear Regression:
    a basic predictive analytics technique that uses historical data to predict an output variable.

    The Predictor variable (input):
    the variable(s) that help predict the value of the output variable. It is commonly referred to as X.
    
    The Output variable:
    the variable that we want to predict. It is commonly referred to as Y.
    
#### To estimate Y using linear regression, we assume the equation: $Ye = βX + α$
*where Yₑ is the estimated or predicted value of Y based on our linear equation.* <br>

#### Our goal is to find statistically significant values of the parameters α and β that minimise the difference between Y and Yₑ. If we are able to determine the optimum values of these two parameters, then we will have the line of best fit that we can use to predict the values of Y, given the value of X. <br>

## So, how do we estimate α and β? <br>
![](https://media3.giphy.com/media/EijsQdawZkiqY/200.gif) <br>

#### We can use a method called Ordinary Least Squares (OLS). <br>
![](https://miro.medium.com/max/338/1*VVA0rF6MWXcw1JmRNFA87g.png) <br>

#### The objective of the least squares method is to find values of α and β that minimise the sum of the squared difference between Y and Yₑ (distance between the linear fit and the observed points). We will not go through the derivation here, but using calculus we can show that the values of the unknown parameters are as follows: <br>
![](https://miro.medium.com/max/222/0*gR-W7RFar9ijxwAa) <br>
#### where X̄ is the mean of X values and Ȳ is the mean of Y values. β is simply the covariance of X and Y (Cov(X, Y)  devided by the variance of X (Var(X)). <br>

    Covariance:
    In probability theory and statistics, covariance is a measure of the joint variability of two random variables. If the greater values of one variable mainly correspond with the greater values of the other variable, and the same holds for the lesser values, (i.e., the variables tend to show similar behavior), the covariance is positive. In the opposite case, when the greater values of one variable mainly correspond to the lesser values of the other, (i.e., the variables tend to show opposite behavior), the covariance is negative. The sign of the covariance therefore shows the tendency in the linear relationship between the variables. The magnitude of the covariance is not easy to interpret because it is not normalized and hence depends on the magnitudes of the variables. The normalized version of the covariance, the correlation coefficient, however, shows by its magnitude the strength of the linear relation.
![](https://www.wallstreetmojo.com/wp-content/uploads/2019/03/Covariance-Formula.jpg) <br>
![](https://media.geeksforgeeks.org/wp-content/uploads/Correl.png) <br>
    
    The Correlation Coefficient:
    Correlation coefficients are used in statistics to measure how strong a relationship is between two variables. There are several types of correlation coefficient, but the most popular is Pearson’s. Pearson’s correlation (also called Pearson’s R) is a correlation coefficient commonly used in linear regression.Correlation coefficient formulas are used to find how strong a relationship is between data. The formulat for Pearson’s R:
![](https://www.statisticshowto.com/wp-content/uploads/2012/10/pearson.gif) <br>
    
    The formulas return a value between -1 and 1, where:
![](https://www.statisticshowto.com/wp-content/uploads/2012/10/pearson-2-small.png) <br>

    1 : A correlation coefficient of 1 means that for every positive increase in one variable, there is a positive increase of a fixed proportion in the other. For example, shoe sizes go up in (almost) perfect correlation with foot length.
    -1: A correlation coefficient of -1 means that for every positive increase in one variable, there is a negative decrease of a fixed proportion in the other. For example, the amount of gas in a tank decreases in (almost) perfect correlation with speed.
    0 : Zero means that for every increase, there isn’t a positive or negative increase. The two just aren’t related.

___
### Example: Let's have a look at the Problem  1 from Exam II<br>

#### We had a table of recoded times and speeds from some experimental observations:

|Elapsed Time (s)|Speed (m/s)|
|---:|---:|
|0 |0|
|1.0 |3|
|2.0 |7|
|3.0 |12|
|4.0 |20|
|5.0 |30|
|6.0 | 45.6| 
|7.0 | 60.3 |
|8.0 | 77.7 |
|9.0 | 97.3 |
|10.0| 121.1|

#### First let's create a dataframe:



```python
# Load the necessary packages
import numpy as np
import pandas as pd
import statistics 
from matplotlib import pyplot as plt

# Create a dataframe:
time = [0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
speed = [0, 3, 7, 12, 20, 30, 45.6, 60.3, 77.7, 97.3, 121.2]
data = pd.DataFrame({'Time':time, 'Speed':speed})
data
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
      <th>Time</th>
      <th>Speed</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>1</td>
      <td>1.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <td>2</td>
      <td>2.0</td>
      <td>7.0</td>
    </tr>
    <tr>
      <td>3</td>
      <td>3.0</td>
      <td>12.0</td>
    </tr>
    <tr>
      <td>4</td>
      <td>4.0</td>
      <td>20.0</td>
    </tr>
    <tr>
      <td>5</td>
      <td>5.0</td>
      <td>30.0</td>
    </tr>
    <tr>
      <td>6</td>
      <td>6.0</td>
      <td>45.6</td>
    </tr>
    <tr>
      <td>7</td>
      <td>7.0</td>
      <td>60.3</td>
    </tr>
    <tr>
      <td>8</td>
      <td>8.0</td>
      <td>77.7</td>
    </tr>
    <tr>
      <td>9</td>
      <td>9.0</td>
      <td>97.3</td>
    </tr>
    <tr>
      <td>10</td>
      <td>10.0</td>
      <td>121.2</td>
    </tr>
  </tbody>
</table>
</div>



#### Now, let's explore the data:



```python
data.describe()
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
      <th>Time</th>
      <th>Speed</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>count</td>
      <td>11.000000</td>
      <td>11.000000</td>
    </tr>
    <tr>
      <td>mean</td>
      <td>5.000000</td>
      <td>43.100000</td>
    </tr>
    <tr>
      <td>std</td>
      <td>3.316625</td>
      <td>41.204077</td>
    </tr>
    <tr>
      <td>min</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <td>25%</td>
      <td>2.500000</td>
      <td>9.500000</td>
    </tr>
    <tr>
      <td>50%</td>
      <td>5.000000</td>
      <td>30.000000</td>
    </tr>
    <tr>
      <td>75%</td>
      <td>7.500000</td>
      <td>69.000000</td>
    </tr>
    <tr>
      <td>max</td>
      <td>10.000000</td>
      <td>121.200000</td>
    </tr>
  </tbody>
</table>
</div>




```python
time_var = statistics.variance(time)
speed_var = statistics.variance(speed)

print("Variance of recorded times is ",time_var)
print("Variance of recorded speed is ",speed_var)
```

    Variance of recorded times is  11.0
    Variance of recorded speed is  1697.7759999999998
    

#### Is there a relationship ( based on covariance, correlation) between time and speed?


```python
# To find the covariance  
data.cov() 
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
      <th>Time</th>
      <th>Speed</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Time</td>
      <td>11.00</td>
      <td>131.750</td>
    </tr>
    <tr>
      <td>Speed</td>
      <td>131.75</td>
      <td>1697.776</td>
    </tr>
  </tbody>
</table>
</div>




```python
# To find the correlation among the columns 
# using pearson method 
data.corr(method ='pearson') 
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
      <th>Time</th>
      <th>Speed</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Time</td>
      <td>1.000000</td>
      <td>0.964082</td>
    </tr>
    <tr>
      <td>Speed</td>
      <td>0.964082</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>



#### Let's do linear regression with primitive Python:
#### To estimate "y" using the OLS method, we need to calculate "xmean" and "ymean", the covariance of X and y ("xycov"), and the variance of X ("xvar") before we can determine the values for alpha and beta. In our case, X is time and y is Speed.


```python
# Calculate the mean of X and y
xmean = np.mean(time)
ymean = np.mean(speed)

# Calculate the terms needed for the numator and denominator of beta
data['xycov'] = (data['Time'] - xmean) * (data['Speed'] - ymean)
data['xvar'] = (data['Time'] - xmean)**2

# Calculate beta and alpha
beta = data['xycov'].sum() / data['xvar'].sum()
alpha = ymean - (beta * xmean)
print(f'alpha = {alpha}')
print(f'beta = {beta}')

```

    alpha = -16.78636363636363
    beta = 11.977272727272727
    

#### We now have an estimate for alpha and beta! Our model can be written as Yₑ = 11.977 X -16.786, and we can make predictions:


```python
X = np.array(time)

ypred = alpha + beta * X
print(ypred)
```

    [-16.78636364  -4.80909091   7.16818182  19.14545455  31.12272727
      43.1         55.07727273  67.05454545  79.03181818  91.00909091
     102.98636364]
    

#### Let’s plot our prediction ypred against the actual values of y, to get a better visual understanding of our model:


```python
# Plot regression against actual data
plt.figure(figsize=(12, 6))
plt.plot(X, ypred, color="red")     # regression line
plt.plot(time, speed, 'ro', color="blue")   # scatter plot showing actual data
plt.title('Actual vs Predicted')
plt.xlabel('Time (s)')
plt.ylabel('Speed (m/s)')

plt.show()
```


![png](output_21_0.png)


#### The red line is our line of best fit, Yₑ = 11.977 X -16.786. We can see from this graph that there is a positive linear relationship between X and y. Using our model, we can predict y from any values of X! <br>
#### For example, if we had a value X = 20, we can predict that:


```python
ypred_20 = alpha + beta * 20
print(ypred_20)
```

    222.7590909090909
    

#### Linear Regression with statsmodels:
#### First, we use statsmodels’ ols function to initialise our simple linear regression model. This takes the formula y ~ X, where X is the predictor variable (Time) and y is the output variable (Speed). Then, we fit the model by calling the OLS object’s fit() method.


```python
import statsmodels.formula.api as smf

# Initialise and fit linear regression model using `statsmodels`
model = smf.ols('Speed ~ Time', data=data)
model = model.fit()
```

#### We no longer have to calculate alpha and beta ourselves as this method does it automatically for us! Calling model.params will show us the model’s parameters:


```python
model.params
```




    Intercept   -16.786364
    Time         11.977273
    dtype: float64



#### In the notation that we have been using, α is the intercept and β is the slope i.e. α =-16.786364 and β = 11.977273.


```python
# Predict values
speed_pred = model.predict()

# Plot regression against actual data
plt.figure(figsize=(12, 6))
plt.plot(data['Time'], data['Speed'], 'o')           # scatter plot showing actual data
plt.plot(data['Time'], speed_pred, 'r', linewidth=2)   # regression line
plt.xlabel('Time (s)')
plt.ylabel('Speed (m/s)')
plt.title('model vs observed')

plt.show()
```


![png](output_29_0.png)


#### How good do you feel about this predictive model? Will you trust it?

___
### Example: Advertising and Sells! <br>
#### This is a classic regression problem. we have a dataset of the spendings on TV, Radio, and Newspaper advertisements and number of sales for a specific product. We are interested in exploring the relationship between these parameters and answering the following questions:
- Can TV advertising spending predict the number of sales for the product?
- Can Radio advertising spending predict the number of sales for the product?
- Can Newspaper advertising spending predict the number of sales for the product?
- Can we use the three of them to predict the number of sales for the product? | Multiple Linear Regression Model
- Which parameter is a better predictor of the number of sales for the product?


```python
# Import and display first rows of the advertising dataset
df = pd.read_csv('advertising.csv')
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
      <th>TV</th>
      <th>Radio</th>
      <th>Newspaper</th>
      <th>Sales</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>230.1</td>
      <td>37.8</td>
      <td>69.2</td>
      <td>22.1</td>
    </tr>
    <tr>
      <td>1</td>
      <td>44.5</td>
      <td>39.3</td>
      <td>45.1</td>
      <td>10.4</td>
    </tr>
    <tr>
      <td>2</td>
      <td>17.2</td>
      <td>45.9</td>
      <td>69.3</td>
      <td>9.3</td>
    </tr>
    <tr>
      <td>3</td>
      <td>151.5</td>
      <td>41.3</td>
      <td>58.5</td>
      <td>18.5</td>
    </tr>
    <tr>
      <td>4</td>
      <td>180.8</td>
      <td>10.8</td>
      <td>58.4</td>
      <td>12.9</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Describe the df
df.describe()
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
      <th>TV</th>
      <th>Radio</th>
      <th>Newspaper</th>
      <th>Sales</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>count</td>
      <td>200.000000</td>
      <td>200.000000</td>
      <td>200.000000</td>
      <td>200.000000</td>
    </tr>
    <tr>
      <td>mean</td>
      <td>147.042500</td>
      <td>23.264000</td>
      <td>30.554000</td>
      <td>14.022500</td>
    </tr>
    <tr>
      <td>std</td>
      <td>85.854236</td>
      <td>14.846809</td>
      <td>21.778621</td>
      <td>5.217457</td>
    </tr>
    <tr>
      <td>min</td>
      <td>0.700000</td>
      <td>0.000000</td>
      <td>0.300000</td>
      <td>1.600000</td>
    </tr>
    <tr>
      <td>25%</td>
      <td>74.375000</td>
      <td>9.975000</td>
      <td>12.750000</td>
      <td>10.375000</td>
    </tr>
    <tr>
      <td>50%</td>
      <td>149.750000</td>
      <td>22.900000</td>
      <td>25.750000</td>
      <td>12.900000</td>
    </tr>
    <tr>
      <td>75%</td>
      <td>218.825000</td>
      <td>36.525000</td>
      <td>45.100000</td>
      <td>17.400000</td>
    </tr>
    <tr>
      <td>max</td>
      <td>296.400000</td>
      <td>49.600000</td>
      <td>114.000000</td>
      <td>27.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
tv = np.array(df['TV'])
radio = np.array(df['Radio'])
newspaper = np.array(df['Newspaper'])
sales = np.array(df['Sales'])

```


```python
# Get Variance and Covariance - What can we infer?
df.cov()
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
      <th>TV</th>
      <th>Radio</th>
      <th>Newspaper</th>
      <th>Sales</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>TV</td>
      <td>7370.949893</td>
      <td>69.862492</td>
      <td>105.919452</td>
      <td>350.390195</td>
    </tr>
    <tr>
      <td>Radio</td>
      <td>69.862492</td>
      <td>220.427743</td>
      <td>114.496979</td>
      <td>44.635688</td>
    </tr>
    <tr>
      <td>Newspaper</td>
      <td>105.919452</td>
      <td>114.496979</td>
      <td>474.308326</td>
      <td>25.941392</td>
    </tr>
    <tr>
      <td>Sales</td>
      <td>350.390195</td>
      <td>44.635688</td>
      <td>25.941392</td>
      <td>27.221853</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Get Correlation Coefficient - What can we infer?
df.corr(method ='pearson') 
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
      <th>TV</th>
      <th>Radio</th>
      <th>Newspaper</th>
      <th>Sales</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>TV</td>
      <td>1.000000</td>
      <td>0.054809</td>
      <td>0.056648</td>
      <td>0.782224</td>
    </tr>
    <tr>
      <td>Radio</td>
      <td>0.054809</td>
      <td>1.000000</td>
      <td>0.354104</td>
      <td>0.576223</td>
    </tr>
    <tr>
      <td>Newspaper</td>
      <td>0.056648</td>
      <td>0.354104</td>
      <td>1.000000</td>
      <td>0.228299</td>
    </tr>
    <tr>
      <td>Sales</td>
      <td>0.782224</td>
      <td>0.576223</td>
      <td>0.228299</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Answer the first question: Can TV advertising spending predict the number of sales for the product?
import statsmodels.formula.api as smf

# Initialise and fit linear regression model using `statsmodels`
model = smf.ols('Sales ~ TV', data=df)
model = model.fit()
print(model.params)
```

    Intercept    7.032594
    TV           0.047537
    dtype: float64
    


```python
# Predict values
TV_pred = model.predict()

# Plot regression against actual data - What do we see?
plt.figure(figsize=(12, 6))
plt.plot(df['TV'], df['Sales'], 'o')           # scatter plot showing actual data
plt.plot(df['TV'], TV_pred, 'r', linewidth=2)   # regression line
plt.xlabel('TV advertising spending')
plt.ylabel('Sales')
plt.title('Predicting with TV spendings only')

plt.show()
```


![png](output_38_0.png)



```python
# Answer the second question: Can Radio advertising spending predict the number of sales for the product?
import statsmodels.formula.api as smf

# Initialise and fit linear regression model using `statsmodels`
model = smf.ols('Sales ~ Radio', data=df)
model = model.fit()
print(model.params)
```

    Intercept    9.311638
    Radio        0.202496
    dtype: float64
    


```python
# Predict values
RADIO_pred = model.predict()

# Plot regression against actual data - What do we see?
plt.figure(figsize=(12, 6))
plt.plot(df['Radio'], df['Sales'], 'o')           # scatter plot showing actual data
plt.plot(df['Radio'], RADIO_pred, 'r', linewidth=2)   # regression line
plt.xlabel('Radio advertising spending')
plt.ylabel('Sales')
plt.title('Predicting with Radio spendings only')

plt.show()
```


![png](output_40_0.png)



```python
# Answer the third question: Can Newspaper advertising spending predict the number of sales for the product?
import statsmodels.formula.api as smf

# Initialise and fit linear regression model using `statsmodels`
model = smf.ols('Sales ~ Newspaper', data=df)
model = model.fit()
print(model.params)
```

    Intercept    12.351407
    Newspaper     0.054693
    dtype: float64
    


```python
# Predict values
NP_pred = model.predict()

# Plot regression against actual data - What do we see?
plt.figure(figsize=(12, 6))
plt.plot(df['Newspaper'], df['Sales'], 'o')           # scatter plot showing actual data
plt.plot(df['Newspaper'], NP_pred, 'r', linewidth=2)   # regression line
plt.xlabel('Newspaper advertising spending')
plt.ylabel('Sales')
plt.title('Predicting with Newspaper spendings only')

plt.show()
```


![png](output_42_0.png)



```python
# Answer the fourth question: Can we use the three of them to predict the number of sales for the product?
# This is a case of multiple linear regression model. This is simply a linear regression model with more than one predictor:
# and is modelled by:  Yₑ = α + β₁X₁ + β₂X₂ + … + βₚXₚ , where p is the number of predictors.
# In this case: Sales = α + β1*TV + β2*Radio + β3*Newspaper
# Multiple Linear Regression with scikit-learn:
from sklearn.linear_model import LinearRegression

# Build linear regression model using TV,Radio and Newspaper as predictors
# Split data into predictors X and output Y
predictors = ['TV', 'Radio', 'Newspaper']
X = df[predictors]
y = df['Sales']

# Initialise and fit model
lm = LinearRegression()
model = lm.fit(X, y)
```


```python
print(f'alpha = {model.intercept_}')
print(f'betas = {model.coef_}')
```

    alpha = 2.9388893694594085
    betas = [ 0.04576465  0.18853002 -0.00103749]
    


```python
# Therefore, our model can be written as:
#Sales = 2.938 + 0.046*TV + 0.1885*Radio -0.001*Newspaper
# we can predict sales from any combination of TV and Radio and Newspaper advertising costs! 
#For example, if we wanted to know how many sales we would make if we invested 
# $300 in TV advertising and $200 in Radio advertising and $50 in Newspaper advertising
#all we have to do is plug in the values:
new_X = [[300, 200,50]]
print(model.predict(new_X))
```

    [54.32241174]
    


```python
# Answer the final question : Which parameter is a better predictor of the number of sales for the product?
# How can we answer that?
# WHAT CAN WE INFER FROM THE BETAs ?

```

___

#### So far on linear regression ... <br>

![](https://memegenerator.net/img/instances/73698591.jpg) <br>


- __What is linear regression?__<br>
    a basic predictive analytics technique that uses historical data to predict an output variable.<br>
- __Why do we need linear regression?__
    To explore the relationship between predictor and output variables and predict the output variable based on known values of predictors.  <br>    
- __How does linear regression work?__
    To estimate Y using linear regression, we assume the equation:  𝑌𝑒=β𝑋+α <br>
    Our goal is to find statistically significant values of the parameters α and β that minimise the difference between Y and Yₑ. If we are able to determine the optimum values of these two parameters, then we will have the line of best fit that we can use to predict the values of Y, given the value of X. <br>
- __How to estimate the coefficients?__
    We used a method called "Ordinary Least Squares (OLS)". __But that is not the only way. Let's put a pin on that!__

![](https://media3.giphy.com/media/15bf6pru8mSR2/giphy.gif) <br>


#### Remember when we discussed Probability Density Function (PDF) for the normal distribution? - Probably not!<br>

![](https://miro.medium.com/max/572/1*P78bMZPhhKnzLkwcNgeJ0g.png) <br>


#### This equation is telling us the probability our sample x from our random variable X, when the true parameters of the distribution are μ and σ. <br>


### Example1 :Let’s say our sample is 3, what is the probability it comes from a distribution of μ = 3 and σ = 1? What if it came from a distribution with μ = 7 and σ = 2? Which one is more probable?<br>


```python
import numpy as np
import pandas as pd
import statistics
import scipy.stats
from matplotlib import pyplot as plt
```


```python
scipy.stats.norm.pdf(3, 3, 1)
```




    0.3989422804014327




```python
scipy.stats.norm.pdf(3, 7, 2)
```




    0.02699548325659403



#### So it is much more likely it came from the first distribution. The PDF equation has shown us how likely those values are to appear in a distribution with certain parameters. Keep that in mind for later. But what if we had a bunch of points we wanted to estimate?
#### Let’s assume we get a bunch of samples fromX which we know to come from some normal distribution, and all are mutually independent from each other. If this is the case, the total probability of observing all of the data is the product of obtaining each data point individually. 
#### This should kinda remind you of our class on probability, where we talked about the probability of multiple events happening back to back (e.g., the royal flush set). 

### Example2 : What is the probability of 2 and 6 being drawn from a distribution with μ = 4 and σ = 1<br>


```python
scipy.stats.norm.pdf(2, 4, 1) * scipy.stats.norm.pdf(6, 4, 1)
```




    0.0029150244650281948



#### Maximum Likelihood Estimation (MLE) is used to specify a distribution of unknown parameters, then using your data to pull out the actual parameter values.To go back to the pin!, let's look at our linear model:
![](https://miro.medium.com/max/352/1*iJrwssQh4dJARzeuQPw1kw.png) <br>
#### The noise parameter (error) is basically why the points (samples) do not fall exactly on the line. The error for each point would be the distance from the point to our line. We’d like to explicitly include those errors in our model. One method of doing this, is to assume the errors are distributed from a Gaussian distribution with a mean of 0 and some unknown variance σ². The Gaussian seems like a good choice, because our errors look like they’re symmetric about were the line would be, and that small errors are more likely than large errors. <br>
#### This model has three parameters: the slope and intercept of our line and the variance of the noise distribution. Our main goal is to find the best parameters for the slope and intercept of our line.
#### let’s rewrite our model from above as a single conditional distribution given x:
![](https://miro.medium.com/max/403/1*S9Wo7Ay3O-CGarsNULSWOA.png) <br>
#### This is equivalent to pushing our x through the equation of the line and then adding noise from the 0 mean Gaussian. Now, we can write the conditional distribution of y given x in terms of this Gaussian. This is just the equation of a Gaussian distribution’s probability density function, with our linear equation in place of the mean:
![](https://miro.medium.com/max/576/1*3M7mJamXgcFPXzvD0U4yIA.png) <br>
#### The semicolon in the conditional distribution acts just like a comma, but it’s a useful notation for separating our observed data from the parameters. <br>
#### Each point is independent and identically distributed (iid), so we can write the likelihood function with respect to all of our observed points as the product of each individual probability density. Since σ² is the same for each data point, we can factor out the term of the Gaussian which doesn’t include x or y from the product:
![](https://miro.medium.com/max/576/1*JXtvd6fO6ydgAqQR4jAaWQ.png) <br>
#### The next step in MLE, is to find the parameters which maximize this function. To make our equation simpler, let’s take the log of our likelihood. Recall, that maximizing the log-likelihood is the same as maximizing the likelihood since the log is monotonic. The natural log cancels out with the exponential, turns products into sums of logs, and division into subtraction of logs; so our log-likelihood looks much simpler:
![](https://miro.medium.com/max/576/1*gDNxsKgiWTj6AWmolmkjlQ.png) <br>
#### To clean things up a bit more, let’s write the output of our line as a single value:
![](https://miro.medium.com/max/226/1*tCAZf5pWI5UYyWLXiZ-tSw.png) <br>
#### Now our log-likelihood can be written as::
![](https://miro.medium.com/max/576/1*U8yya-GV548dLYdRVabERQ.png) <br>
#### To remove the negative signs, let’s recall that maximizing a number is the same thing as minimizing the negative of the number. So instead of maximizing the likelihood, let’s minimize the negative log-likelihood:
![](https://miro.medium.com/max/576/1*Y_B6FPJq0jb17qK04MVltw.png) <br>
#### Our ultimate goal is to find the parameters of our line. To minimize the negative log-likelihood with respect to the linear parameters (the θs), we can imagine that our variance term is a fixed constant. Removing any constant’s which don’t include our θs won’t alter the solution. Therefore, we can throw out any constant terms and elegantly write what we’re trying to minimize as:
![](https://miro.medium.com/max/175/1*O8b2CNiqn3xjUF3fkklrXQ.png) <br>
#### The maximum likelihood estimate for our linear model is the line which minimizes the sum of squared errors!
![](https://media1.giphy.com/media/SJX3gbZ2dbaEhU92Pu/source.gif) <br>
#### Now, let's solve for parameters. We’ve concluded that the maximum likelihood estimates for our slope and intercept can be found by minimizing the sum of squared errors. Let’s expand out our minimization objective and use i as our index over our n data points:
![](https://miro.medium.com/max/403/1*0zO8-m3ZdruX0hgJ4zLm9g.png) <br>
#### The square in the SSE formula makes it quadratic with a single minimum. The minimum can be found by taking the derivative with respect to each of the parameters, setting it equal to 0, and solving for the parameters in turn. <br>

#### Taking the partial derivative with respect to the intercept, Setting the derivative equal to 0 and solving for the intercept gives us:
![](https://miro.medium.com/max/227/1*YzIf9e2kTWbjgx58wb-KXw.png) <br>
#### Taking the partial derivative with respect to the slope, Setting the derivative equal to 0 and solving for the slope gives us:
![](https://miro.medium.com/max/324/1*o0vOZ25b1h57UyidKsJlvQ.png) <br>
#### And now it's time to put it all together:



```python
def find_line(xs, ys):
    """Calculates the slope and intercept"""
    
    # number of points
    n = len(xs)
    # calculate means
    x_bar = sum(xs)/n
    y_bar = sum(ys)/n
        
    # calculate slope
    num = 0
    denom = 0
    for i in range(n):
        num += (xs[i]-x_bar)*(ys[i]-y_bar)
        denom += (xs[i]-x_bar)**2
    slope = num/denom
    
    # calculate intercept
    intercept = y_bar - slope*x_bar
    
    return slope, intercept
```

### Example: Let's have a look at the familiar problem  from Exam II which was also an Example in the previous lab!<br>

#### We had a table of recorded times and speeds from some experimental observations. Use MLE to find the intercept and the slope:

|Elapsed Time (s)|Speed (m/s)|
|---:|---:|
|0 |0|
|1.0 |3|
|2.0 |7|
|3.0 |12|
|4.0 |20|
|5.0 |30|
|6.0 | 45.6| 
|7.0 | 60.3 |
|8.0 | 77.7 |
|9.0 | 97.3 |
|10.0| 121.1|


```python
time = [0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
speed = [0, 3, 7, 12, 20, 30, 45.6, 60.3, 77.7, 97.3, 121.2]
find_line(time, speed) #Is this similar to our past results?! 
```




    (11.977272727272727, -16.78636363636364)




```python
# Predict values
X = np.array(time)
alpha = -16.78636363636364
beta = 11.977272727272727
ypred = alpha + beta * X


# Plot regression against actual data
plt.figure(figsize=(12, 6))
plt.plot(X, speed, 'o')           # scatter plot showing actual data
plt.plot(X, ypred, 'r', linewidth=2)   # regression line
plt.xlabel('Time (s)')
plt.ylabel('Speed (m/s)')
plt.title('model vs observed')

plt.show()
```


![png](output_60_0.png)


## Goodness-of-Fit <br>
### So far, we have assessed the quality of fits visually. We can make numerical assessments as well via Goodness-of-Fit (GOF) measures. Let's discuss three of the most common metrics for evaluating predictions on regression machine learning problems: <br>
### Mean Absolute Error (MAE): <br>
    The Mean Absolute Error (or MAE) is the average of the absolute differences between predictions and actual values. It gives an idea of how wrong the predictions were. The measure gives an idea of the magnitude of the error, but no idea of the direction (e.g. over or under predicting). Here is the formula:

![](https://wikimedia.org/api/rest_v1/media/math/render/svg/3ef87b78a9af65e308cf4aa9acf6f203efbdeded) <br>

    It is thus an arithmetic average of the absolute errors |ei|=|yi-xi|, where yi is the prediction and xi the true value.  This is known as a scale-dependent accuracy measure and therefore cannot be used to make comparisons between series using different scales.


```python
# calculate manually
d = speed - ypred
mae_m = np.mean(abs(d))


print("Results by manual calculation:")
print("MAE:",mae_m)



import sklearn.metrics as metrics
mae = metrics.mean_absolute_error(speed, ypred)
print(mae)
```

    Results by manual calculation:
    MAE: 8.927272727272728
    8.927272727272728
    

### Mean Squared Error (MSE) and Root Mean Squared Error (RMSE): <br>
    The Mean Squared Error (or MSE) is much like the mean absolute error in that it provides a gross idea of the magnitude of error. It measures the average of the squares of the errors—that is, the average squared difference between the estimated values and the actual value. The MSE is a measure of the quality of an estimator—it is always non-negative, and values closer to zero are better. An MSE of zero, meaning that the estimator predicts observations of the parameter with perfect accuracy, is ideal (but typically not possible).Taking the square root of the mean squared error converts the units back to the original units of the output variable and can be meaningful for description and presentation. This is called the Root Mean Squared Error (or RMSE). RMSE is the most widely used metric for regression tasksHere is the formula:

![](https://wikimedia.org/api/rest_v1/media/math/render/svg/e258221518869aa1c6561bb75b99476c4734108e) <br>



```python
mse_m = np.mean(d**2)
rmse_m = np.sqrt(mse_m)
print("MSE:", mse_m)
print("RMSE:", rmse_m)
mse = metrics.mean_squared_error(speed, ypred)
rmse = np.sqrt(mse) # or mse**(0.5) 
print(mse)
print(rmse)
```

    MSE: 108.88210743801659
    RMSE: 10.434658951686758
    108.88210743801659
    10.434658951686758
    

### R^2 Metric: <br>
    The R^2 (or R Squared) metric provides an indication of the goodness of fit of a set of predictions to the actual values. In statistical literature, this measure is called the coefficient of determination. This is a value between 0 and 1 for no-fit and perfect fit respectively. It provides a measure of how well observed outcomes are replicated by the model, based on the proportion of total variation of outcomes explained by the model..Here is the formula:

![](https://wikimedia.org/api/rest_v1/media/math/render/svg/3a1f55d7e84c24299917fb3fec4d0439b81e728d) <br>
![](https://wikimedia.org/api/rest_v1/media/math/render/svg/2669c9340581d55b274d3b8ea67a7deb2225510b) <br>
![](https://wikimedia.org/api/rest_v1/media/math/render/svg/c7e3ab84636f38c257641f85f009bcb422c73151) <br>


```python
r2_m = 1-(sum(d**2)/sum((speed-np.mean(speed))**2))
print("R-Squared:", r2_m)
r2 = metrics.r2_score(speed, ypred)
print(r2)
```

    R-Squared: 0.9294545816516323
    0.9294545816516323
    

![](https://media2.giphy.com/media/5nj4ZZWl6QwneEaBX4/source.gif) <br>

*This notebook was inspired by several blogposts including:*
- __"Introduction to Linear Regression in Python"__ by __Lorraine Li__ available at* https://towardsdatascience.com/introduction-to-linear-regression-in-python-c12a072bedf0 <br>
- __"In Depth: Linear Regression"__ available at* https://jakevdp.github.io/PythonDataScienceHandbook/05.06-linear-regression.html <br>
- __"A friendly introduction to linear regression (using Python)"__ available at* https://www.dataschool.io/linear-regression-in-python/ <br>
- __"What is Maximum Likelihood Estimation — Examples in Python"__ by __Robert R.F. DeFilippi__ available at* https://medium.com/@rrfd/what-is-maximum-likelihood-estimation-examples-in-python-791153818030 <br>
- __"Linear Regression"__ by __William Fleshman__  available at* https://towardsdatascience.com/linear-regression-91eeae7d6a2e <br>
- __"Regression Accuracy Check in Python (MAE, MSE, RMSE, R-Squared)"__ available at* https://www.datatechnotes.com/2019/10/accuracy-check-in-python-mae-mse-rmse-r.html <br>

*Here are some great reads on these topics:* 
- __"Linear Regression in Python"__ by __Sadrach Pierre__ available at* https://towardsdatascience.com/linear-regression-in-python-a1d8c13f3242 <br>
- __"Introduction to Linear Regression in Python"__ available at* https://cmdlinetips.com/2019/09/introduction-to-linear-regression-in-python/ <br>
- __"Linear Regression in Python"__ by __Mirko Stojiljković__ available at* https://realpython.com/linear-regression-in-python/ <br>
- __"A Gentle Introduction to Linear Regression With Maximum Likelihood Estimation"__ by __Jason Brownlee__ available at* https://machinelearningmastery.com/linear-regression-with-maximum-likelihood-estimation/ <br>
- __"Metrics To Evaluate Machine Learning Algorithms in Python"__ by __Jason Brownlee__ available at* https://machinelearningmastery.com/metrics-evaluate-machine-learning-algorithms-python/ <br>
- __"A Gentle Introduction to Maximum Likelihood Estimation"__ by __Jonathan Balaban__ available at* https://towardsdatascience.com/a-gentle-introduction-to-maximum-likelihood-estimation-9fbff27ea12f <br>
- __"Regression: An Explanation of Regression Metrics And What Can Go Wrong"__ by __Divyanshu Mishra__ available at* https://towardsdatascience.com/regression-an-explanation-of-regression-metrics-and-what-can-go-wrong-a39a9793d914 <br>
- __"Tutorial: Understanding Regression Error Metrics in Python"__ available at* https://www.dataquest.io/blog/understanding-regression-error-metrics/ <br>

*Here are some great videos on these topics:* 
- __"StatQuest: Fitting a line to data, aka least squares, aka linear regression."__ by __StatQuest with Josh Starmer__ available at* https://www.youtube.com/watch?v=PaFPbb66DxQ&list=PLblh5JKOoLUIzaEkCLIUxQFjPIlapw8nU <br>
- __"Statistics 101: Linear Regression, The Very Basics"__ by __Brandon Foltz__ available at* https://www.youtube.com/watch?v=ZkjP5RJLQF4 <br>
- __"How to Build a Linear Regression Model in Python | Part 1" and 2,3,4!__ by __Sigma Coding__ available at* https://www.youtube.com/watch?v=MRm5sBfdBBQ <br>
- __"StatQuest: Maximum Likelihood, clearly explained!!!"__ by __StatQuest with Josh Starmer__ available at* https://www.youtube.com/watch?v=XepXtl9YKwc <br>
- __"Maximum Likelihood for Regression Coefficients (part 1 of 3)" and part 2 and 3__ by __Professor Knudson__ available at* https://www.youtube.com/watch?v=avs4V7wBRw0 <br>
- __"StatQuest: R-squared explained"__ by __StatQuest with Josh Starmer__ available at* https://www.youtube.com/watch?v=2AQKmw14mHM <br>

___
![](https://media2.giphy.com/media/dNgK7Ws7y176U/200.gif) <br>


## Exercise: Linear Regression - Yea or Nay <br>

### List some of the pros and cons of linear regression.

#### _Make sure to cite any resources that you may use._ 


```python

```

![](http://quotessayings.net/pics/linear-regression-quote-by-jordan-ellenberg-244617.jpg)
