**Download** (right-click, save target as ...) this page as a jupyterlab notebook from: (LINK NEEDS FIXING!)

[Lab14](https://atomickitty.ddns.net:8000/user/sensei/files/engr-1330-webroot/engr-1330-webbook/ctds-psuedocourse/docs/8-Labs/Lab8/Lab9_Dev.ipynb?_xsrf=2%7C1b4d47c3%7C0c3aca0c53606a3f4b71c448b09296ae%7C1623531240)

___

# <font color=darkred>Laboratory 14: "A Bullet or A Goat?" or "Things you should know before playing with strangers!"</font>


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

# <font color=purple>Python for Simulation</font>

## What is Russian roulette?
>Russian roulette (Russian: русская рулетка, russkaya ruletka) is a lethal game of chance in which a player places a single round in a revolver, spins the cylinder, places the muzzle against their head, and pulls the trigger in hopes that the loaded chamber does not align with the primer percussion mechanism and the barrel, causing the weapon to discharge. Russian refers to the supposed country of origin, and roulette to the element of risk-taking and the spinning of the revolver's cylinder, which is reminiscent of a spinning roulette wheel. <br>
- Wikipedia @ https://en.wikipedia.org/wiki/Russian_roulette

![](https://images.fineartamerica.com/images/artworkimages/mediumlarge/1/echoes-of-the-great-war-the-revolver-weston-westmoreland.jpg)

>A game of dafts, a game of chance <br>
One where revolver's the one to dance <br>
Rounds and rounds, it goes and spins <br>
Makes you regret all those sins <br> \
A game of fools, one of lethality  <br>
With a one to six probability <br>
There were two guys and a gun <br>
With six chambers but only one... <br> \
CLICK, one pushed the gun <br>
CLICK, one missed the fun <br>
CLICK, "that awful sound" ... <br>
BANG!, one had his brains all around! <br>

___
### Example: Simulate a game of Russian Roulette:
- For 2 rounds
- For 5 rounds
- For 10 rounds


```python
import numpy as np                     #import numpy
revolver = np.array([1,0,0,0,0,0])     #create a numpy array with 1 bullet and 5 empty chambers
print(np.random.choice(revolver,2))              #randomly select a value from revolver - simulation
```

    [0 0]
    


```python
print(np.random.choice(revolver,5))
```

    [0 0 1 0 0]
    


```python
print(np.random.choice(revolver,10))
```

    [0 0 0 1 0 0 0 0 0 0]
    

![](https://blog.uvm.edu/aivakhiv/files/2020/06/d4cawex-fd18072b-6140-48d9-93d7-0fa9435abf0e.png)

___
### Example: Simulate the results of throwing a D6 (regular dice) for 10 times. 


```python
import numpy as np                     #import numpy
dice = np.array([1,2,3,4,5,6])         #create a numpy array with values of a D6
np.random.choice(dice,10)              #randomly selecting a value from dice for 10 times- simulation
```




    array([5, 6, 5, 5, 1, 4, 6, 6, 3, 4])



___
### Example: Assume the following rules:

- If the dice shows 1 or 2 spots, my net gain is -1 dollar.

- If the dice shows 3 or 4 spots, my net gain is 0 dollars.

- If the dice shows 5 or 6 spots, my net gain is 1 dollar.

__Define a function to simulate a game with the above rules, assuming a D6, and compute the net gain of the player over any given number of rolls. <br>
Compute the net gain for 5, 50, and 500 rolls__


```python
def D6game(nrolls):
    import numpy as np                     #import numpy
    dice = np.array([1,2,3,4,5,6])         #create a numpy array with values of a D6
    rolls = np.random.choice(dice,nrolls)  #randomly selecting a value from dice for nrolls times- simulation
    gainlist =[]                           #create an empty list for gains|losses
    for i in np.arange(len(rolls)):        #Apply the rules 
        if rolls[i]<=2:
            gainlist.append(-1)
        elif rolls[i]<=4:
            gainlist.append(0)
        elif rolls[i]<=6:
            gainlist.append(+1)
    return (np.sum(gainlist))              #sum up all gains|losses
#   return (gainlist,"The net gain is equal to:",np.sum(gainlist))

```


```python
D6game(5)
```




    2




```python
D6game(50)
```




    -4




```python
D6game(500)
```




    0



![](https://www.gannett-cdn.com/media/2017/09/30/USATODAY/USATODAY/636423937425139027-XXX-D4-MONTY-HALL-27-TV.jpg?width=2560)

### Let's Make A Deal Game Show and Monty Hall Problem 
__The Monty Hall problem is a brain teaser, in the form of a probability puzzle, loosely based on the American television game show Let's Make a Deal and named after its original host, Monty Hall. The problem was originally posed (and solved) in a letter by Steve Selvin to the American Statistician in 1975 (Selvin 1975a), (Selvin 1975b).__

>"Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others, goats. You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat. He then says to you, "Do you want to pick door No. 2?" Is it to your advantage to switch your choice?"

__*From Wikipedia: https://en.wikipedia.org/wiki/Monty_Hall_problem*__

![](https://thumbs.gfycat.com/ClearcutFragrantArcherfish-size_restricted.gif)

![](http://www.bcmath.ca/m10h/The%20Monty%20Hall%20Problem%20(Web)/data/img1.png)

![](https://webstockreview.net/images/clipart-door-orange-door-3.png)

![](https://brilliant-staff-media.s3-us-west-2.amazonaws.com/tiffany-wang/UcEdvPuGYw.png)

___
### Example: Simulate Monty Hall Game for 1000 times. Use a barplot and discuss whether players are better off sticking to their initial choice, or switching doors? 


```python
def othergoat(x):         #Define a function to return "the other goat"!
    if x == "Goat 1":
        return "Goat 2"
    elif x == "Goat 2":
        return "Goat 1"
```


```python
Doors = np.array(["Car","Goat 1","Goat 2"])     #Define a list for objects behind the doors
goats = np.array(["Goat 1" , "Goat 2"])          #Define a list for goats!

def MHgame():
    #Function to simulate the Monty Hall Game
    #For each guess, return ["the guess","the revealed", "the remaining"]
    userguess=np.random.choice(Doors)         #randomly selects a door as userguess
    if userguess == "Goat 1":
        return [userguess, "Goat 2","Car"]
    if userguess == "Goat 2":
        return [userguess, "Goat 1","Car"]
    if userguess == "Car":
        revealed = np.random.choice(goats)
        return [userguess, revealed,othergoat(revealed)]
```


```python
# Check and see if the MHgame function is doing what it is supposed to do:
for i in np.arange(1):
    a =MHgame()
    print(a)
    print(a[0])
    print(a[1])
    print(a[2])
```

    ['Goat 2', 'Goat 1', 'Car']
    Goat 2
    Goat 1
    Car
    


```python
c1 = []         #Create an empty list for the userguess
c2 = []         #Create an empty list for the revealed
c3 = []         #Create an empty list for the remaining
for i in np.arange(1000):         #Simulate the game for 1000 rounds - or any other number of rounds you desire
    game = MHgame()
    c1.append(game[0])             #In each round, add the first element to the userguess list
    c2.append(game[1])             #In each round, add the second element to the revealed list
    c3.append(game[2])             #In each round, add the third element to the remaining list

```


```python
import pandas as pd
#Create a data frame (gamedf) with 3 columns ("Guess","Revealed", "Remaining") and 1000 (or how many number of rounds) rows
gamedf = pd.DataFrame({'Guess':c1,
                       'Revealed':c2,
                       'Remaining':c3})
gamedf
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
      <th>Guess</th>
      <th>Revealed</th>
      <th>Remaining</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>Car</td>
      <td>Goat 2</td>
      <td>Goat 1</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Car</td>
      <td>Goat 2</td>
      <td>Goat 1</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Goat 1</td>
      <td>Goat 2</td>
      <td>Car</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Car</td>
      <td>Goat 2</td>
      <td>Goat 1</td>
    </tr>
    <tr>
      <td>4</td>
      <td>Goat 2</td>
      <td>Goat 1</td>
      <td>Car</td>
    </tr>
    <tr>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <td>995</td>
      <td>Goat 1</td>
      <td>Goat 2</td>
      <td>Car</td>
    </tr>
    <tr>
      <td>996</td>
      <td>Goat 1</td>
      <td>Goat 2</td>
      <td>Car</td>
    </tr>
    <tr>
      <td>997</td>
      <td>Car</td>
      <td>Goat 1</td>
      <td>Goat 2</td>
    </tr>
    <tr>
      <td>998</td>
      <td>Car</td>
      <td>Goat 1</td>
      <td>Goat 2</td>
    </tr>
    <tr>
      <td>999</td>
      <td>Goat 1</td>
      <td>Goat 2</td>
      <td>Car</td>
    </tr>
  </tbody>
</table>
<p>1000 rows × 3 columns</p>
</div>




```python
# Get the count of each item in the first and 3rd column
original_car =gamedf[gamedf.Guess == 'Car'].shape[0]
remaining_car =gamedf[gamedf.Remaining == 'Car'].shape[0]

original_g1 =gamedf[gamedf.Guess == 'Goat 1'].shape[0]
remaining_g1 =gamedf[gamedf.Remaining == 'Goat 1'].shape[0]

original_g2 =gamedf[gamedf.Guess == 'Goat 2'].shape[0]
remaining_g2 =gamedf[gamedf.Remaining == 'Goat 2'].shape[0]
```


```python
# Let's plot a grouped barplot
import matplotlib.pyplot as plt  

# set width of bar
barWidth = 0.25
 
# set height of bar
bars1 = [original_car,original_g1,original_g2]
bars2 = [remaining_car,remaining_g1,remaining_g2]
 
# Set position of bar on X axis
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
 
# Make the plot
plt.bar(r1, bars1, color='darkorange', width=barWidth, edgecolor='white', label='Original Guess')
plt.bar(r2, bars2, color='midnightblue', width=barWidth, edgecolor='white', label='Remaining Door')
 
# Add xticks on the middle of the group bars
plt.xlabel('Item', fontweight='bold')
plt.xticks([r + barWidth/2 for r in range(len(bars1))], ['Car', 'Goat 1', 'Goat 2'])
 
# Create legend & Show graphic
plt.legend()
plt.show()

```


![png](output_33_0.png)


<font color=crimson>__According to the plot, it is statitically beneficial for the players to switch doors because the initial chance for being correct is only 1/3__</font>

![](http://imgs.xkcd.com/comics/monty_hall.png)

# <font color=purple>Python for Probability</font>

![](https://static.insider.com/image/5d08059fdaa48259d13213a5.jpg)

### <font color=purple>Important Terminology:</font>
 
__Experiment:__ An occurrence with an uncertain outcome that we can observe. <br>
*For example, rolling a die.*<br>
__Outcome:__ The result of an experiment; one particular state of the world. What Laplace calls a "case."<br>
*For example: 4.*<br>
__Sample Space:__ The set of all possible outcomes for the experiment.<br>
*For example, {1, 2, 3, 4, 5, 6}.*<br>
__Event:__ A subset of possible outcomes that together have some property we are interested in.<br>
*For example, the event "even die roll" is the set of outcomes {2, 4, 6}.*<br>
__Probability:__ As Laplace said, the probability of an event with respect to a sample space is the number of favorable cases (outcomes from the sample space that are in the event) divided by the total number of cases in the sample space. (This assumes that all outcomes in the sample space are equally likely.) Since it is a ratio, probability will always be a number between 0 (representing an impossible event) and 1 (representing a certain event).<br>
*For example, the probability of an even die roll is 3/6 = 1/2.*<br>

__*From https://people.math.ethz.ch/~jteichma/probability.html*__


```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt  
```

___
### Example: In a game of Russian Roulette, the chance of surviving each round is 5/6 which is almost 83%. Using a for loop, compute probability of surviving 
- For 2 rounds
- For 5 rounds
- For 10 rounds


```python
nrounds =[]
probs =[]

for i in range(3):
    nrounds.append(i)
    probs.append((5/6)**i) #probability of surviving- not getting the bullet!

RRDF = pd.DataFrame({"# of Rounds": nrounds, "Probability of Surviving": probs})
RRDF
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
      <th># of Rounds</th>
      <th>Probability of Surviving</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>0</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <td>1</td>
      <td>1</td>
      <td>0.833333</td>
    </tr>
    <tr>
      <td>2</td>
      <td>2</td>
      <td>0.694444</td>
    </tr>
  </tbody>
</table>
</div>




```python
nrounds =[]
probs =[]

for i in range(6):
    nrounds.append(i)
    probs.append((5/6)**i) #probability of surviving- not getting the bullet!

RRDF = pd.DataFrame({"# of Rounds": nrounds, "Probability of Surviving": probs})
RRDF
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
      <th># of Rounds</th>
      <th>Probability of Surviving</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>0</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <td>1</td>
      <td>1</td>
      <td>0.833333</td>
    </tr>
    <tr>
      <td>2</td>
      <td>2</td>
      <td>0.694444</td>
    </tr>
    <tr>
      <td>3</td>
      <td>3</td>
      <td>0.578704</td>
    </tr>
    <tr>
      <td>4</td>
      <td>4</td>
      <td>0.482253</td>
    </tr>
    <tr>
      <td>5</td>
      <td>5</td>
      <td>0.401878</td>
    </tr>
  </tbody>
</table>
</div>




```python
nrounds =[]
probs =[]

for i in range(11):
    nrounds.append(i)
    probs.append((5/6)**i) #probability of surviving- not getting the bullet!

RRDF = pd.DataFrame({"# of Rounds": nrounds, "Probability of Surviving": probs})
RRDF
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
      <th># of Rounds</th>
      <th>Probability of Surviving</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>0</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <td>1</td>
      <td>1</td>
      <td>0.833333</td>
    </tr>
    <tr>
      <td>2</td>
      <td>2</td>
      <td>0.694444</td>
    </tr>
    <tr>
      <td>3</td>
      <td>3</td>
      <td>0.578704</td>
    </tr>
    <tr>
      <td>4</td>
      <td>4</td>
      <td>0.482253</td>
    </tr>
    <tr>
      <td>5</td>
      <td>5</td>
      <td>0.401878</td>
    </tr>
    <tr>
      <td>6</td>
      <td>6</td>
      <td>0.334898</td>
    </tr>
    <tr>
      <td>7</td>
      <td>7</td>
      <td>0.279082</td>
    </tr>
    <tr>
      <td>8</td>
      <td>8</td>
      <td>0.232568</td>
    </tr>
    <tr>
      <td>9</td>
      <td>9</td>
      <td>0.193807</td>
    </tr>
    <tr>
      <td>10</td>
      <td>10</td>
      <td>0.161506</td>
    </tr>
  </tbody>
</table>
</div>




```python
RRDF.plot.scatter(x="# of Rounds", y="Probability of Surviving",color="red")
```




    <matplotlib.axes._subplots.AxesSubplot at 0x2c7f96de308>




![png](output_44_1.png)


___
### Example: What will be the probability of constantly throwing an even number with a D20 in
- For 2 rolls
- For 5 rolls
- For 10 rolls
- For 15 rolls


```python
nrolls =[]
probs =[]

for i in range(1,16,1):
    nrolls.append(i)
    probs.append((1/2)**i) #probability of throwing an even number-10/20 or 1/2

DRDF = pd.DataFrame({"# of Rolls": nrolls, "Probability of constantly throwing an even number": probs})
DRDF
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
      <th># of Rolls</th>
      <th>Probability of constantly throwing an even number</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>1</td>
      <td>0.500000</td>
    </tr>
    <tr>
      <td>1</td>
      <td>2</td>
      <td>0.250000</td>
    </tr>
    <tr>
      <td>2</td>
      <td>3</td>
      <td>0.125000</td>
    </tr>
    <tr>
      <td>3</td>
      <td>4</td>
      <td>0.062500</td>
    </tr>
    <tr>
      <td>4</td>
      <td>5</td>
      <td>0.031250</td>
    </tr>
    <tr>
      <td>5</td>
      <td>6</td>
      <td>0.015625</td>
    </tr>
    <tr>
      <td>6</td>
      <td>7</td>
      <td>0.007812</td>
    </tr>
    <tr>
      <td>7</td>
      <td>8</td>
      <td>0.003906</td>
    </tr>
    <tr>
      <td>8</td>
      <td>9</td>
      <td>0.001953</td>
    </tr>
    <tr>
      <td>9</td>
      <td>10</td>
      <td>0.000977</td>
    </tr>
    <tr>
      <td>10</td>
      <td>11</td>
      <td>0.000488</td>
    </tr>
    <tr>
      <td>11</td>
      <td>12</td>
      <td>0.000244</td>
    </tr>
    <tr>
      <td>12</td>
      <td>13</td>
      <td>0.000122</td>
    </tr>
    <tr>
      <td>13</td>
      <td>14</td>
      <td>0.000061</td>
    </tr>
    <tr>
      <td>14</td>
      <td>15</td>
      <td>0.000031</td>
    </tr>
  </tbody>
</table>
</div>




```python
DRDF.plot.scatter(x="# of Rolls", y="Probability of constantly throwing an even number",color="crimson")
```




    <matplotlib.axes._subplots.AxesSubplot at 0x2c7f978f488>




![png](output_47_1.png)


___
### Example: What will be the probability of throwing at least one 6 with a D6:
- For 2 rolls
- For 5 rolls
- For 10 rolls
- For 50 rolls - Make a scatter plot for this one!


```python
nRolls =[]
probs =[]

for i in range(1,3,1):
    nRolls.append(i)
    probs.append(1-(5/6)**i) #probability of at least one 6: 1-(5/6)

rollsDF = pd.DataFrame({"# of Rolls": nRolls, "Probability of rolling at least one 6": probs})
rollsDF
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
      <th># of Rolls</th>
      <th>Probability of rolling at least one 6</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>1</td>
      <td>0.166667</td>
    </tr>
    <tr>
      <td>1</td>
      <td>2</td>
      <td>0.305556</td>
    </tr>
  </tbody>
</table>
</div>




```python
nRolls =[]
probs =[]

for i in range(1,6,1):
    nRolls.append(i)
    probs.append(1-(5/6)**i) #probability of at least one 6: 1-(5/6)

rollsDF = pd.DataFrame({"# of Rolls": nRolls, "Probability of rolling at least one 6": probs})
rollsDF
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
      <th># of Rolls</th>
      <th>Probability of rolling at least one 6</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>1</td>
      <td>0.166667</td>
    </tr>
    <tr>
      <td>1</td>
      <td>2</td>
      <td>0.305556</td>
    </tr>
    <tr>
      <td>2</td>
      <td>3</td>
      <td>0.421296</td>
    </tr>
    <tr>
      <td>3</td>
      <td>4</td>
      <td>0.517747</td>
    </tr>
    <tr>
      <td>4</td>
      <td>5</td>
      <td>0.598122</td>
    </tr>
  </tbody>
</table>
</div>




```python
nRolls =[]
probs =[]

for i in range(1,11,1):
    nRolls.append(i)
    probs.append(1-(5/6)**i) #probability of at least one 6: 1-(5/6)

rollsDF = pd.DataFrame({"# of Rolls": nRolls, "Probability of rolling at least one 6": probs})
rollsDF
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
      <th># of Rolls</th>
      <th>Probability of rolling at least one 6</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>1</td>
      <td>0.166667</td>
    </tr>
    <tr>
      <td>1</td>
      <td>2</td>
      <td>0.305556</td>
    </tr>
    <tr>
      <td>2</td>
      <td>3</td>
      <td>0.421296</td>
    </tr>
    <tr>
      <td>3</td>
      <td>4</td>
      <td>0.517747</td>
    </tr>
    <tr>
      <td>4</td>
      <td>5</td>
      <td>0.598122</td>
    </tr>
    <tr>
      <td>5</td>
      <td>6</td>
      <td>0.665102</td>
    </tr>
    <tr>
      <td>6</td>
      <td>7</td>
      <td>0.720918</td>
    </tr>
    <tr>
      <td>7</td>
      <td>8</td>
      <td>0.767432</td>
    </tr>
    <tr>
      <td>8</td>
      <td>9</td>
      <td>0.806193</td>
    </tr>
    <tr>
      <td>9</td>
      <td>10</td>
      <td>0.838494</td>
    </tr>
  </tbody>
</table>
</div>




```python
nRolls =[]
probs =[]

for i in range(1,51,1):
    nRolls.append(i)
    probs.append(1-(5/6)**i) #probability of at least one 6: 1-(5/6)

rollsDF = pd.DataFrame({"# of Rolls": nRolls, "Probability of rolling at least one 6": probs})
```


```python
rollsDF.plot.scatter(x="# of Rolls", y="Probability of rolling at least one 6")
```




    <matplotlib.axes._subplots.AxesSubplot at 0x2c7f97a3d88>




![png](output_53_1.png)


___
### Example: What is the probability of drawing an ace at least once (with replacement):
- in 2 tries
- in 5 tries
- in 10 tries
- in 20 tries - make a scatter plot.



```python
nDraws =[]
probs =[]

for i in range(1,3,1):
    nDraws.append(i)
    probs.append(1-(48/52)**i) #probability of drawing an ace least once : 1-(48/52)

DrawsDF = pd.DataFrame({"# of Draws": nDraws, "Probability of drawing an ace at least once": probs})
DrawsDF
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
      <th># of Draws</th>
      <th>Probability of drawing an ace at least once</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>1</td>
      <td>0.076923</td>
    </tr>
    <tr>
      <td>1</td>
      <td>2</td>
      <td>0.147929</td>
    </tr>
  </tbody>
</table>
</div>




```python
nDraws =[]
probs =[]

for i in range(1,6,1):
    nDraws.append(i)
    probs.append(1-(48/52)**i) #probability of drawing an ace least once : 1-(48/52)

DrawsDF = pd.DataFrame({"# of Draws": nDraws, "Probability of drawing an ace at least once": probs})
DrawsDF
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
      <th># of Draws</th>
      <th>Probability of drawing an ace at least once</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>1</td>
      <td>0.076923</td>
    </tr>
    <tr>
      <td>1</td>
      <td>2</td>
      <td>0.147929</td>
    </tr>
    <tr>
      <td>2</td>
      <td>3</td>
      <td>0.213473</td>
    </tr>
    <tr>
      <td>3</td>
      <td>4</td>
      <td>0.273975</td>
    </tr>
    <tr>
      <td>4</td>
      <td>5</td>
      <td>0.329823</td>
    </tr>
  </tbody>
</table>
</div>




```python
nDraws =[]
probs =[]

for i in range(1,11,1):
    nDraws.append(i)
    probs.append(1-(48/52)**i) #probability of drawing an ace least once : 1-(48/52)

DrawsDF = pd.DataFrame({"# of Draws": nDraws, "Probability of drawing an ace at least once": probs})
DrawsDF
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
      <th># of Draws</th>
      <th>Probability of drawing an ace at least once</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>1</td>
      <td>0.076923</td>
    </tr>
    <tr>
      <td>1</td>
      <td>2</td>
      <td>0.147929</td>
    </tr>
    <tr>
      <td>2</td>
      <td>3</td>
      <td>0.213473</td>
    </tr>
    <tr>
      <td>3</td>
      <td>4</td>
      <td>0.273975</td>
    </tr>
    <tr>
      <td>4</td>
      <td>5</td>
      <td>0.329823</td>
    </tr>
    <tr>
      <td>5</td>
      <td>6</td>
      <td>0.381375</td>
    </tr>
    <tr>
      <td>6</td>
      <td>7</td>
      <td>0.428962</td>
    </tr>
    <tr>
      <td>7</td>
      <td>8</td>
      <td>0.472888</td>
    </tr>
    <tr>
      <td>8</td>
      <td>9</td>
      <td>0.513435</td>
    </tr>
    <tr>
      <td>9</td>
      <td>10</td>
      <td>0.550863</td>
    </tr>
  </tbody>
</table>
</div>




```python
nDraws =[]
probs =[]

for i in range(1,21,1):
    nDraws.append(i)
    probs.append(1-(48/52)**i) #probability of drawing an ace at least once : 1-(48/52)

DrawsDF = pd.DataFrame({"# of Draws": nDraws, "Probability of drawing an ace at least once": probs})
DrawsDF
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
      <th># of Draws</th>
      <th>Probability of drawing an ace at least once</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>1</td>
      <td>0.076923</td>
    </tr>
    <tr>
      <td>1</td>
      <td>2</td>
      <td>0.147929</td>
    </tr>
    <tr>
      <td>2</td>
      <td>3</td>
      <td>0.213473</td>
    </tr>
    <tr>
      <td>3</td>
      <td>4</td>
      <td>0.273975</td>
    </tr>
    <tr>
      <td>4</td>
      <td>5</td>
      <td>0.329823</td>
    </tr>
    <tr>
      <td>5</td>
      <td>6</td>
      <td>0.381375</td>
    </tr>
    <tr>
      <td>6</td>
      <td>7</td>
      <td>0.428962</td>
    </tr>
    <tr>
      <td>7</td>
      <td>8</td>
      <td>0.472888</td>
    </tr>
    <tr>
      <td>8</td>
      <td>9</td>
      <td>0.513435</td>
    </tr>
    <tr>
      <td>9</td>
      <td>10</td>
      <td>0.550863</td>
    </tr>
    <tr>
      <td>10</td>
      <td>11</td>
      <td>0.585412</td>
    </tr>
    <tr>
      <td>11</td>
      <td>12</td>
      <td>0.617303</td>
    </tr>
    <tr>
      <td>12</td>
      <td>13</td>
      <td>0.646742</td>
    </tr>
    <tr>
      <td>13</td>
      <td>14</td>
      <td>0.673915</td>
    </tr>
    <tr>
      <td>14</td>
      <td>15</td>
      <td>0.698999</td>
    </tr>
    <tr>
      <td>15</td>
      <td>16</td>
      <td>0.722153</td>
    </tr>
    <tr>
      <td>16</td>
      <td>17</td>
      <td>0.743525</td>
    </tr>
    <tr>
      <td>17</td>
      <td>18</td>
      <td>0.763254</td>
    </tr>
    <tr>
      <td>18</td>
      <td>19</td>
      <td>0.781466</td>
    </tr>
    <tr>
      <td>19</td>
      <td>20</td>
      <td>0.798276</td>
    </tr>
  </tbody>
</table>
</div>




```python
DrawsDF.plot.scatter(x="# of Draws", y="Probability of drawing an ace at least once")
```




    <matplotlib.axes._subplots.AxesSubplot at 0x2c7f980aac8>




![png](output_59_1.png)


___
### Example: 
- A) Write a function to find the probability of an event in percentage form based on given outcomes and sample space
- B) Use the function and compute the probability of rolling a 4 with a D6
- C) Use the function and compute the probability of drawing a King from a standard deck of cards
- D) Use the function and compute the probability of drawing the King of Hearts from a standard deck of cards
- E) Use the function and compute the probability of drawing an ace after drawing a king
- F) Use the function and compute the probability of drawing an ace after drawing an ace
- G) Use the function and compute the probability of drawing a heart OR a club
- F) Use the function and compute the probability of drawing a Royal Flush <br>
*hint: (in poker) a straight flush including ace, king, queen, jack, and ten all in the same suit, which is the hand of the highest possible value

