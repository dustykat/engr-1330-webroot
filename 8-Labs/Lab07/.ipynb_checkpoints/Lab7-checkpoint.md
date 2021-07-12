**Download** (right-click, save target as ...) this page as a jupyterlab notebook from:

[Lab7](https://atomickitty.ddns.net:8000/user/sensei/files/engr-1330-webroot/engr-1330-webbook/ctds-psuedocourse/docs/8-Labs/Lab6/Lab7_Dev.ipynb?_xsrf=2%7C1b4d47c3%7C0c3aca0c53606a3f4b71c448b09296ae%7C1623531240)

___

# <font color=darkred>Laboratory 7: Numpy for Bread! </font>


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
## Title of the notebook:
## Date:
___

![](https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/NumPy_logo_2020.svg/1280px-NumPy_logo_2020.svg.png) <br>

## <font color=purple>Numpy</font>
Numpy is the core library for scientific computing in Python. It provides a high-performance multidimensional array object, and tools for working with these arrays. The library’s name is short for “Numeric Python” or “Numerical Python”. If you are curious about NumPy, this cheat sheet is recommended:
https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Numpy_Python_Cheat_Sheet.pdf

### <font color=purple>Arrays</font>

A numpy array is a grid of values, all of the same type, and is indexed by a tuple of nonnegative integers. The number of dimensions is the rank of the array; the shape of an array is a tuple of integers giving the size of the array along each dimension. In other words, an array contains information about the raw data, how to locate an element and how to interpret an element.To make a numpy array, you can just use the np.array() function. All you need to do is pass a list to it. Don’t forget that, in order to work with the np.array() function, you need to make sure that the numpy library is present in your environment.
If you want to read more about the differences between a Python list and NumPy array, this link is recommended:
https://webcourses.ucf.edu/courses/1249560/pages/python-lists-vs-numpy-arrays-what-is-the-difference



___
### Example- 1D Arrays
__Let's create a 1D array from the 2000s (2000-2009):__ 


```python
import numpy as np             #First, we need to impoty "numpy"
mylist = [2000,2001,2002,2003,2004,2005,2006,2007,2008,2009]         #Create a list of the years
print(mylist)                 #Check how it looks
np.array(mylist)              #Define it as a numpy array

```

    [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009]





    array([2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009])



___
### Example- n-Dimensional Arrays
__Let's create a 5x2 array from the 2000s (2000-2009):__ 


```python
myotherlist = [[2000,2001],[2002,2003],[2004,2005],[2006,2007],[2008,2009]]     #Since I want a 5x2 array, I should group the years two by two
print(myotherlist)             #See how it looks as a list
np.array(myotherlist)          #See how it looks as a numpy array
```

    [[2000, 2001], [2002, 2003], [2004, 2005], [2006, 2007], [2008, 2009]]





    array([[2000, 2001],
           [2002, 2003],
           [2004, 2005],
           [2006, 2007],
           [2008, 2009]])



### <font color=purple>Arrays Arithmetic</font>

Once you have created the arrays, you can do basic Numpy operations. Numpy offers a variety of operations applicable on arrays. From basic operations such as summation, subtraction, multiplication and division to more advanced and essential operations such as matrix multiplication and other elementwise operations. In the examples below, we will go over some of these:


___
### Example- 1D Array Arithmetic
- Define a 1D array with [0,12,24,36,48,60,72,84,96]
- Multiple all elements by 2
- Take all elements to the power of 2
- Find the maximum value of the array and its position
- Find the minimum value of the array and its position
- Define another 1D array with [-12,0,12,24,36,48,60,72,84]
- Find the summation and subtraction of these two arrays
- Find the multiplication of these two arrays


```python
import numpy as np         #import numpy
Array1 = np.array([0,12,24,36,48,60,72,84,96])     #Step1: Define Array1
print(Array1)
print(Array1*2)     #Step2: Multiple all elements by 2
print(Array1**2)     #Step3: Take all elements to the power of 2
print(np.power(Array1,2)) #Another way to do the same thing, by using a function in numpy
print(np.max(Array1))     #Step4: Find the maximum value of the array
print(np.argmax(Array1))     ##Step4: Find the postition of the maximum value 
print(np.min(Array1))     #Step5: Find the minimum value of the array
print(np.argmin(Array1))     ##Step5: Find the postition of the minimum value 
Array2 = np.array([-12,0,12,24,36,48,60,72,84])     #Step6: Define Array2
print(Array2)
print(Array1+Array2)         #Step7: Find the summation of these two arrays
print(Array1-Array2)         #Step7: Find the subtraction of these two arrays
print(Array1*Array2)         #Step8: Find the multiplication of these two arrays

```

    [ 0 12 24 36 48 60 72 84 96]
    [  0  24  48  72  96 120 144 168 192]
    [   0  144  576 1296 2304 3600 5184 7056 9216]
    [   0  144  576 1296 2304 3600 5184 7056 9216]
    96
    8
    0
    0
    [-12   0  12  24  36  48  60  72  84]
    [-12  12  36  60  84 108 132 156 180]
    [12 12 12 12 12 12 12 12 12]
    [   0    0  288  864 1728 2880 4320 6048 8064]


___
### Example- n-Dimensional Array Arithmetic
- Define a 2x2 array with [5,10,15,20]
- Define another 2x2 array with [3,6,9,12]
- Find the summation and subtraction of these two arrays
- Find the minimum number in the multiplication of these two arrays
- Find the position of the maximum in the multiplication of these two arrays
- Find the mean of the multiplication of these two arrays
- Find the mean of the first row of the multiplication of these two arrays



```python
import numpy as np         #import numpy
Array1 = np.array([[5,10],[15,20]])     #Step1: Define Array1
print(Array1)
Array2 = np.array([[3,6],[9,12]])     #Step2: Define Array2
print(Array2)
print(Array1+Array2)     #Step3: Find the summation
print(Array1-Array2)     #Step3: Find the subtraction
MultArray = Array1@Array2         #Step4: To perform a typical matrix multiplication (or matrix product)
MultArray1 = Array1.dot(Array2)         #Step4: Another way To perform a  matrix multiplication
print(MultArray)
print(MultArray1)
print(np.min(MultArray))     #Step4: Find the minimum value of the multiplication
print(np.argmax(MultArray))     ##Step5: Find the postition of the maximum value 
print(np.mean(MultArray))     ##Step6: Find the mean of the multiplication of these two arrays 
print(np.mean(MultArray[0,:]))     ##Step7: Find the mean of the first row of the multiplication of these two arrays 

```

    [[ 5 10]
     [15 20]]
    [[ 3  6]
     [ 9 12]]
    [[ 8 16]
     [24 32]]
    [[2 4]
     [6 8]]
    [[105 150]
     [225 330]]
    [[105 150]
     [225 330]]
    105
    3
    202.5
    127.5


___
### <font color=purple>Arrays Comparison</font>


Comparing two NumPy arrays determines whether they are equivalent by checking if every element at each corresponding index are the same.

![](https://www.w3resource.com/w3r_images/python-numpy-image-exercise-28.png)

___
### Example- 1D Array Comparison
- Define a 1D array with [1.0,2.5,3.4,7,7]
- Define another 1D array with [5.0/5.0,5.0/2,6.8/2,21/3,14/2]
- Compare and see if the two arrays are equal
- Define another 1D array with [6,1.4,2.2,7.5,7]
- Compare and see if the first array is greater than or equal to the third array


```python
import numpy as np         #import numpy
Array1 = np.array([1.0,2.5,3.4,7,7])     #Step1: Define Array1
print(Array1)
Array2 = np.array([5.0/5.0,5.0/2,6.8/2,21/3,14/2])     #Step2: Define Array1
print(Array2)
print(np.equal(Array1, Array2))             #Step3: Compare and see if the two arrays are equal
Array3 = np.array([6,1.4,2.2,7.5,7])     #Step4: Define Array3
print(Array3)
print(np.greater_equal(Array1, Array3))             #Step3: Compare and see if the two arrays are equal

```

    [1.  2.5 3.4 7.  7. ]
    [1.  2.5 3.4 7.  7. ]
    [ True  True  True  True  True]
    [6.  1.4 2.2 7.5 7. ]
    [False  True  True False  True]


___
### <font color=purple>Arrays Manipulation</font>

numpy.copy() allows us to create a copy of an array. This is particularly useful when we need to manipulate an array while keeping an original copy in memory.
The numpy.delete() function returns a new array with sub-arrays along an axis deleted. Let's have a look at the examples.


![](https://codetorial.net/numpy/_images/numpy_delete_01.png)
![](https://www.w3resource.com/w3r_images/numpy-manipulation-delete-function-image-1.png)

___
### Example- Copying and Deleting Arrays and Elements
- Define a 1D array, named "x" with [1,2,3]
- Define "y" so that "y=x"
- Define "z" as a copy of "x"
- Discuss the difference between y and z
- Delete the second element of x


```python
import numpy as np         #import numpy
x = np.array([1,2,3])     #Step1: Define x
print(x)
y = x                     #Step2: Define y as y=x
print(y)
z = np.copy(x)            #Step3: Define z as a copy of x
print(z)
# For Step4: They look similar but check this out:
x[1] = 8                  # If we change x ...
print(x)
print(y)
print(z)
# By modifying x, y changes but z remains as a copy of the initial version of x.
x = np.delete(x, 1)      #Step5: Delete the second element of x
print(x)
```

    [1 2 3]
    [1 2 3]
    [1 2 3]
    [1 8 3]
    [1 8 3]
    [1 2 3]
    [1 3]


___
### <font color=purple>Sorting Arrays</font>

Sorting means putting elements in an ordered sequence. Ordered sequence is any sequence that has an order corresponding to elements, like numeric or alphabetical, ascending or descending. If you use the sort() method on a 2-D array, both arrays will be sorted.

![](https://www.w3resource.com/w3r_images/numpy-sorting-and-searching-image-exercise-1.svg)

___
### Example- Sorting 1D Arrays
__Define a 1D array as ['FIFA 2020','Red Dead Redemption','Fallout','GTA','NBA 2018','Need For Speed'] and print it out. Then, sort the array alphabetically.__



```python
import numpy as np         #import numpy
games = np.array(['FIFA 2020','Red Dead Redemption','Fallout','GTA','NBA 2018','Need For Speed'])
print(games)
print(np.sort(games))
```

    ['FIFA 2020' 'Red Dead Redemption' 'Fallout' 'GTA' 'NBA 2018'
     'Need For Speed']
    ['FIFA 2020' 'Fallout' 'GTA' 'NBA 2018' 'Need For Speed'
     'Red Dead Redemption']


___
### Example- Sorting n-Dimensional Arrays
__Define a 3x3 array with 17,-6,2,86,-12,0,0,23,12 and print it out. Then, sort the array.__


```python
import numpy as np         #import numpy
a = np.array([[17,-6,2],[86,-12,0],[0,23,12]])
print(a)
print ("Along columns : \n", np.sort(a,axis = 0) ) #This will be sorting in each column
print ("Along rows : \n", np.sort(a,axis = 1) ) #This will be sorting in each row
print ("Sorting by default : \n", np.sort(a) )          #Same as above
print ("Along None Axis : \n", np.sort(a,axis = None) ) #This will be sorted like a 1D array

```

    [[ 17  -6   2]
     [ 86 -12   0]
     [  0  23  12]]
    Along columns : 
     [[  0 -12   0]
     [ 17  -6   2]
     [ 86  23  12]]
    Along rows : 
     [[ -6   2  17]
     [-12   0  86]
     [  0  12  23]]
    Sorting by default : 
     [[ -6   2  17]
     [-12   0  86]
     [  0  12  23]]
    Along None Axis : 
     [-12  -6   0   0   2  12  17  23  86]


___
### <font color=purple>Partitioning (Slice) Arrays</font>


Slicing in python means taking elements from one given index to another given index.

We can do slicing like this: [start:end].

We can also define the step, like this: [start:end:step].

If we don't pass start its considered 0

If we don't pass end its considered length of array in that dimension

If we don't pass step its considered 1

![](https://media.geeksforgeeks.org/wp-content/uploads/Numpy1.jpg)

___
### Example- Slicing 1D Arrays
__Define a 1D array as [1,3,5,7,9], slice out the [3,5,7] and print it out.__


```python
import numpy as np         #import numpy
a = np.array([1,3,5,7,9])     #Define the array
print(a)
aslice = a[1:4]             #slice the [3,5,7]
print(aslice)               #print it out

```

    [1 3 5 7 9]
    [3 5 7]


___
### Example- Slicing n-Dimensional Arrays
__Define a 5x5 array with "Superman, Batman, Jim Hammond, Captain America, Green Arrow, Aquaman, Wonder Woman, Martian Manhunter, Barry Allen, Hal Jordan, Hawkman, Ray Palmer, Spider Man, Thor, Hank Pym, Solar, Iron Man, Dr. Strange, Daredevil, Ted Kord, Captian Marvel, Black Panther, Wolverine, Booster Gold, Spawn " and print it out. Then:__
- Slice the first column and print it out
- Slice the third row and print it out
- Slice 'Wolverine' and print it out
- Slice a 3x3 array with 'Wonder Woman, Ray Palmer, Iron Man, Martian Manhunter, Spider Man, Dr. Strange, Barry Allen, Thor, Daredevil'


```python
import numpy as np         #import numpy
Superheroes = np.array([['Superman', 'Batman', 'Jim Hammond', 'Captain America', 'Green Arrow'],
               ['Aquaman', 'Wonder Woman', 'Martian Manhunter', 'Barry Allen', 'Hal Jordan'],
               ['Hawkman', 'Ray Palmer', 'Spider Man', 'Thor', 'Hank Pym'],
               ['Solar', 'Iron Man', 'Dr. Strange', 'Daredevil', 'Ted Kord'],
               ['Captian Marvel', 'Black Panther', 'Wolverine', 'Booster Gold', 'Spawn']])
print(Superheroes) #Step1
print(Superheroes[:,0])
print(Superheroes[2,:])
print(Superheroes[4,2])
print(Superheroes[1:4,1:4])
```

    [['Superman' 'Batman' 'Jim Hammond' 'Captain America' 'Green Arrow']
     ['Aquaman' 'Wonder Woman' 'Martian Manhunter' 'Barry Allen' 'Hal Jordan']
     ['Hawkman' 'Ray Palmer' 'Spider Man' 'Thor' 'Hank Pym']
     ['Solar' 'Iron Man' 'Dr. Strange' 'Daredevil' 'Ted Kord']
     ['Captian Marvel' 'Black Panther' 'Wolverine' 'Booster Gold' 'Spawn']]
    ['Superman' 'Aquaman' 'Hawkman' 'Solar' 'Captian Marvel']
    ['Hawkman' 'Ray Palmer' 'Spider Man' 'Thor' 'Hank Pym']
    Wolverine
    [['Wonder Woman' 'Martian Manhunter' 'Barry Allen']
     ['Ray Palmer' 'Spider Man' 'Thor']
     ['Iron Man' 'Dr. Strange' 'Daredevil']]


___
## <font color=orange>This is a Numpy Cheat Sheet- similar to the one you had on top of this notebook!</font>

![](https://blog.finxter.com/wp-content/uploads/2019/10/grafik-1-1024x725.png)

### Check out this link for more: <br>
https://blog.finxter.com/collection-10-best-numpy-cheat-sheets-every-python-coder-must-own/

___
![](https://media2.giphy.com/media/5nj4ZZWl6QwneEaBX4/source.gif) <br>

*Here are some of the resources used for creating this notebook:* 
- Johnson, J. (2020). Python Numpy Tutorial (with Jupyter and Colab). Retrieved September 15, 2020, from https://cs231n.github.io/python-numpy-tutorial/ <br>
- Willems, K. (2019). (Tutorial) Python NUMPY Array TUTORIAL. Retrieved September 15, 2020, from https://www.datacamp.com/community/tutorials/python-numpy-tutorial?utm_source=adwords_ppc <br>
- Willems, K. (2017). NumPy Cheat Sheet: Data Analysis in Python. Retrieved September 15, 2020, from https://www.datacamp.com/community/blog/python-numpy-cheat-sheet <br>
- W3resource. (2020). NumPy: Compare two given arrays. Retrieved September 15, 2020, from https://www.w3resource.com/python-exercises/numpy/python-numpy-exercise-28.php <br>



*Here are some great reads on this topic:* 
- __"Python NumPy Tutorial"__ available at *https://www.geeksforgeeks.org/python-numpy-tutorial/<br>
- __"What Is NumPy?"__ a collection of blogs, available at *https://realpython.com/tutorials/numpy/ <br>
- __"Look Ma, No For-Loops: Array Programming With NumPy"__ by __Brad Solomon__ available at *https://realpython.com/numpy-array-programming/ <br>
- __"The Ultimate Beginner’s Guide to NumPy"__ by __Anne Bonner__ available at *https://towardsdatascience.com/the-ultimate-beginners-guide-to-numpy-f5a2f99aef54 <br>


*Here are some great videos on these topics:* 
- __"Learn NUMPY in 5 minutes - BEST Python Library!"__ by __Python Programmer__ available at *https://www.youtube.com/watch?v=xECXZ3tyONo <br>
- __"Python NumPy Tutorial for Beginners"__ by __freeCodeCamp.org__ available at *https://www.youtube.com/watch?v=QUT1VHiLmmI <br>
- __"Complete Python NumPy Tutorial (Creating Arrays, Indexing, Math, Statistics, Reshaping)"__ by __Keith Galli__ available at *https://www.youtube.com/watch?v=GB9ByFAIAH4 <br>
- __"Python NumPy Tutorial | NumPy Array | Python Tutorial For Beginners | Python Training | Edureka"__ by __edureka!__ available at *https://www.youtube.com/watch?v=8JfDAm9y_7s <br>

___
![](https://media.csesoc.org.au/content/images/2019/10/learn11.gif) <br>


## Exercise: Python List vs. Numpy Arrays? <br>

### What are some differences between Python lists and Numpy arrays?

   

#### * Make sure to cite any resources that you may use. 


```python

```

![](https://quotefancy.com/media/wallpaper/3840x2160/722175-Pythagoras-Quote-Number-rules-the-universe.jpg)
