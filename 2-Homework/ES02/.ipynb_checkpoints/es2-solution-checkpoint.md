# <font color=darkblue>Week 2 Assignment </font>



## Full name: 
## R#: 
## Title of the notebook:
## Date: 

![](https://media.tenor.com/images/dc545e5a0f93c9b2bf1d4f0af54ebbff/tenor.gif) <br>


### Question1: List Manipulation

For the list given below, index and pick all the elements from index positions 3 to 10. 
Then, calculate the sum and the length of the elements from index positions 3 to 7. 
Print the sliced list and the values of the sum and the sliced list.

**[22, 45, 54, 87, 10, 97, 88, 75, 99, 11, 19, 39, 47, 81, 84]**


```python
mylist2 = [22, 45, 54, 87, 10, 97, 88, 75, 99, 11, 19, 39, 47, 81, 84] #Make the given list
print(mylist2) #print it

myslicelist2 = mylist2[3:11] #index and pick all elements from 3 to 10 | including 10
print("Sliced_list: ", myslicelist2) #print it

mysubslice2 = myslicelist2[3:8] #slice the elements 3 to 7 | including 7
print(mysubslice2) #print it
mysum = sum(mysubslice2) #calculate the sum
print("Sum: ", mysum) #print it

mylength = len(mysubslice2) #calculate the length
print("Length: ", mylength) #print it
```

    [22, 45, 54, 87, 10, 97, 88, 75, 99, 11, 19, 39, 47, 81, 84]
    Sliced_list:  [87, 10, 97, 88, 75, 99, 11, 19]
    [88, 75, 99, 11, 19]
    Sum:  292
    Length:  5


___
### Question2: Dictionary Manipulation <br>

From the nested dictionary given below, index and pick the string 'hello'. 

**{'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}**


```python
Q2dict = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
Q2dict['k1'][3]['tricky'][3]['target'][3]
```




    'hello'



### Question3: Use of Conditional Execution <br>

A student will not be allowed to sit in exam if his/her attendence is less than 75%. 
Take the following inputs from the user: 

    1. Number of classes held.
    2. Number of classes attended. 
   
Compute the percentage of classes attended 

$$\%_{attended} = \frac{Classes_{attended}}{Classes_{total}}*100$$

Use the result to decide whether the student will be allowed to sit in the exam or not.


```python
nc_held = input('Enter total classes held')              #Ask user for Number of classes held
nc_attended = input('Enter classes attended')            # Ask user for Number of classes attended
attendance = int(nc_attended)/int(nc_held)*100           #Calculate the %attended based on the given formula
print('Attendance:', attendance,' percent')              #print the calculated value

if attendance >= 75:                                     #Print the decision on whether the student will be allowed to sit in the exam or not
    print("Allowed to sit in exam")
else:
    print("Not allowed to sit in exam")
```

    Enter total classes held 100
    Enter classes attended 64


    Attendance: 64.0  percent
    Not allowed to sit in exam


### Question4: RoboCop Modification  <br>

You are driving too fast, and a robotic police officer stops you. 
The robot is programmed with conditional statements to return one of 3 possible results: 
"No ticket","One hundred dollar fine", or "Five hundred dollar fine". according to the following rules

* If your speed is 60 or less, the result is "No Ticket". 
* If speed is between 61 and 80 inclusive, the result is a fine of \$100. 
* If speed is 81 or more, the result is \$500. 
* If it is your birthday, your speed can be higher by a value of 5 in all cases.

You discover you are able to hack into the robot and can modify the fine script.

Modify it so that:

* If speed is between 75 and 85 inclusive, the result is a fine of \$100.
* If speed is 86 or more, the result is \$500. 

Leave the rest unchanged.




```python
# Original Script
# Input Speed
speed = int(input('How Fast ? (numeric)'))
# Input Birthday
yes = 0
# while loop 
while yes == 0:
    userInput = input('Is it your birthday?  (Yes or No)')
    try:
        if userInput == 'Yes':
            is_birthday = True
        elif userInput == 'No':
            is_birthday = False
        yes = 1
    except:
        print ("You did not enter Yes or No, try again \n")
# Exit the while loop when finally have a valid answer

if is_birthday:
    alterspeed = speed-5
else:
    alterspeed = speed
    
if alterspeed > 80:    
    print('Fine = $100')
elif alterspeed > 60:   
    print('Fine = $100')
else:
    print('No Ticket')
```

    How Fast ? (numeric) 76
    Is it your birthday?  (Yes or No) No


    Fine = $100



```python
# Input Speed
speed = int(input('How Fast ? (numeric)'))
# Input Birthday
yes = 0
# while loop 
while yes == 0:
    userInput = input('Is it your birthday?  (Yes or No)')
    try:
        if userInput == 'Yes':
            is_birthday = True
        elif userInput == 'No':
            is_birthday = False
        yes = 1
    except:
        print ("You did not enter Yes or No, try again \n")
# Exit the while loop when finally have a valid answer

if is_birthday:
    alterspeed = speed-5
else:
    alterspeed = speed
    
if alterspeed > 85:              #Change this | the upper bound
    print('Fine = $500')
elif alterspeed > 74:            #Change this | the lower bound
    print('Fine = $100')
else:
    print('No Ticket')
```

    How Fast ? (numeric) 86
    Is it your birthday?  (Yes or No) No


    Fine = $500


### Question5: A Loop for Leaps!  <br>

1904 was a leap year. Write a for loop that prints out all the leap years from in the 20th century (1904-1999).  


```python
for years in range(1904,2000,4): # a sequence from 1904 to 1999 with steps of 4
  print(years)
```

    1904
    1908
    1912
    1916
    1920
    1924
    1928
    1932
    1936
    1940
    1944
    1948
    1952
    1956
    1960
    1964
    1968
    1972
    1976
    1980
    1984
    1988
    1992
    1996


### Question6: Trapped!  <br>

Write a script that:
- asks user for 3 inputs
    - a starting value for $x$
    - an ending value for $x$
    - a stepsize
- creates and prints a sequence based on user's 3 numbers
- calculates the value of $y$ for each number in the defined sequence based on the rules below

> \begin{gather}
y = x~for~0 <= x < 1 \\
y = x^3~for~1 <= x < 2 \\
y = x + 2~for~2 <= x  \\
\end{gather}

- produces a table like this:

|x|y(x)|
|---:|---:|
|0.0|  |
|1.0|  |
|2.0|  |
|3.0|  |
|4.0|  |
|5.0|  |

*the increment can be different from 1.0 (unlike above).

**Include error trapping that:

1. Takes any numeric input for starting or ending $x$, and forces into a float.
2. Takes any numeric input for stepsize. and forces into an integer.
3. Takes any non-numeric input, issues a message that the input needs to be numeric, and makes the user try again.



Test your script with the following inputs for x, x_increment, num_steps

    Case 1) fred , 0.5, 7
    
    Case 2) 0.0, 0.5, 7
      
    Case 3) -3.0, 0.5, 14