__This problem is designed based on an example by *Daniel Poston* from DataCamp, accessible @ *https://www.datacamp.com/community/tutorials/statistics-python-tutorial-probability-1*__


```python
# A
# Create function that returns probability percent rounded to one decimal place
def Prob(outcome, sampspace):
    probability = (outcome / sampspace) * 100
    return round(probability, 1)
```


```python
# B
outcome = 1       #Rolling a 4 is only one of the possible outcomes
space = 6         #Rolling a D6 can have 6 different outcomes
Prob(outcome, space)
```




    16.7




```python
# C
outcome = 4       #Drawing a king is four of the possible outcomes
space = 52        #Drawing from a standard deck of cards can have 52 different outcomes
Prob(outcome, space)
```




    7.7




```python
# D
outcome = 1       #Drawing the king of hearts is only 1 of the possible outcomes
space = 52        #Drawing from a standard deck of cards can have 52 different outcomes
Prob(outcome, space)
```




    1.9




```python
# E
outcome = 4       #Drawing an ace is 4 of the possible outcomes
space = 51        #One card has been drawn
Prob(outcome, space)
```




    7.8




```python
# F
outcome = 3       #Once Ace is already drawn
space = 51        #One card has been drawn
Prob(outcome, space)
```




    5.9




```python
# G
hearts = 13       #13 cards of hearts in a deck
space = 52        #total number of cards in a deck
clubs = 13        #13 cards of clubs in a deck
Prob_heartsORclubs= Prob(hearts, space) + Prob(clubs, space)
print("Probability of drawing a heart or a club is",Prob_heartsORclubs,"%")
```

    Probability of drawing a heart or a club is 50.0 %
    


