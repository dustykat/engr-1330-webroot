**Download** (right-click, save target as ...) this page as a jupyterlab notebook from:

[Lab6](https://atomickitty.ddns.net:8000/user/sensei/files/engr-1330-webroot/engr-1330-webbook/ctds-psuedocourse/docs/8-Labs/Lab4/Lab6_Dev.ipynb?_xsrf=2%7C1b4d47c3%7C0c3aca0c53606a3f4b71c448b09296ae%7C1623531240)

___

# <font color=darkred>Laboratory 6: FUNctions </font>


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

![](https://runestone.academy/runestone/books/published/fopp/_images/function_call.gif) <br>

## <font color=purple>What is a function in Python?</font>

Functions are simply pre-written code fragments that perform a certain task.
In older procedural languages functions and subroutines are similar, but a function returns a value whereas
a subroutine operates on data. 
The difference is subtle but important. 

More recent thinking has functions being able to operate on data (they always could) and the value returned may be simply an exit code.
An analogy are the functions in *MS Excel*. 
To add numbers, we can use the sum(range) function and type `=sum(A1:A5)` instead of typing `=A1+A2+A3+A4+A5`
___
## <font color=purple>Calling the Function</font>

We call a function simply by typing the name of the function or by using the dot notation.
Whether we can use the dot notation or not depends on how the function is written, whether it is part of a class, and how it is imported into a program.

Some functions expect us to pass data to them to perform their tasks. 
These data are known as parameters( older terminology is arguments, or argument list) and we pass them to the function by enclosing their values in parenthesis ( ) separated by commas. 

For instance, the `print()` function for displaying text on the screen is \called" by typing `print('Hello World')` where print is the name of the function and the literal (a string) 'Hello World' is the argument.
___
## <font color=purple>Program flow</font>

A function, whether built-in, or added must be defined *before* it is called, otherwise the script will fail.  Certain built-in functions "self define" upon start (such as `print()` and `type()` and we need not worry about those funtions).  The diagram below illustrates the requesite flow control for functions that need to be defined before use.

![](https://atomickitty.ddns.net:8000/user/sensei/files/engr-1330-webroot/engr-1330-webbook/ctds-psuedocourse/docs/8-Labs/Lab4/flow-control-diagram.png?_xsrf=2%7C1b4d47c3%7C0c3aca0c53606a3f4b71c448b09296ae%7C1623531240)
___
An example below  will illustrate, change the cell to code and run it, you should get an error.
Then fix the indicated line (remove the leading "#" in the import math ... line) and rerun, should get a functioning script.


```python
# reset the notebook using a magic function in JupyterLab
%reset -f 
# An example, run once as is then activate indicated line, run again - what happens?
x= 4.
sqrt_by_arithmetic = x**0.5
print('Using arithmetic square root of ', x, ' is ',sqrt_by_arithmetic )
#import math # import the math package ## activate and rerun
sqrt_by_math = math.sqrt(x)  # note the dot notation
print('Using math package square root of ',  x,' is ',sqrt_by_arithmetic)
```


```python
# Here is an alternative way: We just load the function that we want:
# reset the notebook using a magic function in JupyterLab
%reset -f 
# An example, run once as is then activate indicated line, run again - what happens?
x= 4.
sqrt_by_arithmetic = x**0.5
print('Using arithmetic square root of ', x, ' is ',sqrt_by_arithmetic )
from math import sqrt # import sqrt from the math package ## activate and rerun
sqrt_by_math = sqrt(x)  # note the notation
print('Using math package square root of ',  x,' is ',sqrt_by_arithmetic)
```

    Using arithmetic square root of  4.0  is  2.0
    Using math package square root of  4.0  is  2.0


___
## <font color=purple>Built-In in Primitive Python (Base install)</font>

The base Python functions and types built into it that are always available, the figure below lists those functions.

![](https://atomickitty.ddns.net:8000/user/sensei/files/engr-1330-webroot/engr-1330-webbook/ctds-psuedocourse/docs/8-Labs/Lab4/base-functions.png?_xsrf=2%7C1b4d47c3%7C0c3aca0c53606a3f4b71c448b09296ae%7C1623531240)

Notice all have the structure of `function_name()`, except `__import__()` which has a constructor type structure, and is not intended for routine use.  We will learn about constructors later.


___
## <font color=purple>Added-In using External Packages/Modules and Libaries (e.g. math)</font>

Python is also distributed with a large number of external functions. 
These functions are saved
in files known as modules. 
To use the built-in codes in Python modules, we have to import
them into our programs first. We do that by using the import keyword. 
There are three
ways to import:
1. Import the entire module by writing import moduleName; For instance, to import the random module, we write import random. To use the randrange() function in the random module, we write random.randrange( 1, 10);28
2. Import and rename the module by writing import random as r (where r is any name of your choice). Now to use the randrange() function, you simply write r.randrange(1, 10); and
3. Import specific functions from the module by writing from moduleName import name1[,name2[, ... nameN]]. For instance, to import the randrange() function from the random module, we write from random import randrange. To import multiple functions, we separate them with a comma. To import the randrange() and randint() functions, we write from random import randrange, randint. To use the function now, we do not have to use the dot notation anymore. Just write randrange( 1, 10).


```python
# Example 1 of import
%reset -f 
import random
low = 1 ; high = 10
random.randrange(low,high) #generate random number in range low to high
```




    4




```python
# Example 2 of import
%reset -f 
import random as r
low = 1 ; high = 10
r.randrange(low,high)
```




    7




```python
# Example 3 of import
%reset -f 
from random import randrange 
low = 1 ; high = 10
randrange(low,high)
```




    5



___
The modules that come with Python are extensive and listed at 
https://docs.python.org/3/py-modindex.html.
There are also other modules that can be downloaded and used
(just like user defined modules below). 
In these labs we are building primitive codes to learn how to code and how to create algorithms. 
For many practical cases you will want to load a well-tested package to accomplish the tasks. 

That exercise is saved for the end of the document.

## <font color=purple>User-Built</font>

We can define our own functions in Python and reuse them throughout the program.
The syntax for defining a function is:

    def functionName( argument ):
        code detailing what the function should do
        note the colon above and indentation
        ...
        ...
        return [expression]
        
The keyword `def` tells the program that the indented code from the next line onwards is
part of the function. 
The keyword `return `tells the program to return an answer from the
function. 
There can be multiple return statements in a function. 
Once the function executes
a return statement, the program exits the function and continues with *its* next executable
statement. 
If the function does not need to return any value, you can omit the return
statement.

Functions can be pretty elaborate; they can search for things in a list, determine variable
types, open and close files, read and write to files. 

To get started we will build a few really
simple mathematical functions; we will need this skill in the future anyway, especially in
scientific programming contexts.

___
### <font color=purple>User-built within a Code Block</font>
 
For our first function we will code $$f(x) = x\sqrt{1 + x}$$ into a function named `dusty()`.

When you run the next cell, all it does is prototype the function (defines it), nothing happens until we use the function.


```python
def dusty(x) :
    temp = x * ((1.0+x)**(0.5)) # don't need the math package
    return temp
# the function should make the evaluation
# store in the local variable temp
# return contents of temp
```


```python
# wrapper to run the dusty function
yes = 0
while yes == 0:
    xvalue = input('enter a numeric value')
    try:
        xvalue = float(xvalue)
        yes = 1
    except:
        print('enter a bloody number! Try again \n')
# call the function, get value , write output
yvalue = dusty(xvalue)
print('f(',xvalue,') = ',yvalue) # and we are done 
```

    enter a numeric value 5


    f( 5.0 ) =  12.24744871391589


___
### Example: The Average Function

Create the AVERAGE function for three values and test it for these values:
- 3,4,5
- 10,100,1000
- -5,15,5


```python
def AVERAGE3(x,y,z) : #define the function "AVERAGE3"
    Ave = (x+y+z)/3  #computes the average
    return Ave
```


```python
print(AVERAGE3(3,4,5))
print(AVERAGE3(10,100,1000))
print(AVERAGE3(-5,15,5))
```

    4.0
    370.0
    5.0


___
### Example: The KATANA Function

Create the Katana function for rounding off to the nearest hundredths (to 2 decimal places) and test it for these values:
- 25.33694
- 15.753951
- 3.14159265359


```python
def Katana(x) : #define the function "Katana"
    newX = round(x, 2)
    return newX
```


```python
print(Katana(25.33694))
print(Katana(15.753951))
print(Katana(3.14159265359))
```

    25.34
    15.75
    3.14


___
## <font color=purple>Variable Scope</font>
An important concept when defining a function is the concept of variable scope. 
Variables defined inside a function are treated differently from variables defined outside. 
Firstly, any variable declared within a function is only accessible within the function. 
These are known as local variables. 

In the `dusty()` function, the variables `x` and `temp` are local to the function.
Any variable declared outside a function in a main program is known as a program variable
and is accessible anywhere in the program. 

In the example, the variables `xvalue` and `yvalue` are program variables (global to the program; if they are addressed within a function, they could be operated on.)
Generally we want to protect the program variables from the function unless the intent is to change their values. 
The way the function is written in the example, the function cannot damage `xvalue` or `yvalue`.

If a local variable shares the same name as a program variable, any code inside the function is
accessing the local variable. Any code outside is accessing the program variable

___
### <font color=purple>As Separate Module/File</font>

In this section we will invent the `neko()` function, export it to a file, so we can reuse it in later notebooks without having to retype or cut-and-paste. The `neko()` function evaluates:

$$f(x) = x\sqrt{|(1 + x)|}$$

Its the same as the dusty() function, except operates on the absolute value in the wadical.

1. Create a text file named "mylibrary.txt"
2. Copy the neko() function script below into that file.

        def neko(input_argument) :
            import math #ok to import into a function
            local_variable = input_argument * math.sqrt(abs(1.0+input_argument))
            return local_variable


4. rename mylibrary.txt to mylibrary.py
5. modify the wrapper script to use the neko function as an external module


```python
# wrapper to run the neko function
import mylibrary
yes = 0
while yes == 0:
    xvalue = input('enter a numeric value')
    try:
        xvalue = float(xvalue)
        yes = 1
    except:
        print('enter a bloody number! Try again \n')
# call the function, get value , write output
yvalue = mylibrary.neko(xvalue)
print('f(',xvalue,') = ',yvalue) # and we are done 
```

    enter a numeric value 5


    f( 5.0 ) =  12.24744871391589


___
In JupyterHub environments, you may discover that changes you make to your external python file are not reflected when you re-run your script; you need to restart the kernel to get the changes to actually update. The figure below depicts the notebook, external file relatonship

![](https://atomickitty.ddns.net:8000/user/sensei/files/engr-1330-webroot/engr-1330-webbook/ctds-psuedocourse/docs/8-Labs/Lab4/external-file-import.png?_xsrf=2%7C1b4d47c3%7C0c3aca0c53606a3f4b71c448b09296ae%7C1623531240)



___

### <font color=purple>Rudimentary Graphics</font>

Graphing values is part of the broader field of data visualization, which has two main
goals:

   1. To explore data, and
   2. To communicate data.

In this subsection we will concentrate on introducing skills to start exploring data and to
produce meaningful visualizations we can use throughout the rest of this notebook. 
Data visualization is a rich field of study that fills entire books.
The reason to start visualization here instead of elsewhere is that with functions plotting
is a natural activity and we have to import the matplotlib module to make the plots.

The example below is code adapted from Grus (2015) that illustrates simple generic
plots. I added a single line (label the x-axis), and corrected some transcription
errors (not the original author's mistake, just the consequence of how the API handled the
cut-and-paste), but otherwise the code is unchanged.


```python
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
```


    
![png](output_28_0.png)
    



```python
# Now lets put the plotting script into a function so we can make line charts of any two numeric lists

def plotAline(list1,list2,strx,stry,strtitle): # plot list1 on x, list2 on y, xlabel, ylabel, title
    from matplotlib import pyplot as plt # import the plotting library from matplotlibplt.show()
    plt.plot( list1, list2, color ='green', marker ='o', linestyle ='solid') # create a line chart, years on x-axis, gdp on y-axis
    plt.title(strtitle)# add a title
    plt.ylabel(stry)# add a label to the x and y-axes
    plt.xlabel(strx)
    plt.show() # display the plot
    return #null return
```


```python
# wrapper
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]  # define two lists years and gdp
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]
print(type(years[0]))
print(type(gdp[0]))
plotAline(years,gdp,"Year","Billions of $","Nominal GDP")
```

    <class 'int'>
    <class 'float'>



    
![png](output_30_1.png)
    


___
### Example- The Hopeless Romantic! 
Copy the wrapper script for the `plotAline()` function, and modify the copy to create a plot of
$$ x = 16sin^3(t) $$
$$ y = 13cos(t) - 5cos(2t) - 2cos(3t) - cos(4t) $$
for t raging from [0,2$\Pi$] (inclusive).

Label the plot and the plot axes.



```python
from matplotlib import pyplot as plt # import the plotting library 
import numpy as np # import NumPy: for large, multi-dimensional arrays and matrices, along with  high-level mathematical functions to operate on these arrays.
pi = np.pi #pi value from the np package
t= np.linspace(0,2*pi,360)# the NumPy function np.linspace is similar to the range()

x = 16*np.sin(t)**3
y = 13*np.cos(t) - 5*np.cos(2*t) - 2*np.cos(3*t) - np.cos(4*t)

plt.plot( x, y, color ='purple', marker ='.', linestyle ='solid') 
plt.ylabel("Y-axis")# add a label to the x and y-axes
plt.xlabel("X-axis")
plt.axis('equal') #sets equal axis ratios
plt.title("A Hopeless Romantic's Curve")# add a title
plt.show() # display the plot
```


    
![png](output_32_0.png)
    


___
![](https://media2.giphy.com/media/5nj4ZZWl6QwneEaBX4/source.gif) <br>


*Here are some great reads on this topic:* 
- __"Functions in Python"__ available at *https://www.geeksforgeeks.org/functions-in-python/<br>
- __"Defining Your Own Python Function"__ by __John Sturtz__ available at *https://realpython.com/defining-your-own-python-function/ <br>
- __"Graph Plotting in Python | Set 1"__ available at *https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/ <br>
- __"Python Plotting With Matplotlib (Guide)"__ by __Brad Solomon__ available at *https://realpython.com/python-matplotlib-guide/ <br>

*Here are some great videos on these topics:* 
- __"How To Use Functions In Python (Python Tutorial #3)"__ by __CS Dojo__ available at *https://www.youtube.com/watch?v=NSbOtYzIQI0 <br>
- __"Python Tutorial for Beginners 8: Functions"__ by __Corey Schafer__ available at *https://www.youtube.com/watch?v=9Os0o3wzS_I <br>
- __"Python 3 Programming Tutorial - Functions"__ by __sentdex__ available at *https://www.youtube.com/watch?v=owglNL1KQf0 <br><br>

![](https://media.csesoc.org.au/content/images/2019/10/learn11.gif) <br>
___


## Exercise: A Function for Coffee. Because Coffee is life! <br>

![](https://i.pinimg.com/originals/0c/ba/0a/0cba0a85d486b2d4b94b352cbcf410c5.png) <br>

### Write a pseudo-code for a function that asks for user's preferences on their coffee (e.g., type of brew), follows certain steps to prepare that coffee, and delivers that coffee with an appropriate message. You can be as imaginative as you like, but make sure to provide logical justification for your script.      

#### * Make sure to cite any resources that you may use. 


```python

```

![](https://i.pinimg.com/originals/d9/05/74/d90574bbfd1fc794927da511fb4db59a.jpg)
