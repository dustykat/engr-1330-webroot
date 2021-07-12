# <font color=darkblue>Week 3 Assignment </font>

## Full name: 
## R#: 
## Title of the notebook:
## Date: 

![](https://campaignjr.com/v1/wp-content/uploads/2016/12/12_funny-and-inspiring-graphic-design-related-gifs.gif) <br>


___
### Question1: User-Defined Function 
Create the function $$f(x) = e^x - 10 cos(x) - 100$$ as a function (i.e. use the `def` keyword)

    def name(parameters) :
        operations on parameters
        ...
        ...
        return (value, or null)

Then apply your function to the value.

Use your function to complete the table below:

| x | f(x) |
|---:|---:|
| 0.0 | |
| 1.50 | |
| 2.00 | |
| 2.25 | |
| 3.0 | |
| 4.25 | |



```python
from math import exp # package that contains exp function
from math import cos # package that contains cosine function
def gollum(x) : #define the function "gollum"
    precious = exp(x) - 10*cos(x) -100  #as stated by the question
    return precious
```


```python
from prettytable import PrettyTable #package that contains the PrettyTable function 
t = PrettyTable(['x', 'y']) #Define an empty table

x = [0.0,1.5,2.0,2.25,3.0,4.25] #the list of x values according to the table
for i in range(0,6,1): #a counter to go through the list x
    t.add_row([x[i], gollum(x[i])]) #for each x value, fill one row in table t with the value of x and the value of gollum function of that x

print(t)
```

___
### Question2: Power Plot <br>

Copy the wrapper script for the `plotAline()` function (from the Lab4_dev notebook), and modify the copy to create a plot of
$$ y = x^2 $$
for x raging from 0 to 9 (inclusive) in steps of 1.

Label the plot and the plot axes.


```python
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
xxx = [] # null list
yyy = [] # null list
for i in range(0,10):
    xxx.append(1.0*i) #float i and append to the list
for i in range(0,10):
    yyy.append(xxx[i]**2)
plotAline(xxx,yyy,"X","Y","Plot of Y = X^2 ")
```


    
![png](output_8_0.png)
    


___
### Question3: Cars! <br>

Write a class named '**CarSpeed**' to calculate the speed (in miles/hour) of different brands of cars based on the information given in the table below.  
The formula to calculate speed is also given below.  
Based on your output, which brand of car has the highest speed?

$$Speed = \frac{Distance}{Time}$$

| Car brand   | Distance (miles) | Time (hours) |
| ----------- | -----------------|------------|
| Ford        | 120              | 1.75       |
| Ferrari     | 100              | 1.20       |
| BMW         | 205              | 2.35       |
| Porsche     | 155              | 1.85       |
| Audi        | 190              | 2.10       |
| Jaguar      | 255              | 2.45       |

##### Notes: 
1. Use docstrings to describe the purpose of the class.
2. Create an object for each car brand and display the output as shown below.

Ford_Speed (miles/hour): **SPEED**  
Ferrari_Speed (miles/hour): **SPEED**   
BMW_Speed (miles/hour): **SPEED**    
Porsche_Speed (miles/hour): **SPEED**   
Audi_Speed (miles/hour): **SPEED**  
Jaguar_Speed (miles/hour): **SPEED**  
The car with the highest speed is: **CAR BRAND**


```python
class CarSpeed:
    """This class calculates the speed of the car based on the given distance and time"""
    def __init__(self, distance, time):
        self.distance = distance
        self.time= time
        
    def speed(self):
        return self.distance/self.time
    
```


```python
ford = CarSpeed(120, 1.75)
ferrari = CarSpeed(100, 1.20)
bmw = CarSpeed(205, 2.35)
porsche = CarSpeed(155, 1.85)
audi = CarSpeed(190, 2.10)
jaguar = CarSpeed(255, 2.45)
```


```python
print("Ford_Speed (miles/hour):", ford.speed())
print("Ferrari_Speed (miles/hour):", ferrari.speed())
print("BMW_Speed (miles/hour):", bmw.speed())
print("Porsche_Speed (miles/hour):", porsche.speed())
print("Audi_Speed (miles/hour):", audi.speed())
print("Jaguar_Speed (miles/hour):", jaguar.speed())

```

    Ford_Speed (miles/hour): 68.57142857142857
    Ferrari_Speed (miles/hour): 83.33333333333334
    BMW_Speed (miles/hour): 87.23404255319149
    Porsche_Speed (miles/hour): 83.78378378378378
    Audi_Speed (miles/hour): 90.47619047619047
    Jaguar_Speed (miles/hour): 104.08163265306122



```python
# which brand of car has the highest speed?
BrSp = {"Ford":ford.speed(),"Ferrari":ferrari.speed(),"BMW":bmw.speed(),"Porsche":porsche.speed(),"Audi":audi.speed(),"Jaguar":jaguar.speed()} #Create a dictionary with brands and speeds
print(BrSp)
max_key = max(BrSp, key=BrSp.get) #Find the key(brand) associated with maximum speed
print("The brand of car with the highest speed is",max_key)
```

    {'Ford': 68.57142857142857, 'Ferrari': 83.33333333333334, 'BMW': 87.23404255319149, 'Porsche': 83.78378378378378, 'Audi': 90.47619047619047, 'Jaguar': 104.08163265306122}
    The brand of car with the highest speed is Jaguar


___
### Question4: RoboCop Modification  <br>

Write a class named '**Tax**' to calculate the state tax (in dollars) of Employees at Texas Tech University based on their annual salary.  
The state tax is 16% if the annual salary is below 80,000 dollars and 22% if the salary is more than 80,000 dollars. 

$$Tax = Annual salary \times State\, tax\, \%$$

| Employee    | Annual salary (dollars) | 
| ----------- | ------------------------|
| Bob         | 1,50,000                | 
| Mary        | 78,000                  | 
| John        | 55,000                  | 
| Danny       | 1,75,000                | 

#### Notes: 
1. Use docstrings to describe the purpose of the class.
2. Use if....else conditional statements within the method of the class to choose the relevant tax % based on the annual salary.
3. Create an object for employee and display the output as shown below.

Bob's tax amount (in dollars): **AMOUNT**  
Mary's tax amount (in dollars): **AMOUNT**  
John's tax amount (in dollars): **AMOUNT**  
Danny's tax amount (in dollars): **AMOUNT** 




```python
class Tax:
    """This class calculates the tax amount based on the annual salary and the state tax %"""
    def __init__(self, salary):
        self.salary = salary
        
    def taxamount(self):
        if self.salary < 80000:
            return self.salary*(16/100)
        else: 
            return self.salary*(22/100)
    
bob = Tax(150000)
mary = Tax(78000)
john = Tax(55000)
danny = Tax(175000)

print("Bob's tax amount (in dollars):", bob.taxamount())  
print("Mary's tax amount (in dollars):", mary.taxamount())  
print("John's tax amount (in dollars):", john.taxamount())  
print("Danny's tax amount (in dollars):", danny.taxamount())
```

    Bob's tax amount (in dollars): 33000.0
    Mary's tax amount (in dollars): 12480.0
    John's tax amount (in dollars): 8800.0
    Danny's tax amount (in dollars): 38500.0


![](https://freight.cargo.site/w/1200/i/c96b2ce17b2aee95c6e837552e3e38d058ac4ad2a6759448ed78128963790744/Happy_Coding_BC_6-03-05.png)


```python

```