```python
# F
draw1 = 5       #5 cards are needed
space1 = 52        #out of the possible 52 cards
draw2 = 4       #4 cards are needed
space2 = 51        #out of the possible 51 cards
draw3 = 3       #3 cards are needed
space3 = 50        #out of the possible 50 cards
draw4 = 2       #2 cards are needed
space4 = 49        #out of the possible 49 cards
draw5 = 1       #1 cards is needed
space5 = 48        #out of the possible 48 cards

#Probability of a getting a Royal Flush
Prob_RF= 4*(Prob(draw1, space1)/100) * (Prob(draw2, space2)/100) * (Prob(draw3, space3)/100) * (Prob(draw4, space4)/100) * (Prob(draw5, space5)/100)     
print("Probability of drawing a royal flush is",Prob_RF,"%")
```

    Probability of drawing a royal flush is 1.5473203199999998e-06 %
    

___
### Example: Two unbiased dice are thrown once and the total score is observed. Define an appropriate function and use a simulation to find the estimated probability that :
- the total score is greater than 10?
- the total score is even and greater than 7?


__This problem is designed based on an example by *Elliott Saslow*
from Medium.com, accessible @ *https://medium.com/future-vision/simulating-probability-events-in-python-5dd29e34e381*__


```python
import numpy as np
def DiceRoll1(nSimulation):
    count =0
    dice = np.array([1,2,3,4,5,6])         #create a numpy array with values of a D6
    for i in range(nSimulation):
        die1 = np.random.choice(dice,1)    #randomly selecting a value from dice - throw the D6 once
        die2 = np.random.choice(dice,1)    #randomly selecting a value from dice - throw the D6 once again!
        score = die1 + die2                #summing them up
        if score > 10:                     #if it meets our desired condition:
            count +=1                      #add one to the "count"
    return count/nSimulation               #compute the probability of the desired event by dividing count by the total number of trials

nSimulation = 10000
print("The probability of rolling a number greater than 10 after",nSimulation,"rolld is:",DiceRoll1(nSimulation)*100,"%")

```

    The probability of rolling a number greater than 10 after 10000 rolld is: 8.35 %
    


