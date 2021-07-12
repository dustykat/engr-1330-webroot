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

```

___
### Question2: Dictionary Manipulation <br>

From the nested dictionary given below, index and pick the string 'hello'. 

**{'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}**


```python

```

### Question3: Use of Conditional Execution <br>

A student will not be allowed to sit in exam if his/her attendence is less than 75%. 
Take the following inputs from the user: 

    1. Number of classes held.
    2. Number of classes attended. 
   
Compute the percentage of classes attended 

$$\%_{attended} = \frac{Classes_{attended}}{Classes_{total}}*100$$

Use the result to decide whether the student will be allowed to sit in the exam or not.


```python

```

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
    print('Fine = $500')
elif alterspeed > 60:   
    print('Fine = $100')
else:
    print('No Ticket')
```


```python

```

### Question5: A Loop for Leaps!  <br>

1904 was a leap year. Write a for loop that prints out all the leap years from in the 20th century (1904-1999).  


```python

```

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

```

![](https://www.codester.com/static/uploads/items/000/021/21656/preview.jpg)
