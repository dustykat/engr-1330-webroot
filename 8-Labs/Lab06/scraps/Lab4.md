**Download** (right-click, save target as ...) this page as a jupyterlab notebook from:

[Lab4](https://atomickitty.ddns.net:8000/user/sensei/files/engr-1330-webroot/engr-1330-webbook/ctds-psuedocourse/docs/8-Labs/Lab3/Lab4_Dev.ipynb?_xsrf=2%7C1b4d47c3%7C0c3aca0c53606a3f4b71c448b09296ae%7C1623531240)

___

# <font color=darkred>Laboratory 4: Loops, Looops, Loooooops </font>


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

![](https://i.pinimg.com/originals/d0/45/12/d04512a3837fd4c7cf88efe26883e037.gif) <br>

## <font color=purple>Program flow control (Loops)</font>
- Controlled repetition
- Structured FOR Loop
- Structured WHILE Loop

### <font color=purple>Count controlled repetition</font>
![](https://chortle.ccsu.edu/assemblytutorial/Chapter-18/countingLoop.gif) <br>

Count-controlled repetition is also called definite repetition because the number of repetitions is known before the loop begins executing. 
When we do not know in advance the number of times we want to execute a statement, we cannot use count-controlled repetition. 
In such an instance, we would use sentinel-controlled repetition. 

A count-controlled repetition will exit after running a certain number of times. 
The count is kept in a variable called an index or counter. 
When the index reaches a certain value (the loop bound) the loop will end. 

Count-controlled repetition requires

* control variable (or loop counter)
* initial value of the control variable
* increment (or decrement) by which the control variable is modified each iteration through the loop
* condition that tests for the final value of the control variable 

We can use both `for` and `while` loops, for count controlled repetition, but the `for` loop in combination with the `range()` function is more common.

#### Structured `FOR` loop
We have seen the for loop already, but we will formally introduce it here. The `for` loop executes a block of code repeatedly until the condition in the `for` statement is no longer true.

#### Looping through an iterable
An iterable is anything that can be looped over - typically a list, string, or tuple. 
The syntax for looping through an iterable is illustrated by an example.

First a generic syntax

    for a in iterable:
    print(a)
    
Notice the colon `:` and the indentation.
Now a specific example:

___
### Example: A Loop to Begin With! 

Make a list with "Walter", "Jesse", "Gus, "Hank". Then, write a loop that prints all the elements of your lisk.


```python
# set a list
BB = ["Walter","Jesse","Gus","Hank"]
# loop thru the list
for AllStrings in BB:
    print(AllStrings)
```

    Walter
    Jesse
    Gus
    Hank


___
#### The `range()` function to create an iterable

The `range(begin,end,increment)` function will create an iterable starting at a value of begin, in steps defined by increment (`begin += increment`), ending at `end`. 

So a generic syntax becomes

    for a in range(begin,end,increment):
    print(a)

The example that follows is count-controlled repetition (increment skip if greater)


```python
# set a list
BB = ["Walter","Jesse","Gus","Hank"]
# loop thru the list
for i in range(0,4,1): # Change the numbers, what happens?
    print(BB[i])
```

    Walter
    Jesse
    Gus
    Hank


___
### Example: That's odd! 

Write a loop to print all the odd numbers between 0 and 10.


```python
# For loop with range
for x in range(1,10,2): # a sequence from 2 to 5 with steps of 1
  print(x)
```

    1
    3
    5
    7
    9


___
### <font color=purple>Sentinel-controlled repetition</font>
![](https://media.geeksforgeeks.org/wp-content/uploads/20191119172228/Flow-Diagram-do-while-loop.jpg) <br>

When loop control is based on the value of what we are processing, sentinel-controlled repetition is used. 
Sentinel-controlled repetition is also called indefinite repetition because it is not known in advance how many times the loop will be executed. 


![](https://media0.giphy.com/media/3Xw8jY3zbFRtFd6eK8/giphy.gif) <br>

It is a repetition procedure for solving a problem by using a sentinel value (also called a signal value, a dummy value or a flag value) to indicate "end of process". 
The sentinel value itself need not be a part of the processed data.

One common example of using sentinel-controlled repetition is when we are processing data from a file and we do not know in advance when we would reach the end of the file. 

We can use both `for` and `while` loops, for __Sentinel__ controlled repetition, but the `while` loop is more common.

#### Structured `WHILE` loop
The `while` loop repeats a block of instructions inside the loop while a condition remainsvtrue.

First a generic syntax

    while condition is true:
        execute a
        execute b
    ....

Notice our friend, the colon `:` and the indentation again.


```python
# set a counter
counter = 5
# while loop
while counter > 0:
    print("Counter = ",counter)
    counter = counter -1
```

    Counter =  5
    Counter =  4
    Counter =  3
    Counter =  2
    Counter =  1


> The while loop structure just depicted is a "decrement, skip if equal" in lower level languages. The next structure, also a while loop is an "increment, skip if greater" structure.


```python
# set a counter
counter = 0
# while loop
while counter <= 5:  # change this line to: while counter <= 5: what happens?
    print ("Counter = ",counter)
    counter = counter +1  # change this line to: counter +=1  what happens?

```

    Counter =  0
    Counter =  1
    Counter =  2
    Counter =  3
    Counter =  4
    Counter =  5


___
### <font color=purple>Nested Repetition | Loops within Loops</font>
 
![](https://i.gifer.com/7kmF.gif) <br>



> Round like a circle in a spiral, like a wheel within a wheel <br>
Never ending or beginning on an ever spinning reel <br>
Like a snowball down a mountain, or a carnival balloon <br>
Like a carousel that's turning running rings around the moon <br>
Like a clock whose hands are sweeping past the minutes of its face <br>
And the world is like an apple whirling silently in space <br>
Like the circles that you find in the windmills of your mind! <br>
<br>
***Windmills of Your Mind lyrics © Sony/ATV Music Publishing LLC, BMG Rights Management*** <br>
***Songwriters: Marilyn Bergman / Michel Legrand / Alan Bergman*** <br>
***Recommended versions: Neil Diamond | Dusty Springfield | Farhad Mehrad***  <br>

"Like the circles that you find in the windmills of your mind", Nested repetition is when a control structure is placed inside of the body or main part of another control structure.

#### `break` to exit out of a loop

Sometimes you may want to exit the loop when a certain condition different from the counting
condition is met. Perhaps you are looping through a list and want to exit when you find the
first element in the list that matches some criterion. The break keyword is useful for such
an operation.
For example run the following program:


```python
#
j = 0
for i in range(0,5,1):
    j += 2
    print ("i = ",i,"j = ",j)
    if j == 6:
        break
```

    i =  0 j =  2
    i =  1 j =  4
    i =  2 j =  6



```python
# One Small Change
j = 0
for i in range(0,5,1):
    j += 2
    print( "i = ",i,"j = ",j)
    if j == 7:
        break
```

    i =  0 j =  2
    i =  1 j =  4
    i =  2 j =  6
    i =  3 j =  8
    i =  4 j =  10


In the first case, the for loop only executes 3 times before the condition j == 6 is TRUE and the loop is exited. 
In the second case, j == 7 never happens so the loop completes all its anticipated traverses.

In both cases an `if` statement was used within a for loop. Such "mixed" control structures
are quite common (and pretty necessary). 
A `while` loop contained within a `for` loop, with several `if` statements would be very common and such a structure is called __nested control.__
There is typically an upper limit to nesting but the limit is pretty large - easily in the
hundreds. It depends on the language and the system architecture ; suffice to say it is not
a practical limit except possibly for general-domain AI applications.
<hr>
We can also do mundane activities and leverage loops, arithmetic, and format codes to make useful tables like


### Example: Cosines in the loop! 

Write a loop to print a table of the cosines of numbers between 0 and 0.01 with steps of 0.001.


```python
import math # package that contains cosine
print("     Cosines     ")
print("   x   ","|"," cos(x) ")
print("--------|--------")
for i in range(0,100,1):
    x = float(i)*0.001
    print("%.3f" % x, "  |", " %.4f "  % math.cos(x)) # note the format code and the placeholder % and syntax of using package
```

___
### Example: Getting the hang of it! 

Write a Python script that takes a real input value (a float) for x and returns the y
value according to the rules below

\begin{gather}
y = x~for~0 <= x < 1 \\
y = x^2~for~1 <= x < 2 \\
y = x + 2~for~2 <= x < 3 \\
\end{gather}

Test the script with x values of 0.0, 1.0, 1.1, and 2.1. <br>
add functionality to **automaticaly** populate the table below:

|x|y(x)|
|---:|---:|
|0.0|  |
|1.0|  |
|2.0|  |
|3.0|  |
|4.0|  |
|5.0|  |


```python
userInput = input('Enter enter a float') #ask for user's input
x = float(userInput)
print("x:", x)

if x >= 0 and x < 1:
    y = x
    print("y is equal to",y)
elif x >= 1 and x < 2:
    y = x*x
    print("y is equal to",y)
else:
    y = x+2
    print("y is equal to",y)
```


```python
# without pretty table

print("---x---","|","---y---")
print("--------|--------")
for x in range(0,6,1):
    if x >= 0 and x < 1:
        y = x
        print("%4.f" % x, "   |", " %4.f " % y)
    elif x >= 1 and x < 2:
        y = x*x
        print("%4.f" % x, "   |", " %4.f " % y)
    else:
        y = x+2
        print("%4.f" % x, "   |", " %4.f " % y)
```


```python
# with pretty table

from prettytable import PrettyTable #Required to create tables

t = PrettyTable(['x', 'y']) #Define an empty table


for x in range(0,6,1):
    if x >= 0 and x < 1:
        y = x
        print("for x equal to", x, ", y is equal to",y)
        t.add_row([x, y]) #will add a row to the table "t"
    elif x >= 1 and x < 2:
        y = x*x
        print("for x equal to", x, ", y is equal to",y)
        t.add_row([x, y])
    else:
        y = x+2
        print("for x equal to", x, ", y is equal to",y)
        t.add_row([x, y])

print(t)
```

___
#### The `continue` statement
The continue instruction skips the block of code after it is executed for that iteration. 
It is
best illustrated by an example.


```python
j = 0
for i in range(0,5,1):
    j += 2
    print ("\n i = ", i , ", j = ", j) #here the \n is a newline command
    if j == 6:
        continue
    print(" this message will be skipped over if j = 6 ") # still within the loop, so the skip is implemented
    
#When j ==6 the line after the continue keyword is not printed. 
#Other than that one difference the rest of the script runs normally.
```

    
     i =  0 , j =  2
     this message will be skipped over if j = 6 
    
     i =  1 , j =  4
     this message will be skipped over if j = 6 
    
     i =  2 , j =  6
    
     i =  3 , j =  8
     this message will be skipped over if j = 6 
    
     i =  4 , j =  10
     this message will be skipped over if j = 6 


___
#### The `try`, `except` structure

An important control structure (and a pretty cool one for error trapping) is the `try`, `except`
statement.

The statement controls how the program proceeds when an error occurs in an instruction.
The structure is really useful to trap likely errors (divide by zero, wrong kind of input) 
yet let the program keep running or at least issue a meaningful message to the user.

The syntax is:

    try:
    do something
    except:
    do something else if ``do something'' returns an error

Here is a really simple, but hugely important example:


```python
#MyErrorTrap.py
x = 12.
y = 12.
while y >= -12.: # sentinel controlled repetition
    try:         
        print ("x = ", x, "y = ", y, "x/y = ", x/y)
    except:
        print ("error divide by zero")
    y -= 1
```

    x =  12.0 y =  12.0 x/y =  1.0
    x =  12.0 y =  11.0 x/y =  1.0909090909090908
    x =  12.0 y =  10.0 x/y =  1.2
    x =  12.0 y =  9.0 x/y =  1.3333333333333333
    x =  12.0 y =  8.0 x/y =  1.5
    x =  12.0 y =  7.0 x/y =  1.7142857142857142
    x =  12.0 y =  6.0 x/y =  2.0
    x =  12.0 y =  5.0 x/y =  2.4
    x =  12.0 y =  4.0 x/y =  3.0
    x =  12.0 y =  3.0 x/y =  4.0
    x =  12.0 y =  2.0 x/y =  6.0
    x =  12.0 y =  1.0 x/y =  12.0
    error divide by zero
    x =  12.0 y =  -1.0 x/y =  -12.0
    x =  12.0 y =  -2.0 x/y =  -6.0
    x =  12.0 y =  -3.0 x/y =  -4.0
    x =  12.0 y =  -4.0 x/y =  -3.0
    x =  12.0 y =  -5.0 x/y =  -2.4
    x =  12.0 y =  -6.0 x/y =  -2.0
    x =  12.0 y =  -7.0 x/y =  -1.7142857142857142
    x =  12.0 y =  -8.0 x/y =  -1.5
    x =  12.0 y =  -9.0 x/y =  -1.3333333333333333
    x =  12.0 y =  -10.0 x/y =  -1.2
    x =  12.0 y =  -11.0 x/y =  -1.0909090909090908
    x =  12.0 y =  -12.0 x/y =  -1.0


So this silly code starts with x fixed at a value of 12, and y starting at 12 and decreasing by
1 until y equals -1. The code returns the ratio of x to y and at one point y is equal to zero
and the division would be undefined. By trapping the error the code can issue us a measure
and keep running.

Modify the script as shown below,Run, and see what happens


```python
#NoErrorTrap.py
x = 12.
y = 12.
while y >= -12.: # sentinel controlled repetition
    print ("x = ", x, "y = ", y, "x/y = ", x/y)
    y -= 1
```

    x =  12.0 y =  12.0 x/y =  1.0
    x =  12.0 y =  11.0 x/y =  1.0909090909090908
    x =  12.0 y =  10.0 x/y =  1.2
    x =  12.0 y =  9.0 x/y =  1.3333333333333333
    x =  12.0 y =  8.0 x/y =  1.5
    x =  12.0 y =  7.0 x/y =  1.7142857142857142
    x =  12.0 y =  6.0 x/y =  2.0
    x =  12.0 y =  5.0 x/y =  2.4
    x =  12.0 y =  4.0 x/y =  3.0
    x =  12.0 y =  3.0 x/y =  4.0
    x =  12.0 y =  2.0 x/y =  6.0
    x =  12.0 y =  1.0 x/y =  12.0



    ---------------------------------------------------------------------------

    ZeroDivisionError                         Traceback (most recent call last)

    <ipython-input-31-82eeaceb9a12> in <module>
          3 y = 12.
          4 while y >= -12.: # sentinel controlled repetition
    ----> 5     print ("x = ", x, "y = ", y, "x/y = ", x/y)
          6     y -= 1


    ZeroDivisionError: float division by zero


___
![](https://media2.giphy.com/media/5nj4ZZWl6QwneEaBX4/source.gif) <br>


*Here are some great reads on this topic:* 
- __"Python for Loop"__ available at *https://www.programiz.com/python-programming/for-loop/<br>
- __"Python "for" Loops (Definite Iteration)"__ by __John Sturtz__ available at *https://realpython.com/python-for-loop/ <br>
- __"Python "while" Loops (Indefinite Iteration)"__ by __John Sturtz__ available at *https://realpython.com/python-while-loop/ <br>
- __"loops in python"__ available at *https://www.geeksforgeeks.org/loops-in-python/ <br>
- __"Python Exceptions: An Introduction"__ by __Said van de Klundert__ available at *https://realpython.com/python-exceptions/ <br>

*Here are some great videos on these topics:* 
- __"Python For Loops - Python Tutorial for Absolute Beginners"__ by __Programming with Mosh__ available at *https://www.youtube.com/watch?v=94UHCEmprCY <br>
- __"Python Tutorial for Beginners 7: Loops and Iterations - For/While Loops"__ by __Corey Schafer__ available at *https://www.youtube.com/watch?v=6iF8Xb7Z3wQ <br>
- __"Python 3 Programming Tutorial - For loop"__ by __sentdex__ available at *https://www.youtube.com/watch?v=xtXexPSfcZg <br><br>

![](https://media.csesoc.org.au/content/images/2019/10/learn11.gif) <br>
___


## Exercise: FOR or WHILE? <br>


### 1000 people have asked to be enlisted to take the first dose of COVID-19 vaccine. You are asked to write a loop and allow the ones who meet the requirements to take the shot. What kind of loop will you use? a FOR loop or a WHILE loop? Explain the logic behind your choice briefly. 

#### * Make sure to cite any resources that you may use. 


```python

```

![](https://i.pinimg.com/originals/51/97/7b/51977b7f744a0b085b593af84b0ec943.jpg)