```python
import numpy as np
def DiceRoll2(nSimulation):
    count =0
    dice = np.array([1,2,3,4,5,6])         #create a numpy array with values of a D6
    for i in range(nSimulation):
        die1 = np.random.choice(dice,1)    #randomly selecting a value from dice - throw the D6 once
        die2 = np.random.choice(dice,1)    #randomly selecting a value from dice - throw the D6 once again!
        score = die1 + die2
        if score %2 ==0 and score > 7:      #the total score is even and greater than 7
            count +=1
    return count/nSimulation

nSimulation = 10000
print("The probability of rolling an even number and greater than 7 after",nSimulation," rolls is:",DiceRoll2(nSimulation)*100,"%")
```

    The probability of rolling an even number and greater than 7 after 10000  rolls is: 24.77 %
    

___
### Example: An urn contains 10 white balls, 20 reds and 30 greens. We want to draw 5 balls with replacement. Use a simulation (10000 trials) to find the estimated probability that:
- we draw 3 white and 2 red balls
- we draw 5 balls of the same color


__This problem is designed based on an example by *Elliott Saslow*
from Medium.com, accessible @ *https://medium.com/future-vision/simulating-probability-events-in-python-5dd29e34e381*__


```python
# A
import numpy as np
import random
d = {}                     #Create an empty dictionary to associate numbers and colors
for i in range(0,60,1):     #total of 60 balls
    if i <10:                 #10 white balls
        d[i]="White"
    elif i>9 and i<30:         #20 red balls
        d[i]="Red"
    else:                         #60-30=30 green balls
        d[i]="Green"
#
nSimulation= 10000         #How many trials?
outcome1= 0                #initial value on the desired outcome counter

for i in range(nSimulation):
    draw=[]                     #an empty list for the draws
    for i in range(5):                               #how many balls we want to draw?
        draw.append(d[random.randint(0,59)])         #randomly choose a number from 0 to 59- simulation of drawing balls
    drawarray = np.array(draw)                       #convert the list into a numpy array
    white = sum(drawarray== "White")                 #count the white balls
    red = sum(drawarray== "Red")                     #count the red balls
    green = sum(drawarray== "Green")                 #count the green balls
    if white ==3 and red==2:                         #If the desired condition is met, add one to the counter
        outcome1 +=1
print("The probability of drawing 3 white and 2 red balls is",(outcome1/nSimulation)*100,"%")
```

    The probability of drawing 3 white and 2 red balls is 0.54 %
    


