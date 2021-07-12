**Download** (right-click, save target as ...) this page as a jupyterlab notebook from:

[Lab8](https://atomickitty.ddns.net:8000/user/sensei/files/engr-1330-webroot/engr-1330-webbook/ctds-psuedocourse/docs/8-Labs/Lab7/Lab8_Dev.ipynb?_xsrf=2%7C1b4d47c3%7C0c3aca0c53606a3f4b71c448b09296ae%7C1623531240)

___

# <font color=darkred>Laboratory 8: Pandas for Butter! </font>


```python
# Preamble script block to identify host, user, and kernel
import sys
! hostname
! whoami
print(sys.executable)
print(sys.version)
print(sys.version_info)
```

    atomickitty
    sensei
    /opt/jupyterhub/bin/python3
    3.8.5 (default, Jul 28 2020, 12:59:40) 
    [GCC 9.3.0]
    sys.version_info(major=3, minor=8, micro=5, releaselevel='final', serial=0)


## Full name: 
## R#: 
## Title of the notebook:
## Date:
___

![](https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Pandas_logo.svg/1280px-Pandas_logo.svg.png) <br>

## <font color=purple>Pandas</font>
A data table is called a `DataFrame` in pandas (and other programming environments too).

The figure below from https://pandas.pydata.org/docs/getting_started/index.html illustrates a dataframe model:

![](https://pandas.pydata.org/docs/_images/01_table_dataframe.svg) 

Each column and each row in a dataframe is called a series, the header row, and index column are special.

To use pandas, we need to import the module, generally pandas has numpy as a dependency so it also must be imported




```python
import numpy as np #Importing NumPy library as "np"
import pandas as pd #Importing Pandas library as "pd"
```

___
### <font color=darkgreen>Dataframe-structure using primative python</font>

First lets construct a dataframe like object using python primatives.
We will construct 3 lists, one for row names, one for column names, and one for the content.


```python
mytabular = np.random.randint(1,100,(5,4))
myrowname = ['A','B','C','D','E']
mycolname = ['W','X','Y','Z']
mytable = [['' for jcol in range(len(mycolname)+1)] for irow in range(len(myrowname)+1)] #non-null destination matrix, note the implied loop construction
```


```python
print(mytabular)
```

    [[61 82 48 85]
     [45 36 97 72]
     [91  3 22 35]
     [18 65 30 63]
     [79 71  8 45]]


The above builds a placeholder named `mytable` for the psuedo-dataframe.
Next we populate the table, using a for loop to write the column names in the first row, row names in the first column, and the table fill for the rest of the table.


```python
for irow in range(1,len(myrowname)+1): # write the row names
    mytable[irow][0]=myrowname[irow-1]
for jcol in range(1,len(mycolname)+1): # write the column names
    mytable[0][jcol]=mycolname[jcol-1]  
for irow in range(1,len(myrowname)+1): # fill the table (note the nested loop)
    for jcol in range(1,len(mycolname)+1):
        mytable[irow][jcol]=mytabular[irow-1][jcol-1]
```

Now lets print the table out by row and we see we have a very dataframe-like structure


```python
for irow in range(0,len(myrowname)+1):
    print(mytable[irow][0:len(mycolname)+1])
```

    ['', 'W', 'X', 'Y', 'Z']
    ['A', 61, 82, 48, 85]
    ['B', 45, 36, 97, 72]
    ['C', 91, 3, 22, 35]
    ['D', 18, 65, 30, 63]
    ['E', 79, 71, 8, 45]


We can also query by row 


```python
print(mytable[3][0:len(mycolname)+1])
```

    ['C', 91, 3, 22, 35]


Or by column


```python
for irow in range(0,len(myrowname)+1):  #cannot use implied loop in a column slice
    print(mytable[irow][2])
```

    X
    82
    36
    3
    65
    71


Or by row+column index; sort of looks like a spreadsheet syntax.


```python
print(' ',mytable[0][3])
print(mytable[3][0],mytable[3][3])
```

      Y
    C 22


___
### <font color=darkgreen>Create a proper dataframe</font>
We will now do the same using pandas


```python
df = pd.DataFrame(np.random.randint(1,100,(5,4)), ['A','B','C','D','E'], ['W','X','Y','Z'])
df
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
      <th>W</th>
      <th>X</th>
      <th>Y</th>
      <th>Z</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>52</td>
      <td>34</td>
      <td>33</td>
      <td>4</td>
    </tr>
    <tr>
      <th>B</th>
      <td>11</td>
      <td>40</td>
      <td>9</td>
      <td>69</td>
    </tr>
    <tr>
      <th>C</th>
      <td>59</td>
      <td>60</td>
      <td>71</td>
      <td>32</td>
    </tr>
    <tr>
      <th>D</th>
      <td>96</td>
      <td>51</td>
      <td>89</td>
      <td>63</td>
    </tr>
    <tr>
      <th>E</th>
      <td>9</td>
      <td>46</td>
      <td>81</td>
      <td>84</td>
    </tr>
  </tbody>
</table>
</div>



We can also turn our table into a dataframe, notice how the constructor adds header row and index column


```python
df1 = pd.DataFrame(mytable)
df1
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
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td></td>
      <td>W</td>
      <td>X</td>
      <td>Y</td>
      <td>Z</td>
    </tr>
    <tr>
      <th>1</th>
      <td>A</td>
      <td>61</td>
      <td>82</td>
      <td>48</td>
      <td>85</td>
    </tr>
    <tr>
      <th>2</th>
      <td>B</td>
      <td>45</td>
      <td>36</td>
      <td>97</td>
      <td>72</td>
    </tr>
    <tr>
      <th>3</th>
      <td>C</td>
      <td>91</td>
      <td>3</td>
      <td>22</td>
      <td>35</td>
    </tr>
    <tr>
      <th>4</th>
      <td>D</td>
      <td>18</td>
      <td>65</td>
      <td>30</td>
      <td>63</td>
    </tr>
    <tr>
      <th>5</th>
      <td>E</td>
      <td>79</td>
      <td>71</td>
      <td>8</td>
      <td>45</td>
    </tr>
  </tbody>
</table>
</div>



To get proper behavior, we can just reuse our original objects


```python
df2 = pd.DataFrame(mytabular,myrowname,mycolname)
df2
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
      <th>W</th>
      <th>X</th>
      <th>Y</th>
      <th>Z</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>61</td>
      <td>82</td>
      <td>48</td>
      <td>85</td>
    </tr>
    <tr>
      <th>B</th>
      <td>45</td>
      <td>36</td>
      <td>97</td>
      <td>72</td>
    </tr>
    <tr>
      <th>C</th>
      <td>91</td>
      <td>3</td>
      <td>22</td>
      <td>35</td>
    </tr>
    <tr>
      <th>D</th>
      <td>18</td>
      <td>65</td>
      <td>30</td>
      <td>63</td>
    </tr>
    <tr>
      <th>E</th>
      <td>79</td>
      <td>71</td>
      <td>8</td>
      <td>45</td>
    </tr>
  </tbody>
</table>
</div>



___
## <font color=purple>Getting the shape of dataframes</font>

The shape method will return the row and column rank (count) of a dataframe.



```python
df.shape
```




    (5, 4)




```python
df1.shape
```




    (6, 5)




```python
df2.shape
```




    (5, 4)



___
## <font color=purple>Appending new columns</font>
To append a column simply assign a value to a new column name to the dataframe


```python
df['new']= 'NA'
df
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
      <th>W</th>
      <th>X</th>
      <th>Y</th>
      <th>Z</th>
      <th>new</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>52</td>
      <td>34</td>
      <td>33</td>
      <td>4</td>
      <td>NA</td>
    </tr>
    <tr>
      <th>B</th>
      <td>11</td>
      <td>40</td>
      <td>9</td>
      <td>69</td>
      <td>NA</td>
    </tr>
    <tr>
      <th>C</th>
      <td>59</td>
      <td>60</td>
      <td>71</td>
      <td>32</td>
      <td>NA</td>
    </tr>
    <tr>
      <th>D</th>
      <td>96</td>
      <td>51</td>
      <td>89</td>
      <td>63</td>
      <td>NA</td>
    </tr>
    <tr>
      <th>E</th>
      <td>9</td>
      <td>46</td>
      <td>81</td>
      <td>84</td>
      <td>NA</td>
    </tr>
  </tbody>
</table>
</div>



___
## <font color=purple>Appending new rows</font>
A bit trickier but we can create a copy of a row and concatenate it back into the dataframe.


```python
newrow = df.loc[['E']].rename(index={"E": "X"}) # create a single row, rename the index
newtable = pd.concat([df,newrow]) # concatenate the row to bottom of df - note the syntax
```


```python
newtable
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
      <th>W</th>
      <th>X</th>
      <th>Y</th>
      <th>Z</th>
      <th>new</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>52</td>
      <td>34</td>
      <td>33</td>
      <td>4</td>
      <td>NA</td>
    </tr>
    <tr>
      <th>B</th>
      <td>11</td>
      <td>40</td>
      <td>9</td>
      <td>69</td>
      <td>NA</td>
    </tr>
    <tr>
      <th>C</th>
      <td>59</td>
      <td>60</td>
      <td>71</td>
      <td>32</td>
      <td>NA</td>
    </tr>
    <tr>
      <th>D</th>
      <td>96</td>
      <td>51</td>
      <td>89</td>
      <td>63</td>
      <td>NA</td>
    </tr>
    <tr>
      <th>E</th>
      <td>9</td>
      <td>46</td>
      <td>81</td>
      <td>84</td>
      <td>NA</td>
    </tr>
    <tr>
      <th>X</th>
      <td>9</td>
      <td>46</td>
      <td>81</td>
      <td>84</td>
      <td>NA</td>
    </tr>
  </tbody>
</table>
</div>



___
## <font color=purple>Removing Rows and Columns</font>

To remove a column is straightforward, we use the drop method


```python
newtable.drop('new', axis=1, inplace = True)
newtable
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
      <th>W</th>
      <th>X</th>
      <th>Y</th>
      <th>Z</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>52</td>
      <td>34</td>
      <td>33</td>
      <td>4</td>
    </tr>
    <tr>
      <th>B</th>
      <td>11</td>
      <td>40</td>
      <td>9</td>
      <td>69</td>
    </tr>
    <tr>
      <th>C</th>
      <td>59</td>
      <td>60</td>
      <td>71</td>
      <td>32</td>
    </tr>
    <tr>
      <th>D</th>
      <td>96</td>
      <td>51</td>
      <td>89</td>
      <td>63</td>
    </tr>
    <tr>
      <th>E</th>
      <td>9</td>
      <td>46</td>
      <td>81</td>
      <td>84</td>
    </tr>
    <tr>
      <th>X</th>
      <td>9</td>
      <td>46</td>
      <td>81</td>
      <td>84</td>
    </tr>
  </tbody>
</table>
</div>



To remove a row, you really got to want to, easiest is probablty to create a new dataframe with the row removed


```python
newtable = newtable.loc[['A','B','D','E','X']] # select all rows except C
newtable
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
      <th>W</th>
      <th>X</th>
      <th>Y</th>
      <th>Z</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>52</td>
      <td>34</td>
      <td>33</td>
      <td>4</td>
    </tr>
    <tr>
      <th>B</th>
      <td>11</td>
      <td>40</td>
      <td>9</td>
      <td>69</td>
    </tr>
    <tr>
      <th>D</th>
      <td>96</td>
      <td>51</td>
      <td>89</td>
      <td>63</td>
    </tr>
    <tr>
      <th>E</th>
      <td>9</td>
      <td>46</td>
      <td>81</td>
      <td>84</td>
    </tr>
    <tr>
      <th>X</th>
      <td>9</td>
      <td>46</td>
      <td>81</td>
      <td>84</td>
    </tr>
  </tbody>
</table>
</div>



___
## <font color=purple>Indexing</font>
We have already been indexing, but a few examples follow:


```python
newtable['X'] #Selecing a single column
```




    A    34
    B    40
    D    51
    E    46
    X    46
    Name: X, dtype: int64




```python
newtable[['X','W']] #Selecing multiple columns
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
      <th>X</th>
      <th>W</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>34</td>
      <td>52</td>
    </tr>
    <tr>
      <th>B</th>
      <td>40</td>
      <td>11</td>
    </tr>
    <tr>
      <th>D</th>
      <td>51</td>
      <td>96</td>
    </tr>
    <tr>
      <th>E</th>
      <td>46</td>
      <td>9</td>
    </tr>
    <tr>
      <th>X</th>
      <td>46</td>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>




```python
newtable.loc['E'] #Selecing rows based on label via loc[ ] indexer
```




    W     9
    X    46
    Y    81
    Z    84
    Name: E, dtype: int64




```python
newtable.loc[['E','X','B']] #Selecing multiple rows based on label via loc[ ] indexer
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
      <th>W</th>
      <th>X</th>
      <th>Y</th>
      <th>Z</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>E</th>
      <td>9</td>
      <td>46</td>
      <td>81</td>
      <td>84</td>
    </tr>
    <tr>
      <th>X</th>
      <td>9</td>
      <td>46</td>
      <td>81</td>
      <td>84</td>
    </tr>
    <tr>
      <th>B</th>
      <td>11</td>
      <td>40</td>
      <td>9</td>
      <td>69</td>
    </tr>
  </tbody>
</table>
</div>




```python
newtable.loc[['B','E','D'],['X','Y']] #Selecting elemens via both rows and columns via loc[ ] indexer
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
      <th>X</th>
      <th>Y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>B</th>
      <td>40</td>
      <td>9</td>
    </tr>
    <tr>
      <th>E</th>
      <td>46</td>
      <td>81</td>
    </tr>
    <tr>
      <th>D</th>
      <td>51</td>
      <td>89</td>
    </tr>
  </tbody>
</table>
</div>



___
## <font color=purple>Conditional Selection</font>



```python
df = pd.DataFrame({'col1':[1,2,3,4,5,6,7,8],
                   'col2':[444,555,666,444,666,111,222,222],
                   'col3':['orange','apple','grape','mango','jackfruit','watermelon','banana','peach']})
df
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
      <th>col1</th>
      <th>col2</th>
      <th>col3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>444</td>
      <td>orange</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>555</td>
      <td>apple</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>666</td>
      <td>grape</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>444</td>
      <td>mango</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>666</td>
      <td>jackfruit</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>111</td>
      <td>watermelon</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>222</td>
      <td>banana</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>222</td>
      <td>peach</td>
    </tr>
  </tbody>
</table>
</div>




```python
#What fruit corresponds to the number 555 in ‘col2’?

df[df['col2']==555]['col3']
```




    1    apple
    Name: col3, dtype: object




```python
#What fruit corresponds to the minimum number in ‘col2’?

df[df['col2']==df['col2'].min()]['col3']
```




    5    watermelon
    Name: col3, dtype: object



___
## <font color=purple>Descriptor Functions</font>


```python
#Creating a dataframe from a dictionary

df = pd.DataFrame({'col1':[1,2,3,4,5,6,7,8],
                   'col2':[444,555,666,444,666,111,222,222],
                   'col3':['orange','apple','grape','mango','jackfruit','watermelon','banana','peach']})
df
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
      <th>col1</th>
      <th>col2</th>
      <th>col3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>444</td>
      <td>orange</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>555</td>
      <td>apple</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>666</td>
      <td>grape</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>444</td>
      <td>mango</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>666</td>
      <td>jackfruit</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>111</td>
      <td>watermelon</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>222</td>
      <td>banana</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>222</td>
      <td>peach</td>
    </tr>
  </tbody>
</table>
</div>



### <font color=darkblue>`head` method</font>


Returns the first few rows, useful to infer structure


```python
#Returns only the first five rows

df.head()
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
      <th>col1</th>
      <th>col2</th>
      <th>col3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>444</td>
      <td>orange</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>555</td>
      <td>apple</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>666</td>
      <td>grape</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>444</td>
      <td>mango</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>666</td>
      <td>jackfruit</td>
    </tr>
  </tbody>
</table>
</div>



### <font color=darkblue>`info` method</font>

Returns the data model (data column count, names, data types)


```python
#Info about the dataframe

df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 8 entries, 0 to 7
    Data columns (total 3 columns):
     #   Column  Non-Null Count  Dtype 
    ---  ------  --------------  ----- 
     0   col1    8 non-null      int64 
     1   col2    8 non-null      int64 
     2   col3    8 non-null      object
    dtypes: int64(2), object(1)
    memory usage: 320.0+ bytes


### <font color=darkblue>`describe` method</font>

Returns summary statistics of each numeric column.  
Also returns the minimum and maximum value in each column, and the IQR (Interquartile Range).  
Again useful to understand structure of the columns.


```python
#Statistics of the dataframe

df.describe()
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
      <th>col1</th>
      <th>col2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>8.00000</td>
      <td>8.0000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>4.50000</td>
      <td>416.2500</td>
    </tr>
    <tr>
      <th>std</th>
      <td>2.44949</td>
      <td>211.8576</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.00000</td>
      <td>111.0000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>2.75000</td>
      <td>222.0000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>4.50000</td>
      <td>444.0000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>6.25000</td>
      <td>582.7500</td>
    </tr>
    <tr>
      <th>max</th>
      <td>8.00000</td>
      <td>666.0000</td>
    </tr>
  </tbody>
</table>
</div>



### <font color=darkblue>Counting and Sum methods</font>


There are also methods for counts and sums by specific columns


```python
df['col2'].sum() #Sum of a specified column
```




    3330



The `unique` method returns a list of unique values (filters out duplicates in the list, underlying dataframe is preserved)


```python
df['col2'].unique() #Returns the list of unique values along the indexed column 
```




    array([444, 555, 666, 111, 222])



The `nunique` method returns a count of unique values


```python
df['col2'].nunique() #Returns the total number of unique values along the indexed column 
```




    5



The `value_counts()` method returns the count of each unique value (kind of like a histogram, but each value is the bin)


```python
df['col2'].value_counts()  #Returns the number of occurences of each unique value
```




    222    2
    444    2
    666    2
    111    1
    555    1
    Name: col2, dtype: int64



___
## <font color=purple>Using functions in dataframes - symbolic apply</font>

The power of pandas is an ability to apply a function to each element of a dataframe series (or a whole frame) by a technique called symbolic (or synthetic programming) application of the function.

Its pretty complicated but quite handy, best shown by an example


```python
def times2(x):  # A prototype function to scalar multiply an object x by 2
    return(x*2)

print(df)
print('Apply the times2 function to col2')
df['col2'].apply(times2) #Symbolic apply the function to each element of column col2, result is another dataframe
```

       col1  col2        col3
    0     1   444      orange
    1     2   555       apple
    2     3   666       grape
    3     4   444       mango
    4     5   666   jackfruit
    5     6   111  watermelon
    6     7   222      banana
    7     8   222       peach
    Apply the times2 function to col2





    0     888
    1    1110
    2    1332
    3     888
    4    1332
    5     222
    6     444
    7     444
    Name: col2, dtype: int64



___
## <font color=purple>Sorts</font>
 


```python
df.sort_values('col2', ascending = True) #Sorting based on columns 
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
      <th>col1</th>
      <th>col2</th>
      <th>col3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>111</td>
      <td>watermelon</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>222</td>
      <td>banana</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>222</td>
      <td>peach</td>
    </tr>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>444</td>
      <td>orange</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>444</td>
      <td>mango</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>555</td>
      <td>apple</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>666</td>
      <td>grape</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>666</td>
      <td>jackfruit</td>
    </tr>
  </tbody>
</table>
</div>



___
## <font color=purple>Aggregating (Grouping Values) dataframe contents</font>



```python
#Creating a dataframe from a dictionary

data = {
    'key' : ['A', 'B', 'C', 'A', 'B', 'C'],
    'data1' : [1, 2, 3, 4, 5, 6],
    'data2' : [10, 11, 12, 13, 14, 15],
    'data3' : [20, 21, 22, 13, 24, 25]
}

df1 = pd.DataFrame(data)
df1
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
      <th>key</th>
      <th>data1</th>
      <th>data2</th>
      <th>data3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A</td>
      <td>1</td>
      <td>10</td>
      <td>20</td>
    </tr>
    <tr>
      <th>1</th>
      <td>B</td>
      <td>2</td>
      <td>11</td>
      <td>21</td>
    </tr>
    <tr>
      <th>2</th>
      <td>C</td>
      <td>3</td>
      <td>12</td>
      <td>22</td>
    </tr>
    <tr>
      <th>3</th>
      <td>A</td>
      <td>4</td>
      <td>13</td>
      <td>13</td>
    </tr>
    <tr>
      <th>4</th>
      <td>B</td>
      <td>5</td>
      <td>14</td>
      <td>24</td>
    </tr>
    <tr>
      <th>5</th>
      <td>C</td>
      <td>6</td>
      <td>15</td>
      <td>25</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Grouping and summing values in all the columns based on the column 'key'

df1.groupby('key').sum()
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
      <th>data1</th>
      <th>data2</th>
      <th>data3</th>
    </tr>
    <tr>
      <th>key</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>5</td>
      <td>23</td>
      <td>33</td>
    </tr>
    <tr>
      <th>B</th>
      <td>7</td>
      <td>25</td>
      <td>45</td>
    </tr>
    <tr>
      <th>C</th>
      <td>9</td>
      <td>27</td>
      <td>47</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Grouping and summing values in the selected columns based on the column 'key'

df1.groupby('key')[['data1', 'data2']].sum()
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
      <th>data1</th>
      <th>data2</th>
    </tr>
    <tr>
      <th>key</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>5</td>
      <td>23</td>
    </tr>
    <tr>
      <th>B</th>
      <td>7</td>
      <td>25</td>
    </tr>
    <tr>
      <th>C</th>
      <td>9</td>
      <td>27</td>
    </tr>
  </tbody>
</table>
</div>



___
## <font color=purple>Filtering out missing values</font>


```python
#Creating a dataframe from a dictionary

df = pd.DataFrame({'col1':[1,2,3,4,None,6,7,None],
                   'col2':[444,555,None,444,666,111,None,222],
                   'col3':['orange','apple','grape','mango','jackfruit','watermelon','banana','peach']})
df
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
      <th>col1</th>
      <th>col2</th>
      <th>col3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.0</td>
      <td>444.0</td>
      <td>orange</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2.0</td>
      <td>555.0</td>
      <td>apple</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3.0</td>
      <td>NaN</td>
      <td>grape</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4.0</td>
      <td>444.0</td>
      <td>mango</td>
    </tr>
    <tr>
      <th>4</th>
      <td>NaN</td>
      <td>666.0</td>
      <td>jackfruit</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6.0</td>
      <td>111.0</td>
      <td>watermelon</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7.0</td>
      <td>NaN</td>
      <td>banana</td>
    </tr>
    <tr>
      <th>7</th>
      <td>NaN</td>
      <td>222.0</td>
      <td>peach</td>
    </tr>
  </tbody>
</table>
</div>



Below we drop any row that contains a `NaN` code.


```python
df_dropped = df.dropna()
df_dropped
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
      <th>col1</th>
      <th>col2</th>
      <th>col3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.0</td>
      <td>444.0</td>
      <td>orange</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2.0</td>
      <td>555.0</td>
      <td>apple</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4.0</td>
      <td>444.0</td>
      <td>mango</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6.0</td>
      <td>111.0</td>
      <td>watermelon</td>
    </tr>
  </tbody>
</table>
</div>



Below we replace `NaN` codes with some value, in this case 0


```python
df_filled1 = df.fillna(0)
df_filled1
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
      <th>col1</th>
      <th>col2</th>
      <th>col3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.0</td>
      <td>444.0</td>
      <td>orange</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2.0</td>
      <td>555.0</td>
      <td>apple</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3.0</td>
      <td>0.0</td>
      <td>grape</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4.0</td>
      <td>444.0</td>
      <td>mango</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.0</td>
      <td>666.0</td>
      <td>jackfruit</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6.0</td>
      <td>111.0</td>
      <td>watermelon</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7.0</td>
      <td>0.0</td>
      <td>banana</td>
    </tr>
    <tr>
      <th>7</th>
      <td>0.0</td>
      <td>222.0</td>
      <td>peach</td>
    </tr>
  </tbody>
</table>
</div>



Below we replace `NaN` codes with some value, in this case the mean value of of the column in which the missing value code resides.


```python
df_filled2 = df.fillna(df.mean())
df_filled2
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
      <th>col1</th>
      <th>col2</th>
      <th>col3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.000000</td>
      <td>444.0</td>
      <td>orange</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2.000000</td>
      <td>555.0</td>
      <td>apple</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3.000000</td>
      <td>407.0</td>
      <td>grape</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4.000000</td>
      <td>444.0</td>
      <td>mango</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3.833333</td>
      <td>666.0</td>
      <td>jackfruit</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6.000000</td>
      <td>111.0</td>
      <td>watermelon</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7.000000</td>
      <td>407.0</td>
      <td>banana</td>
    </tr>
    <tr>
      <th>7</th>
      <td>3.833333</td>
      <td>222.0</td>
      <td>peach</td>
    </tr>
  </tbody>
</table>
</div>



___
## <font color=purple>Reading a File into a Dataframe</font>

Pandas has methods to read common file types, such as `csv`,`xlsx`, and `json`.  Ordinary text files are also quite manageable.

On a machine you control you can write script to retrieve files from the internet and process them.



```python
import pandas as pd 
readfilecsv = pd.read_csv('CSV_ReadingFile.csv')  #Reading a .csv file
print(readfilecsv)
```

        a   b   c   d
    0   0   1   2   3
    1   4   5   6   7
    2   8   9  10  11
    3  12  13  14  15


Similar to reading and writing .csv files, you can also read and write .xslx files as below (useful to know this)


```python
readfileexcel = pd.read_excel('Excel_ReadingFile.xlsx', sheet_name='Sheet1', engine='openpyxl') #Reading a .xlsx file
print(readfileexcel)
```

       Unnamed: 0   a   b   c   d
    0           0   0   1   2   3
    1           1   4   5   6   7
    2           2   8   9  10  11
    3           3  12  13  14  15


___
## <font color=purple>Writing a dataframe to file</font>


```python
#Creating and writing to a .csv file
readfilecsv = pd.read_csv('CSV_ReadingFile.csv')
readfilecsv.to_csv('CSV_WritingFile1.csv')
readfilecsv = pd.read_csv('CSV_WritingFile1.csv')
print(readfilecsv)
```

       Unnamed: 0   a   b   c   d
    0           0   0   1   2   3
    1           1   4   5   6   7
    2           2   8   9  10  11
    3           3  12  13  14  15



```python
#Creating and writing to a .csv file by excluding row labels 
readfilecsv = pd.read_csv('CSV_ReadingFile.csv')
readfilecsv.to_csv('CSV_WritingFile2.csv', index = False)
readfilecsv = pd.read_csv('CSV_WritingFile2.csv')
print(readfilecsv)
```

        a   b   c   d
    0   0   1   2   3
    1   4   5   6   7
    2   8   9  10  11
    3  12  13  14  15



```python
#Creating and writing to a .xlsx file
readfileexcel = pd.read_excel('Excel_ReadingFile.xlsx', sheet_name='Sheet1',  engine='openpyxl')
readfileexcel.to_excel('Excel_WritingFile.xlsx', sheet_name='MySheet',  engine='openpyxl')
readfileexcel = pd.read_excel('Excel_WritingFile.xlsx', sheet_name='MySheet',  engine='openpyxl')
print(readfileexcel)
```

       Unnamed: 0  Unnamed: 0.1   a   b   c   d
    0           0             0   0   1   2   3
    1           1             1   4   5   6   7
    2           2             2   8   9  10  11
    3           3             3  12  13  14  15


___
## <font color=orange>This is a Pandas Cheat Sheet</font>

![](https://i.pinimg.com/originals/39/08/5c/39085c27945ad3eb49e0de7dff6f0b0e.png)


___
![](https://media2.giphy.com/media/5nj4ZZWl6QwneEaBX4/source.gif) <br>

*Here are some of the resources used for creating this notebook:* 

- Pandas foundations. Retrieved February 15, 2021, from https://www.datacamp.com/courses/pandas-foundations <br>
- Pandas tutorial. Retrieved February 15, 2021, from https://www.w3schools.com/python/pandas/default.asp <br>
- Pandas tutorial: Dataframes in Python. Retrieved February 15, 2021, from https://www.datacamp.com/community/tutorials/pandas-tutorial-dataframe-python <br>

*Here are some great reads on this topic:* 
- __"Introduction to Pandas in Python"__ available at *https://www.geeksforgeeks.org/introduction-to-pandas-in-python/<br>
- __"Pandas Introduction & Tutorials for Beginners"__ by __Walker Rowe__, available at *https://www.bmc.com/blogs/pandas-basics/ <br>
- __"Using Pandas and Python to Explore Your Dataset"__ by __Reka Horvath__ available at *https://realpython.com/pandas-python-explore-dataset/ <br>
- __"Python Pandas Tutorial: A Complete Introduction for Beginners"__ by __George McIntire, Lauren Washington, and Brendan Martin__ available at *https://www.learndatasci.com/tutorials/python-pandas-tutorial-complete-introduction-for-beginners/ <br>


*Here are some great videos on these topics:* 
- __"Python: Pandas Tutorial | Intro to DataFrames"__ by __Joe James__ available at *https://www.youtube.com/watch?v=e60ItwlZTKM <br>
- __"Complete Python Pandas Data Science Tutorial! (Reading CSV/Excel files, Sorting, Filtering, Groupby)"__ by __Keith Galli__ available at *https://www.youtube.com/watch?v=vmEHCJofslg <br>
- __"What is Pandas? Why and How to Use Pandas in Python"__ by __Python Programmer__ available at *https://www.youtube.com/watch?v=dcqPhpY7tWk <br>


___
![](https://media.csesoc.org.au/content/images/2019/10/learn11.gif) <br>


## Exercise: Pandas of Data  <br>

### Pandas library supports three major types of data structures: Series, DataFrames, and Panels. What are some differences between the three structures?

#### * Make sure to cite any resources that you may use. 


```python

```

![](https://www.quotemaster.org/images/q/13084/1308445/i4.png)
![](https://images.fineartamerica.com/images/artworkimages/mediumlarge/2/bad-panda-balazs-solti.jpg)
