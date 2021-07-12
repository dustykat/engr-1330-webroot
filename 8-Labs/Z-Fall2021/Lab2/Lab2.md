**Download** (right-click, save target as ...) this page as a jupyterlab notebook from:

[Lab2](https://atomickitty.ddns.net:8000/user/sensei/files/engr-1330-webroot/engr-1330-webbook/ctds-psuedocourse/docs/8-Labs/Lab1/Lab2_Dev.ipynb?_xsrf=2%7C1b4d47c3%7C0c3aca0c53606a3f4b71c448b09296ae%7C1623531240)

___

# <font color=darkred>Laboratory 2: First Steps... </font>



![](https://i1.wp.com/timemanagementninja.com/wp-content/uploads/2013/10/First-Steps.jpg?resize=600%2C400) <br>


### Notice the code cell below!
### From this notebook forward please include and run the script in the cell, it will help in debugging a notebook.


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


### Also, from now on, please make sure that you have the following markdown cell, filled with your own information, on top of your notebooks:

## Full name: 
## R#: 
## Title of the notebook:
## Date: 
___

### Now, let's get to work!

![](https://www.shutterstock.com/blog/wp-content/uploads/sites/5/2019/06/Variable-Font-Demo-3.gif) <br>

## <font color=purple>Variables</font>

Variables are names given to data that we want to store and manipulate in programs. A
variable has a name and a value. The value representation depends on what type of object
the variable represents.
The utility of variables comes in when we have a structure that is universal, but values of
variables within the structure will change - otherwise it would be simple enough to just
hardwire the arithmetic.

Suppose we want to store the time of concentration for some hydrologic calculation. 
To do so, we can name a variable `TimeOfConcentration`, and then `assign` a value to the variable,
for instance:


```python
TimeOfConcentration = 0.0
```

After this assignment statement the variable is created in the program and has a value of 0.0. 
The use of a decimal point in the initial assignment establishes the variable as a float (a real variable is called a floating point representation -- or just a float).


```python
TimeOfConcentration + 5
```




    5.0



### <font color=purple>Naming Rules</font>

Variable names in Python can only contain letters (a - z, A - Z), numerals (0 - 9), or underscores. 
The first character cannot be a number, otherwise there is considerable freedom in naming. 
The names can be reasonably long. 
`runTime`, `run_Time`, `_run_Time2`, `_2runTime` are all valid names, but `2runTime` is not valid, and will create an error when you try to use it.


```python
# Script to illustrate variable names
runTime = 1
_2runTime = 2 # change to 2runTime = 2 and rerun script
runTime2 = 2
print(runTime,_2runTime,runTime2)
```

    1 2 2


There are some reserved words that cannot be used as variable names because they have preassigned meaning in Parseltongue. These words include print, input, if, while, and for. There are several more; the interpreter won't allow you to use these names as variables and will issue an error message when you attempt to run a program with such words used as variables.

___
## <font color=purple>Operators</font>

The `=` sign used in the variable definition is called an assignment operator (or assignment sign). 
The symbol means that the expression to the right of the symbol is to be evaluated and the result placed into the variable on the left side of the symbol.  The "operation" is assignment, the "=" symbol is the operator name.

Consider the script below:


```python
# Assignment Operator
x = 5
y = 10
print (x,y)
x=y # reverse order y=x and re-run, what happens?
print (x,y)
```

    5 10
    10 10


So look at what happened. When we assigned values to the variables named `x` and `y`, they started life as 5 and 10. 
We then wrote those values to the console, and the program returned 5 and 10. 
Then we assigned `y` to `x` which took the value in y and replaced the value that was in x with this value. 
We then wrote the contents again, and both variables have the value 10.

### What's it with # ?
> Comments are added by writing a hashtag symbol (#) followed by any text of your choice. Any text that follows the hashtag symbol on the same line is ignored by the Python interpreter.

![](https://thumbs.gfycat.com/AgitatedRipeCicada-size_restricted.gif) <br>


___
## <font color=purple>Arithmetic Operators</font>

In addition to assignment we can also perform arithmetic operations on variables. The
fundamental arithmetic operators are:

| Symbol | Meaning | Example |
|:---|:---|:---|
| = |Assignment| x=3 Assigns value of 3 to x.|
| + |Addition| x+y Adds values in x and y.|
| - |Subtraction| x-y Subtracts values in y from x.|
|$*$ |Multiplication| x*y Multiplies values in x and y.|
| / |Division| x/y Divides value in x by value in y.|
| // |Floor division| x//y Divide x by y, truncate result to whole number.|
| % |Modulus| x%y Returns remainder when x is divided by y.|
|$**$ |Exponentation| x$**$y Raises value in x by value in y. ( e.g. xy)|
| += |Additive assignment| x+=2 Equivalent to x = x+2.|
| -= |Subtractive assignment| x-=2 Equivalent to x = x-2.|
| *= |Multiplicative assignment| x\*=3 Equivalent to x = x\*3.|
| /= |Divide assignment| x/3 Equivalent to x = x/3.|

Run the script in the next cell for some illustrative results


```python
# Uniary Arithmetic Operators
x = 10
y = 5
print(x, y)
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print((x+1)//y)
print((x+1)%y)
print(x**y)
```

    10 5
    15
    5
    50
    2.0
    2
    1
    100000



```python
# Arithmetic assignment operators
x = 1
x += 2
print(type(x),x)
x = 1
x -= 2
print(type(x),x)
x = 1
x *=3
print(type(x),x)
x = 10
x /= 2
print(type(x),x)  # Interesting what division does to variable type
```

    <class 'int'> 3
    <class 'int'> -1
    <class 'int'> 3
    <class 'float'> 5.0


___
## <font color=purple>Data Type</font>
In the computer data are all binary digits (actually 0 and +5 volts). 
At a higher level of abstraction data are typed into integers, real, or alphanumeric representation. 
The type affects the kind of arithmetic operations that are allowed (as well as the kind of arithmetic - integer versus real arithmetic; lexicographical ordering of alphanumeric , etc.)
In scientific programming, a common (and really difficult to detect) source of slight inaccuracies (that tend to snowball as the program runs) is mixed mode arithmetic required because two numeric values are of different types (integer and real).

Learn more from the textbook

https://www.inferentialthinking.com/chapters/04/Data_Types.html

Here we present a quick summary

### <font color=purple>Integer</font>
Integers are numbers without any fractional portion (nothing after the decimal point { which
is not used in integers). Numbers like -3, -2, -1, 0, 1, 2, 200 are integers. A number like 1.1
is not an integer, and 1.0 is also not an integer (the presence of the decimal point makes the
number a real).

To declare an integer in Python, just assign the variable name to an integer for example

    MyPhoneNumber = 14158576309
    
### <font color=purple>Real (Float)</font>
A real or float is a number that has (or can have) a fractional portion - the number has
decimal parts. The numbers 3.14159, -0.001, 11.11, 1., are all floats. 
The last one is especially tricky, if you don't notice the decimal point you might think it is an integer but the
inclusion of the decimal point in Python tells the program that the value is to be treated as a 
float.
To declare a 
float in Python, just assign the variable name to a 
float for example

    MyMassInKilos = 74.8427

### <font color=purple>String(Alphanumeric)</font>
A string is a data type that is treated as text elements. The usual letters are strings, but
numbers can be included. The numbers in a string are simply characters and cannot be
directly used in arithmetic. 
There are some kinds of arithmetic that can be performed on strings but generally we process string variables to capture the text nature of their contents. 
To declare a string in Python, just assign the variable name to a string value - the trick is the value is enclosed in quotes. 
The quotes are delimiters that tell the program that the characters between the quotes are characters and are to be treated as literal representation.

For example

    MyName = 'Theodore'
    MyCatName = "Dusty"
    DustyMassInKilos = "7.48427"
    
are all string variables. 
The last assignment is made a string on purpose. 
String variables can be combined using an operation called concatenation. 
The symbol for concatenation is the plus symbol `+`.

Strings can also be converted to all upper case using the `upper()` function. The syntax for
the `upper()` function is `'string to be upper case'.upper()`. 
Notice the "dot" in the syntax. 
The operation passes everything to the left of the dot to the function which then
operates on that content and returns the result all upper case (or an error if the input stream
is not a string).


```python
# Variable Types Example
MyPhoneNumber = 14158576309
MyMassInKilos = 74.8427
MyName = 'Theodore'
MyCatName = "Dusty"
DustyMassInKilos = "7.48427"
print("All about me")
print("Name: ",MyName, " Mass :",MyMassInKilos,"Kg" )
print('Phone : ',MyPhoneNumber)
print('My cat\'s name :', MyCatName)  # the \ escape character is used to get the ' into the literal
print("All about concatenation!")
print("A Silly String : ",MyCatName+MyName+DustyMassInKilos)
print("A SILLY STRING :  ", (MyCatName+MyName+DustyMassInKilos).upper())
print(MyName[0:4])    # Notice how the string is sliced- This is Python: ALWAYS start counting from zero!
```

    All about me
    Name:  Theodore  Mass : 74.8427 Kg
    Phone :  14158576309
    My cat's name : Dusty
    All about concatenation!
    A Silly String :  DustyTheodore7.48427
    A SILLY STRING :   DUSTYTHEODORE7.48427
    Theo


Strings can be formatted using the `%` operator or the `format()` function. The concepts will
be introduced later on as needed in the workbook, you can Google search for examples of
how to do such formatting.

### <font color=purple>Changing Types</font>
A variable type can be changed. 
This activity is called type casting. 
Three functions allow
type casting: `int()`, `float()`, and `str()`. 
The function names indicate the result of using
the function, hence `int()` returns an integer, `float()` returns a 
oat, and `str()` returns a
string.

There is also the useful function `type()` which returns the type of variable.

The easiest way to understand is to see an example. 


```python
# Type Casting Examples
MyInteger = 234
MyFloat = 876.543
MyString = 'What is your name?'
print(MyInteger,MyFloat,MyString)
print('Integer as float',float(MyInteger))
print('Float as integer',int(MyFloat))
print('Integer as string',str(MyInteger))
print('Integer as hexadecimal',hex(MyInteger))
print('Integer Type',type((MyInteger)))  # insert the hex conversion and see what happens!
```

___
## <font color=purple>Expressions</font>

![](https://thumbs.gfycat.com/HandsomeRegularHuman-max-1mb.gif) <br>

Expressions are the "algebraic" constructions that are evaluated and then placed into a variable.
Consider

    x1 = 7 + 3 * 6 / 2 - 1

The expression is evaluated from the left to right and in words is

    Into the object named x1 place the result of:
    
    integer 7 + (integer 6 divide by integer 2 = float 3 * integer 3 = float 9 - integer 1 = float 8) = float 15

The division operation by default produces a float result unless forced otherwise.  The result is the variable `x1` is a float with a value of `15.0`
    


```python
# Expressions Example
x1 = 7 + 3 * 6 // 2 - 1  # Change / into // and see what happens!
print(type(x1),x1)
## Simple I/O (Input/Output)
```

    <class 'int'> 15


### Example: Simple Input/Output

Get two floating point numbers via the `input()` function and store them under the variable names `float1` and `float2`. Then, compare them, and try a few operations on them!

    float1 = input("Please enter float1: ")
    float1 = float(float1) 
    ...
    
Print `float1` and `float2` to the output screen.  

    print("float1:", float1)
    ...

Then check whether `float1` is greater than or equal to `float2`.



```python
float1 = input("Please enter float1: ")
float2 = input("Please enter float2: ")
```

    Please enter float1: 2.5
    Please enter float2: 5



```python
print("float1:", float1)
print("float2:", float2)
```

    float1: 2.5
    float2: 5



```python
float1 = float(float1)
float2 = float(float2)
```


```python
print("float1:", float1)
print("float2:", float2)
```

    float1: 2.5
    float2: 5.0



```python
float1>float2
```




    False




```python
float1+float2
```




    7.5




```python
float1/float2
```




    0.5



___
![](https://media2.giphy.com/media/5nj4ZZWl6QwneEaBX4/source.gif) <br>


*Here are some great reads on this topic:* 
- __"Variables in Python"__ by __John Sturtz__ available at *https://realpython.com/python-variables/ <br>
- __"A Beginner’s Guide To Python Variables"__ by __Avijeet Biswal__ available at *https://www.simplilearn.com/tutorials/python-tutorial/python-variables <br>
- __"A Very Basic Introduction to Variables in Python"__ by __Dr. Python__ available at *https://medium.com/@doctorsmonsters/a-very-basic-introduction-to-variables-in-python-4231e36dac52 <br>


*Here are some great videos on these topics:* 
- __"Python Tutorial for Absolute Beginners #1 - What Are Variables?"__ by __CS Dojo__ available at *https://www.youtube.com/watch?v=Z1Yd7upQsXY <br>
- __"#4 Python Tutorial for Beginners | Variables in Python"__ by __Telusko__ available at *https://www.youtube.com/watch?v=TqPzwenhMj0 <br>
- __"Variables and Types in Python"__ by __DataCamp__ available at *https://www.youtube.com/watch?v=OH86oLzVzzw <br>

![](https://media.csesoc.org.au/content/images/2019/10/learn11.gif) <br>


___
## Exercise: Integer or Float? <br>


### Think of a few cases where one might need to convert a float into an integer.

#### * Make sure to cite any resources that you may use. 



![](https://quotefancy.com/media/wallpaper/3840x2160/959294-Douglas-Horton-Quote-Beauty-is-variable-ugliness-is-constant.jpg)