```python
# B
import numpy as np
import random
d = {}
for i in range(0,60,1):
    if i <10:
        d[i]="White"
    elif i>9 and i<30:
        d[i]="Red"
    else:
        d[i]="Green"
#
nSimulation= 10000
outcome1= 0
outcome2= 0         #we can consider multiple desired outcomes


for i in range(nSimulation):
    draw=[]
    for i in range(5):
        draw.append(d[random.randint(0,59)])
    drawarray = np.array(draw)
    white = sum(drawarray== "White")
    red = sum(drawarray== "Red")
    green = sum(drawarray== "Green")
    if white ==3 and red==2:
        outcome1 +=1
    if white ==5 or red==5 or green==5:
        outcome2 +=1

print("The probability of drawing 3 white and 2 red balls is",(outcome1/nSimulation)*100,"%")
print("The probability of drawing 5 balls of the same color is",(outcome2/nSimulation)*100,"%")

```

    The probability of drawing 3 white and 2 red balls is 0.53 %
    The probability of drawing 5 balls of the same color is 3.8 %
    

___
![](https://media2.giphy.com/media/5nj4ZZWl6QwneEaBX4/source.gif) <br>

*Here are some of the resources used for creating this notebook:* 


- __"Poker Probability and Statistics with Python"__ by __Daniel Poston__ available at *https://www.datacamp.com/community/tutorials/statistics-python-tutorial-probability-1*<br>
- __"Simulating probability events in Python"__ by __Elliott Saslow__ available at *https://medium.com/future-vision/simulating-probability-events-in-python-5dd29e34e381*<br>


*Here are some great reads on this topic:* 
- __"Simulate the Monty Hall Problem Using Python"__ by __randerson112358__ available at *https://medium.com/swlh/simulate-the-monty-hall-problem-using-python-7b76b943640e* <br>
- __"The Monty Hall problem"__ available at *https://scipython.com/book/chapter-4-the-core-python-language-ii/examples/the-monty-hall-problem/*<br>
- __"Introduction to Probability Using Python"__ by __Lisandra Melo__ available at *https://medium.com/future-vision/simulating-probability-events-in-python-5dd29e34e381* <br>
- __"Introduction to probability and statistics for Data Scientists and machine learning using python : Part-1"__ by __Arun Singh__ available at *https://medium.com/@anayan/introduction-to-probability-and-statistics-for-data-scientists-and-machine-learning-using-python-377a9b082487*<br>

*Here are some great videos on these topics:* 
- __"Monty Hall Problem - Numberphile"__ by __Numberphile__ available at *https://www.youtube.com/watch?v=4Lb-6rxZxx0* <br>
- __"The Monty Hall Problem"__ by __D!NG__ available at *https://www.youtube.com/watch?v=TVq2ivVpZgQ* <br>
- __"21 - Monty Hall - PROPENSITY BASED THEORETICAL MODEL PROBABILITY - MATHEMATICS in the MOVIES"__ by __Motivating Mathematical Education and STEM__ available at *https://www.youtube.com/watch?v=iBdjqtR2iK4* <br>
- __"The Monty Hall Problem"__ by __niansenx__ available at *https://www.youtube.com/watch?v=mhlc7peGlGg* <br>
- __"The Monty Hall Problem - Explained"__ by __AsapSCIENCE__ available at *https://www.youtube.com/watch?v=9vRUxbzJZ9Y* <br>
- __"Introduction to Probability | 365 Data Science Online Course"__ by __365 Data Science__ available at *https://www.youtube.com/watch?v=soZRfdnkUQg* <br>
- __"Probability explained | Independent and dependent events | Probability and Statistics | Khan Academy"__ by __Khan Academy__ available at *https://www.youtube.com/watch?v=uzkc-qNVoOk* <br>
- __"Math Antics - Basic Probability"__ by __mathantics__ available at *https://www.youtube.com/watch?v=KzfWUEJjG18* <br>

___
![](https://media2.giphy.com/media/dNgK7Ws7y176U/200.gif) <br>


## Exercise: Risk or Probability  <br>

### Are they the same? Are they different? Discuss your opinion. 

#### _Make sure to cite any resources that you may use._ 


```python

```

![](https://cdn.quotes.pub/660x400/thats-too-bad-mr-hall-said-opening-door-579647.jpg)
