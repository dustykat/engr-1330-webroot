**Download** (right-click, save target as ...) this page as a jupyterlab notebook from: (LINK NEEDS FIXING!)

[Lab24](https://atomickitty.ddns.net:8000/user/sensei/files/engr-1330-webroot/engr-1330-webbook/ctds-psuedocourse/docs/8-Labs/Lab8/Lab9_Dev.ipynb?_xsrf=2%7C1b4d47c3%7C0c3aca0c53606a3f4b71c448b09296ae%7C1623531240)

___

# <font color=darkred>Laboratory 24: "A Tale of Supportive Machines!" </font>


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

___

# Support Vector Machines (SVM)

![](https://memegenerator.net/img/instances/68631404.jpg) <br>


### “Support Vector Machine” (SVM) is a supervised machine learning algorithm which can be used for both classification or regression challenges. However,  it is mostly used in classification problems. In the SVM algorithm, we plot each data item as a point in n-dimensional space (where n is number of features you have) with the value of each feature being the value of a particular coordinate. Then, we perform classification by finding the hyper-plane that differentiates the two classes very well (look at the below snapshot). <br>

![](https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2019/11/svm1.png) <br>

    Hyperplane:
    In geometry, a hyperplane is a subspace whose dimension is one less than that of its ambient space. If a space is 3-dimensional then its hyperplanes are the 2-dimensional planes, while if the space is 2-dimensional, its hyperplanes are the 1-dimensional lines. (@Wikipedia: https://en.wikipedia.org/wiki/Hyperplane)

![](https://images.deepai.org/glossary-terms/3bb86574825445cba73a67222b744648/hyperplane.png) <br>

### Support Vectors are simply the co-ordinates of individual observation. The SVM classifier is a frontier which best segregates the two classes (hyper-plane/ line). <br>

![](https://www.analyticsvidhya.com/wp-content/uploads/2015/10/SVM_1.png) <br>


## How does it work?

![](https://miro.medium.com/max/1200/0*MgG8zoCB6CY4Fa19.gif) <br>

### Identify the right hyper-plane (Scenario-1): 
__Here, we have three hyper-planes (A, B and C). Now, identify the right hyper-plane to classify star and circle.__


![](https://www.analyticsvidhya.com/wp-content/uploads/2015/10/SVM_21.png)

__Remember a thumb rule to identify the right hyper-plane: “Select the hyper-plane which segregates the two classes better”. In this scenario, hyper-plane “B” has excellently performed this job.__  <br>     


<hr>
    
### Identify the right hyper-plane (Scenario-2): 
__Here, we have three hyper-planes (A, B and C) and all are segregating the classes well. Now, How can we identify the right hyper-plane?__


![](https://www.analyticsvidhya.com/wp-content/uploads/2015/10/SVM_3.png)

__Here, maximizing the distances between nearest data point (either class) and hyper-plane will help us to decide the right hyper-plane. This distance is called as Margin. Let’s look at the below snapshot:__  <br>     

![](https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2019/11/svm-2.png)

__Below, you can see that the margin for hyper-plane C is high as compared to both A and B. Hence, we name the right hyper-plane as C. Another lightning reason for selecting the hyper-plane with higher margin is robustness. If we select a hyper-plane having low margin then there is high chance of miss-classification.__  <br> 

![](https://www.analyticsvidhya.com/wp-content/uploads/2015/10/SVM_4.png)


<hr>
    
### Identify the right hyper-plane (Scenario-3): 
__Hint: Use the rules as discussed in previous section to identify the right hyper-plane__


![](https://www.analyticsvidhya.com/wp-content/uploads/2015/10/SVM_5.png)

__Some of you may have selected the hyper-plane B as it has higher margin compared to A. But, here is the catch, SVM selects the hyper-plane which classifies the classes accurately prior to maximizing margin. Here, hyper-plane B has a classification error and A has classified all correctly. Therefore, the right hyper-plane is A.__  <br>     


<hr>
    
### Identify the right hyper-plane (Scenario-4): 
__Below, I am unable to segregate the two classes using a straight line, as one of the stars lies in the territory of other(circle) class as an outlier.__


![](https://www.analyticsvidhya.com/wp-content/uploads/2015/10/SVM_61.png)

__As I have already mentioned, one star at other end is like an outlier for star class. The SVM algorithm has a feature to ignore outliers and find the hyper-plane that has the maximum margin. Hence, we can say, SVM classification is robust to outliers.__  <br>     

![](https://www.analyticsvidhya.com/wp-content/uploads/2015/10/SVM_71.png)


<hr>
    
### Identify the right hyper-plane (Scenario-5): 
__In the scenario below, we can’t have linear hyper-plane between the two classes, so how does SVM classify these two classes? Till now, we have only looked at the linear hyper-plane.__


![](https://www.analyticsvidhya.com/wp-content/uploads/2015/10/SVM_8.png)

__SVM can solve this problem. Easily! It solves this problem by introducing additional feature. Here, we will add a new feature z=x^2+y^2. Now, let’s plot the data points on axis x and z:__  <br>     

![](https://www.analyticsvidhya.com/wp-content/uploads/2015/10/SVM_9.png)

__In above plot, points to consider are:__
- __All values for z would be positive always because z is the squared sum of both x and y__
- __In the original plot, red circles appear close to the origin of x and y axes, leading to lower value of z and star relatively away from the origin result to higher value of z.__ <br>


__In the SVM classifier, it is easy to have a linear hyper-plane between these two classes. But, another burning question which arises is, should we need to add this feature manually to have a hyper-plane. No, the SVM  algorithm has a technique called the kernel trick. The SVM kernel is a function that takes low dimensional input space and transforms it to a higher dimensional space i.e. it converts not separable problem to separable problem. It is mostly useful in non-linear separation problem. Simply put, it does some extremely complex data transformations, then finds out the process to separate the data based on the labels or outputs you’ve defined. When we look at the hyper-plane in original input space it looks like a circle:__  <br>   

![](https://www.analyticsvidhya.com/wp-content/uploads/2015/10/SVM_10.png)


__From another perspective, this is what's happening:__
![](https://machinelearningwithmlr.files.wordpress.com/2019/10/ch06_fig_5_mlr.png?w=656)

__There are different Kernel functions that can be used with SVMs:__
![](https://www.researchgate.net/profile/Jui-Sheng_Chou/publication/239386696/figure/tbl2/AS:667912230674445@1536254093339/SVM-Kernel-Function-Types.png)

__Depending on the nature of the problem, different Kernels may be advantagous:__
![](https://machinelearningwithmlr.files.wordpress.com/2019/10/ch06_fig_6_mlr.png?w=656)

## Let's see how to implement SVM in Python!

![](https://miro.medium.com/max/1200/1*Pp5ZQowsSjqKmvtjlqWEug.jpeg)


___
## Example: Re-using the Iris Plants Classification <br>

![](https://www.almanac.com/sites/default/files/styles/opengraph/public/image_nodes/iris-flowers.jpg?itok=lq_po7Qz) <br>



### The Iris Flower Dataset involves predicting the flower species given measurements of iris flowers. The Iris Data Set contains information on sepal length, sepal width, petal length, petal width all in cm, and class of iris plants. The data set contains 3 classes of 50 instances each.

![](https://miro.medium.com/max/1000/1*lFC_U5j_Y8IXF4Ga87KNVg.png) <br>


### Let's use SVM in Python and see if we can classifity iris plants based on the four given predictors.



<hr>

*__Acknowledgements__*
1. *Fisher,R.A. "The use of multiple measurements in taxonomic problems" Annual Eugenics, 7, Part II, 179-188 (1936); also in "Contributions to Mathematical Statistics" (John Wiley, NY, 1950).*
2. *Duda,R.O., & Hart,P.E. (1973) Pattern Classification and Scene Analysis. (Q327.D83) John Wiley & Sons.  ISBN 0-471-22361-1.  See page 218.*
3. *Dasarathy, B.V. (1980) "Nosing Around the Neighborhood: A New System Structure and Classification Rule for Recognition in Partially Exposed Environments".  IEEE Transactions on Pattern Analysis and Machine Intelligence, Vol. PAMI-2, No. 1, 67-71.*
4. *Gates, G.W. (1972) "The Reduced Nearest Neighbor Rule".  IEEE Transactions on Information Theory, May 1972, 431-433.*      
5. *See also: 1988 MLC Proceedings, 54-64.  Cheeseman et al's AUTOCLASS II conceptual clustering system finds 3 classes in the data.*

### As you know by now, the first step is to load some necessary libraries:


```python
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import sklearn.metrics as metrics
import seaborn as sns
%matplotlib inline
from sklearn import datasets #There is a version of the iris database in the sklearn package

from sklearn import svm #The function for applyin SVM
```


```python
# import some data to play with
iris = datasets.load_iris()
X = iris.data[:, :2] # Let's say we only take the first two features: Sepal Width and Sepal Length
                     
y = iris.target
```


```python
# we create an instance of SVM and fit our data. 
svc = svm.SVC(kernel='linear').fit(X, y)
```


```python
# create a mesh to plot in
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
h = (x_max / x_min)/100
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
 np.arange(y_min, y_max, h))
```


```python
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired)
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.xlim(xx.min(), xx.max())
plt.title('SVC with linear kernel')
plt.show()
```


![png](output_13_0.png)



```python
plt.subplot(1, 1, 1)
Z = svc.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, cmap=plt.cm.Paired, alpha=0.8)
plt.scatter(X[:, 0], X[:, 1], cmap=plt.cm.Paired, c=y)
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.xlim(xx.min(), xx.max())
plt.title('SVC with linear kernel')
plt.show()
```


![png](output_14_0.png)



```python
svc = svm.SVC(kernel='rbf').fit(X, y)
```

    C:\Users\Farha\Anaconda3\lib\site-packages\sklearn\svm\base.py:193: FutureWarning: The default value of gamma will change from 'auto' to 'scale' in version 0.22 to account better for unscaled features. Set gamma explicitly to 'auto' or 'scale' to avoid this warning.
      "avoid this warning.", FutureWarning)
    


```python
plt.subplot(1, 1, 1)
Z = svc.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, cmap=plt.cm.Paired, alpha=0.8)
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired)
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.xlim(xx.min(), xx.max())
plt.title('SVC with linear kernel')
plt.show()
```


![png](output_16_0.png)


**gamma:** <br>
Kernel coefficient for ‘rbf’, ‘poly’ and ‘sigmoid’. Higher the value of gamma, will try to exact fit the as per training data set i.e. generalization error and cause over-fitting problem.
![](https://www.analyticsvidhya.com/wp-content/uploads/2015/10/SVM_15.png) <br>

**C:** <br>
Penalty parameter C of the error term. It also controls the trade-off between smooth decision boundaries and classifying the training points correctly.
![](https://www.analyticsvidhya.com/wp-content/uploads/2015/10/SVM_18.png) <br>


```python

```

### Trying the route similar to what we did before, we should read the dataset and explore it using tools such as descriptive statistics:


```python
dataset = pd.read_csv('iris.csv')
dataset.head()
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
      <th>sepal-length</th>
      <th>sepal-width</th>
      <th>petal-length</th>
      <th>petal-width</th>
      <th>Class</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>5.1</td>
      <td>3.5</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <td>1</td>
      <td>4.9</td>
      <td>3.0</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <td>2</td>
      <td>4.7</td>
      <td>3.2</td>
      <td>1.3</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <td>3</td>
      <td>4.6</td>
      <td>3.1</td>
      <td>1.5</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <td>4</td>
      <td>5.0</td>
      <td>3.6</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
  </tbody>
</table>
</div>



### We should seperate the predictors and target - similar to what we did for logisitc regression:


```python
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values
```

### Now we split the training and testing datasets with a 0.75/0.25 ratio:


```python
from sklearn.model_selection import train_test_split
 
 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)
```

### Then, we create an instance of SVM and fit our data:


```python
from sklearn import svm
#create a classifier
cls = svm.SVC(kernel="linear")
#train the model
cls.fit(X_train,y_train)
#predict the response
pred = cls.predict(X_test)
```

### And we can evaluate the performance of our SVM model:


```python
from sklearn.metrics import classification_report, confusion_matrix

print(confusion_matrix(y_test, pred))
print(metrics.classification_report(y_test, y_pred=pred))
```

    [[14  0  0]
     [ 0 12  1]
     [ 0  0 11]]
                     precision    recall  f1-score   support
    
        Iris-setosa       1.00      1.00      1.00        14
    Iris-versicolor       1.00      0.92      0.96        13
     Iris-virginica       0.92      1.00      0.96        11
    
           accuracy                           0.97        38
          macro avg       0.97      0.97      0.97        38
       weighted avg       0.98      0.97      0.97        38
    
    

<hr>
<hr>

### Pros and Cons associated with SVM ...

#### Pros:
- **It works really well with a clear margin of separation.**
- **It is effective in high dimensional spaces.**
- **It is effective in cases where the number of dimensions is greater than the number of samples.**
- **It uses a subset of training points in the decision function (called support vectors), so it is also memory efficient.**
- **It allows utilization of different kernel functions  for the decision function which also makes it versatile.**

#### Cons:
- **It doesn’t perform well when we have large data set because the required training time is higher.**
- **It also doesn’t perform very well, when the data set has more noise i.e. target classes are overlapping.**


![](https://miro.medium.com/max/2800/1*pYZhrwePzlYsaOkK-0hEXA.png) <br>


![](https://media2.giphy.com/media/5nj4ZZWl6QwneEaBX4/source.gif) <br>

*This notebook was inspired by several blogposts including:* 

- __"Understanding Support Vector Machine(SVM) algorithm from examples (along with code)"__ by __SUNIL RAY__ available at *https://www.analyticsvidhya.com/blog/2017/09/understaing-support-vector-machine-example-code/ <br>
- __"A Quick Guide To Learn Support Vector Machine In Python"__ by __Mohammad Waseem__ available at *https://www.edureka.co/blog/support-vector-machine-in-python/ <br>


*Here are some great reads on these topics:* 
- __"Support Vector Machine – Simplified"__ by __TAVISH SRIVASTAVA__ available at *https://www.analyticsvidhya.com/blog/2014/10/support-vector-machine-simplified/?utm_source=blog&utm_medium=understandingsupportvectormachinearticle <br>
- __"Creating a simple binary SVM classifier with Python and Scikit-learn"__ by __Chris__ available at *https://www.machinecurve.com/index.php/2020/05/03/creating-a-simple-binary-svm-classifier-with-python-and-scikit-learn/#summary <br>
- __"Support Vector Machine introduction"__ available at *https://pythonprogramming.net/support-vector-machine-intro-machine-learning-tutorial/ <br>
- __"Classifying data using Support Vector Machines(SVMs) in Python"__ available at *https://www.geeksforgeeks.org/classifying-data-using-support-vector-machinessvms-in-python/ <br>
- __"Support Vector Machines explained with Python examples"__ by __Carolina Bento__ available at *https://towardsdatascience.com/support-vector-machines-explained-with-python-examples-cb65e8172c85 <br>



*Here are some great videos on these topics:* 
- __"Support Vector Machines, Clearly Explained!!!"__ by __StatQuest with Josh Starmer__ available at *https://www.youtube.com/watch?v=efR1C6CvhmE <br>
- __"Support Vector Machine (SVM) - Fun and Easy Machine Learning"__ by __Augmented Startups__ available at *https://www.youtube.com/watch?v=Y6RRHw9uN9o <br>
- __"How SVM (Support Vector Machine) algorithm works"__ by __Thales Sehn Körting__ available at *https://www.youtube.com/watch?v=1NxnPkZM9bc <br>


___
![](https://media2.giphy.com/media/dNgK7Ws7y176U/200.gif) <br>


## Exercise: Who would you trust? A tree or a machine?  <br>

### What are some advantages and disadvantages the Random Forest algorithm against the Support Vector Machines?

#### _Make sure to cite any resources that you may use._ 


```python

```

![](https://www.quotemaster.org/images/8a/8a4a5240c603576bb2723eba06888447.png)


```python

```
