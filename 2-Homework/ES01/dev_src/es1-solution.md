# <font color=darkblue>Week 1 Assignment </font>



## Full name: 
## R#: 
## Title of the notebook:
## Date: 

![](https://miro.medium.com/max/1600/1*qdAW1TjCN57h1lbuuzvchg.gif) <br>


## Question1: Playing with a Markdown cell <br>


### Use the empty Markdown cell below, set it up so that it meets all the mentioned requirements:

"O Captain! my Captain! our fearful trip is done,
The ship has weather’d every rack, the prize we sought is won,
The port is near, the bells I hear, the people all exulting,
While follow eyes the steady keel, the vessel grim and daring;"
<br> <font color=red>[Have this verse in blue and italic]</font><br>

But O heart! heart! heart!
O the bleeding drops of red,
Where on the deck my Captain lies,
Fallen cold and dead.
<br> <font color=red>[Have this verse as indented quoting]</font><br>


O Captain! my Captain! rise up and hear the bells;
Rise up—for you the flag is flung—for you the bugle trills,
For you bouquets and ribbon’d wreaths—for you the shores a-crowding,
For you they call, the swaying mass, their eager faces turning;
<br> <font color=red>[Have this verse in pink and bold]</font><br>

Here Captain! dear father!
This arm beneath your head!
It is some dream that on the deck,
You’ve fallen cold and dead.
<br> <font color=red>[Have this verse as indented quoting]</font><br>

My Captain does not answer, his lips are pale and still,
My father does not feel my arm, he has no pulse nor will,
The ship is anchor’d safe and sound, its voyage closed and done,
From fearful trip the victor ship comes in with object won;
<br> <font color=red>[Have this verse in orange, italic and bold]</font><br>

Exult O shores, and ring O bells!
But I with mournful tread,
Walk the deck my Captain lies,
Fallen cold and dead."
<br> <font color=red>[Have this verse as indented quoting]</font><br>


<br> <font color=red>[Attach an image of WALT WHITMAN from an online resource here.]</font><br>


---

_<font color=blue> "O Captain! my Captain! our fearful trip is done,</font>_<br>
_<font color=blue>The ship has weather’d every rack, the prize we sought is won,</font>_<br>
_<font color=blue>The port is near, the bells I hear, the people all exulting,</font>_<br>
_<font color=blue>While follow eyes the steady keel, the vessel grim and daring;"</font>_<br>

>But O heart! heart! heart!
O the bleeding drops of red,
Where on the deck my Captain lies,
Fallen cold and dead.
<br> 


__<font color=pink>O Captain! my Captain! rise up and hear the bells;</font>__<br>
__<font color=pink>Rise up—for you the flag is flung—for you the bugle trills,</font>__<br>
__<font color=pink>For you bouquets and ribbon’d wreaths—for you the shores a-crowding,</font>__<br>
__<font color=pink>For you they call, the swaying mass, their eager faces turning;</font>__<br>

> Here Captain! dear father!
This arm beneath your head!
It is some dream that on the deck,
You’ve fallen cold and dead.
<br>

___<font color=orange>My Captain does not answer, his lips are pale and still,</font>___<br>
___<font color=orange>My father does not feel my arm, he has no pulse nor will,</font>___<br>
___<font color=orange>The ship is anchor’d safe and sound, its voyage closed and done,</font>___<br>
___<font color=orange>From fearful trip the victor ship comes in with object won;</font>___<br>


> Exult O shores, and ring O bells!
But I with mournful tread,
Walk the deck my Captain lies,
Fallen cold and dead."
<br> 

![](https://www.pbs.org/wgbh/americanexperience/media/canonical_images/film/Walt_Whitman_2800x1576.jpg) <br>


---

## Question2: To quote or not to quote! <br>


### Change the cell below to a code cell and run the script:


```python
print(3 + 7 )
print('3 + 7')
MyNumber = 3+7
MyName = 'Dusty'
print(MyName, MyNumber)
print('MyName', 'MyNumber')
MyNumber = 3+2.0
print(MyNumber)

```

    10
    3 + 7
    Dusty 10
    MyName MyNumber
    5.0


### Answer the following questions based on the output

1.  What is the difference between `print( 3 + 7 )` and `print( '3 + 7')`?

2.  What is the difference between `print( MyName, MyNumber)` and `print('MyName', 'MyNumber')`

3.  Change `MyNumber = 3+2` to `MyNumber = 3+2.0`, and re-run the script, what happens? Why?

Write your answers below:

> Answer1: print( 3 + 7 ) returns the output of the summation of 3 and 7 which is equal to 10. print( '3 + 7' ) prints the string between quotation marks as is. 

> Answer2: print( MyName, MyNumber) returns the content of "MyName" and "MyNumber" variables. But print( 'MyName', 'MyNumber') prints merely those strings. 

> Answer3: After modifying the script, "MyNumber" is now updated to 5.0 which is a float. This is because we summed up an integer (3) and a float (2.0) which will always result in a float (5.0)

## Question3: Arithmetic and Expressions <br>


### Calculate the expressions below by hand taking care to keep track of result type (integer or float):



    x1 = 7 + 3 * 6 / 2 - 1
    
    x2 = 2 % 2 + 2 * 2 - 2 / 2
    
    x3 = ( 3 * 9 * ( 3 + ( 9 * 3 / ( 3 ) ) ) )

### Write your results below

x1 (by hand) = 15

x2 (by hand) = 3

x3 (by hand) = 324

### Now write a script to evaluate and print the results, by

1. Assigning a value to a variable.  Use the names above

        x1 = 7 + 3 * 6 / 2 - 1
        x2 = ...
        x3 = ...
    
2. Then print the type and contents of each variable.

        print(type(x1),x1) 
        print(type(x2),x2)
        ...


```python
x1 = 7 + 3 * 6 / 2 - 1   
x2 = 2 % 2 + 2 * 2 - 2 / 2
x3 = ( 3 * 9 * ( 3 + ( 9 * 3 / ( 3 ) ) ) )
print(type(x1),x1) 
print(type(x2),x2)
print(type(x3),x3)
```

    <class 'float'> 15.0
    <class 'float'> 3.0
    <class 'float'> 324.0


## Question4: String Element Manipulation  <br>


### Define the string given below in quotes to a meaningful variable name.

    some_string ='Computational Thinking'

### Then

1. Index and print all the elements from index positions 2 to 10.

        begin = ???
        end = ???
        print(some_string[begin:end])
        
  
2. Index and print the string 'Think'.




```python
Q4string ='Computational Thinking' #Defining the given string
```


```python
print(Q4string[2:10])  #Indexing with [#first index:#last index] syntax and printing
```

    mputatio



```python
print(Q4string[14:19]) #Indexing so that we can get "Think"
```

    Think


![](https://freight.cargo.site/w/1200/i/c96b2ce17b2aee95c6e837552e3e38d058ac4ad2a6759448ed78128963790744/Happy_Coding_BC_6-03-05.png)