```python
from prettytable import PrettyTable

try:
    userInput = input('Enter the starting value for x') #ask for user's input on the initial value
    start = float(userInput)
    userInput2 = input('Enter the ending value for x') #ask for user's input on the last value
    stop = float(userInput2)
    userInput3 = float(input('Enter the step size for x')) #ask for user's input on the step size
    step = int(userInput3)

    print("the range for x goes from", start, " to", stop, " by increments of", step)
    t = PrettyTable(['x', 'y'])
    for x in range(int(start),int(stop),int(step)):
        if x >= 0 and x < 1:
            y = x
            print("for x equal to", x, ", y is equal to",y)
            t.add_row([x, y])
        elif x >= 1 and x < 2:
            y = x*x*x
            print("for x equal to", x, ", y is equal to",y)
            t.add_row([x, y])
        else:
            y = x+2
            print("for x equal to", x, ", y is equal to",y)
            t.add_row([x, y])
    print(t)
except:
    print ("the input needs to be numeric. Please try again!")

```

    Enter the starting value for x 0
    Enter the ending value for x 6
    Enter the step size for x 1


    the range for x goes from 0.0  to 6.0  by increments of 1
    for x equal to 0 , y is equal to 0
    for x equal to 1 , y is equal to 1
    for x equal to 2 , y is equal to 4
    for x equal to 3 , y is equal to 5
    for x equal to 4 , y is equal to 6
    for x equal to 5 , y is equal to 7
    +---+---+
    | x | y |
    +---+---+
    | 0 | 0 |
    | 1 | 1 |
    | 2 | 4 |
    | 3 | 5 |
    | 4 | 6 |
    | 5 | 7 |
    +---+---+


![](https://www.codester.com/static/uploads/items/000/021/21656/preview.jpg)
