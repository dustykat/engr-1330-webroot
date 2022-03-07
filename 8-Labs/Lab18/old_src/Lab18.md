**Download** (right-click, save target as ...) this page as a jupyterlab notebook from: (LINK NEEDS FIXING!)

[Lab18](https://atomickitty.ddns.net:8000/user/sensei/files/engr-1330-webroot/engr-1330-webbook/ctds-psuedocourse/docs/8-Labs/Lab8/Lab9_Dev.ipynb?_xsrf=2%7C1b4d47c3%7C0c3aca0c53606a3f4b71c448b09296ae%7C1623531240)

___

# <font color=darkred>Laboratory 18: "Reject it or Fail!" or a Lab on "Hypothesis Testing" </font>


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
    


```python
A = 123456789 #lET'S SAY THAT THIS IS MY R NUMBER
print(hex(A))
#print(bin(A))
```

    0x75bcd15
    

## Full name: 
## R#: 
## HEX: 
## Title of the notebook
## Date: 

#### Remember where we left our last laboratory session? 

![](https://media.tumblr.com/tumblr_mbui1kpPoU1rxdw8g.gif)


#### Accept my gratitude if you do! But in case you saw Agent K and Agent J sometime after Thursday or for any other reason, do not recall it, here is where were we left things:
#### We had a dataset with two sets of numbers (Set 1 and Set2). We did a bunch of stuff and decided that the Normal Distribution Data Model provides a good fit for both of sample sets. We, then used the right parameters for Normal Data Model (mean and standard deviation) to generate one new sample set based on each set. We then looked at the four sets next to each other and asked a rather simple question: Are these sets different or similar?
#### While we reached some assertions based on visual assessment, we did not manage to solidify our assertation in any numerical way. Well, now is the time! 


```python
#Load the necessary packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```


```python
#Previously ...
data = pd.read_csv("lab13_data.csv") 
set1 = np.array(data['Set1'])
set2 = np.array(data['Set2'])
mu1 = set1.mean()
sd1 = set1.std()
mu2 = set2.mean()
sd2 = set2.std()
set1_s = np.random.normal(mu1, sd1, 100)
set2_s = np.random.normal(mu2, sd2, 100)
data2 = pd.DataFrame({'Set1s':set1_s,'Set2s':set2_s})

```


```python
#Previously ...
fig, ax = plt.subplots()
data2.plot.hist(density=False, ax=ax, title='Histogram: Set1 and Set1 samples vs. Set2 and Set2 samples', bins=40)
data.plot.hist(density=False, ax=ax, bins=40)

ax.set_ylabel('Count')
ax.grid(axis='y')
```


![png](output_9_0.png)



```python
#Previously ...
fig = plt.figure(figsize =(10, 7)) 
plt.boxplot ([set1, set1_s, set2, set2_s],1, '')
plt.show()
```


![png](output_10_0.png)


__We can use statistical hypothesis tests to confirm that our sets are from Normal Distribution Data Models. We can use the Shapiro-Wilk Normality Test:__


```python
# the Shapiro-Wilk Normality Test for set1
from scipy.stats import shapiro

stat, p = shapiro(data['Set1'])
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
	print('Probably Gaussian')
else:
	print('Probably not Gaussian')
```

    stat=0.992, p=0.793
    Probably Gaussian
    


```python
# the Shapiro-Wilk Normality Test for set2
from scipy.stats import shapiro

stat, p = shapiro(data['Set2'])
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
	print('Probably Gaussian')
else:
	print('Probably not Gaussian')
```

    stat=0.981, p=0.151
    Probably Gaussian
    

__Now let's confirm that set1 and set1_s are from the same distribution. We can use the Mann-Whitney U Test for this:__


```python
from scipy.stats import mannwhitneyu # import a useful non-parametric test
stat, p = mannwhitneyu(data['Set1'],data2['Set1s'])
print('statistic=%.3f, p-value at rejection =%.3f' % (stat, p))
if p > 0.05:
    print('Probably the same distribution')
else:
    print('Probably different distributions')
```

    statistic=4902.000, p-value at rejection =0.406
    Probably the same distribution
    

__Let's also confirm that set2 and set2_s are from the same distribution:__


```python
from scipy.stats import mannwhitneyu # import a useful non-parametric test
stat, p = mannwhitneyu(data['Set2'],data2['Set2s'])
print('statistic=%.3f, p-value at rejection =%.3f' % (stat, p))
if p > 0.05:
    print('Probably the same distribution')
else:
    print('Probably different distributions')
```

    statistic=4811.000, p-value at rejection =0.323
    Probably the same distribution
    

__Based on the results we can say set1 and set1_s probably belong to the same distrubtion. The same can be stated about set2 and set2_s. Now let's check and see if set1 and set2 are SIGNIFICANTLY different or not?__


```python
from scipy.stats import mannwhitneyu # import a useful non-parametric test
stat, p = mannwhitneyu(data['Set1'],data['Set2'])
print('statistic=%.3f, p-value at rejection =%.3f' % (stat, p))
if p > 0.05:
    print('Probably the same distribution')
else:
    print('Probably different distributions')
```

    statistic=0.000, p-value at rejection =0.000
    Probably different distributions
    

__The test's result indicate that the set1 and set2 belong to distirbutions with different measures of central tendency (means). We can check the same for set1_s and set2_s as well:__


```python
from scipy.stats import mannwhitneyu # import a useful non-parametric test
stat, p = mannwhitneyu(data2['Set1s'],data2['Set2s'])
print('statistic=%.3f, p-value at rejection =%.3f' % (stat, p))
if p > 0.05:
    print('Probably the same distribution')
else:
    print('Probably different distributions')
```

    statistic=0.000, p-value at rejection =0.000
    Probably different distributions
    

__Now we can state at a 95% confidence level that set1 and set2 are different. The same for set1s and set2s.__

___
### Example: A dataset containing marks obtained by students on basic skills like basic math and language skills (reading and writing) is collected from an educational institution and we have been tasked to give them some important inferences. 

> Hypothesis: There is no difference in means of student performance in any of basic literacy skills i.e. reading, writing, math.

___
*This is based on an example by Joju John Varghese on "Hypothesis Testing for Inference using a Dataset" available @ https://medium.com/swlh/hypothesis-testing-for-inference-using-a-data-set-aaa799e94cdf. The dataset is available @ https://www.kaggle.com/spscientist/students-performance-in-exams.*


```python
df = pd.read_csv("StudentsPerformance.csv") 
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
      <th>gender</th>
      <th>race/ethnicity</th>
      <th>parental level of education</th>
      <th>lunch</th>
      <th>test preparation course</th>
      <th>math score</th>
      <th>reading score</th>
      <th>writing score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>female</td>
      <td>group B</td>
      <td>bachelor's degree</td>
      <td>standard</td>
      <td>none</td>
      <td>72</td>
      <td>72</td>
      <td>74</td>
    </tr>
    <tr>
      <td>1</td>
      <td>female</td>
      <td>group C</td>
      <td>some college</td>
      <td>standard</td>
      <td>completed</td>
      <td>69</td>
      <td>90</td>
      <td>88</td>
    </tr>
    <tr>
      <td>2</td>
      <td>female</td>
      <td>group B</td>
      <td>master's degree</td>
      <td>standard</td>
      <td>none</td>
      <td>90</td>
      <td>95</td>
      <td>93</td>
    </tr>
    <tr>
      <td>3</td>
      <td>male</td>
      <td>group A</td>
      <td>associate's degree</td>
      <td>free/reduced</td>
      <td>none</td>
      <td>47</td>
      <td>57</td>
      <td>44</td>
    </tr>
    <tr>
      <td>4</td>
      <td>male</td>
      <td>group C</td>
      <td>some college</td>
      <td>standard</td>
      <td>none</td>
      <td>76</td>
      <td>78</td>
      <td>75</td>
    </tr>
  </tbody>
</table>
</div>




```python
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
      <th>math score</th>
      <th>reading score</th>
      <th>writing score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>count</td>
      <td>1000.00000</td>
      <td>1000.000000</td>
      <td>1000.000000</td>
    </tr>
    <tr>
      <td>mean</td>
      <td>66.08900</td>
      <td>69.169000</td>
      <td>68.054000</td>
    </tr>
    <tr>
      <td>std</td>
      <td>15.16308</td>
      <td>14.600192</td>
      <td>15.195657</td>
    </tr>
    <tr>
      <td>min</td>
      <td>0.00000</td>
      <td>17.000000</td>
      <td>10.000000</td>
    </tr>
    <tr>
      <td>25%</td>
      <td>57.00000</td>
      <td>59.000000</td>
      <td>57.750000</td>
    </tr>
    <tr>
      <td>50%</td>
      <td>66.00000</td>
      <td>70.000000</td>
      <td>69.000000</td>
    </tr>
    <tr>
      <td>75%</td>
      <td>77.00000</td>
      <td>79.000000</td>
      <td>79.000000</td>
    </tr>
    <tr>
      <td>max</td>
      <td>100.00000</td>
      <td>100.000000</td>
      <td>100.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
set1 = df['math score']
set2 = df['reading score']
set3 = df['writing score']
```


```python
import seaborn as sns
sns.distplot(set1,color='navy', rug=True)
sns.distplot(set2,color='darkorange', rug=True)
sns.distplot(set3,color='green', rug=True)
plt.xlim(0,100)
plt.xlabel('Test Results')

```




    Text(0.5, 0, 'Test Results')




![png](output_27_1.png)


####  It seems that all three samples have the same population means and it seems there is no significant difference between them at all. Let's set the null and alternative hypothesis:

> Ho: There is no difference in performance of students between math, reading and writing skills. <br>
Ha: There is a difference in performance of students between math, reading and writing skills. <br>


```python
from scipy.stats import mannwhitneyu # import a useful non-parametric test
stat, p = mannwhitneyu(set1,set2)
print('statistic=%.3f, p-value at rejection =%.3f' % (stat, p))
if p > 0.05:
    print('Probably the same distribution')
else:
    print('Probably different distributions')
```

    statistic=441452.500, p-value at rejection =0.000
    Probably different distributions
    


```python
from scipy.stats import mannwhitneyu # import a useful non-parametric test
stat, p = mannwhitneyu(set1,set3)
print('statistic=%.3f, p-value at rejection =%.3f' % (stat, p))
if p > 0.05:
    print('Probably the same distribution')
else:
    print('Probably different distributions')
```

    statistic=461212.500, p-value at rejection =0.001
    Probably different distributions
    


```python
from scipy.stats import mannwhitneyu # import a useful non-parametric test
stat, p = mannwhitneyu(set2,set3)
print('statistic=%.3f, p-value at rejection =%.3f' % (stat, p))
if p > 0.05:
    print('Probably the same distribution')
else:
    print('Probably different distributions')
```

    statistic=480672.000, p-value at rejection =0.067
    Probably the same distribution
    


```python
from scipy.stats import kruskal
stat, p = kruskal(set1, set2, set3)
print('Statistics=%.3f, p=%.3f' % (stat, p))
# interpret
alpha = 0.05
if p > 0.05:
    print('Probably the same distribution')
else:
    print('Probably different distributions')
```

    Statistics=21.225, p=0.000
    Probably different distributions
    

___

### Example: Website Design: A practical example of A/B Testing
*inspired by an example in __"A/B Test Significance in Python"__ by __Samuel Hinton__ available at* https://cosmiccoding.com.au/tutorials/ab_tests <br>
![](https://www.invespcro.com/blog/images/blog-images/ab-test-1-1.jpg) <br>
#### Imagine you’re in charge of a website (e.g., an online videogame shop). You have the current version of the website (aka. "A"), but aren’t happy with it. For instance, you are not selling as much as you like. You want to change the design of the "Add to Cart" button (aka. "B") and maybe that will increase your sells. <br>
![](https://www.volusion.com/blog/content/images/wp/buttonaandbuttonn.jpg) <br>

#### you set up your website so that half the people are directed to the old website, and half to one where you’ve made your change. You have data from both, and want to know, with confidence, “Does the change I made increase the sells?”.<br>

*This is an A/B test. Often this is used interchangably with the term “split testing”, though in general A/B tests test small changes, and split testing might be when you present two entirely different websites to the user.* <br>

#### Why not just change the website and monitor it for a week?
    Good question - by having two sites active at once and randomly directing users to one or the other, you control for all other variables. If one week later puts you the week before Christmas, this will impact sales, and you might draw the wrong conclusion because of these confounding effects.
#### Why is it not an A/B/C test?
    you can have as many perturbations running as you want, but got to keep the name simple. The more perturbations you try though, the smaller a number of samples you’ll have for each case, and the harder it will be to draw statistically significant conclusions.

#### Let us assume you have 1000 users, 550 were directed to site A, 450 to site B. In site A, 48 users made a purchase. In site B, 56 users made a purchase. Is this a statistically significant result?


```python
num_a= 550
num_b = 450
click_a= 48
click_b = 56
rate_a= click_a / num_a
rate_b = click_b / num_b
print(rate_a)
print(rate_b)
```

    0.08727272727272728
    0.12444444444444444
    

#### You can click a button, or not. Two discrete options are available, so this is a textbook binomial distribution, with some unknown rate for site A and site B. We don’t know the true click rate, but we can estimate it using our small sample.


```python
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom

# Determine the probability of having x number of clicks - Binomial Dist.
clicks = np.arange(10, 100)
prob_a = binom(num_a, rate_a).pmf(clicks)
prob_b = binom(num_b, rate_b).pmf(clicks)

# Make the bar plots.
plt.bar(clicks, prob_a, label="A", alpha=0.7)
plt.bar(clicks, prob_b, label="B", alpha=0.7)
plt.legend()
plt.xlabel("# of Sells"); plt.ylabel("Probability");
```


![png](output_37_0.png)


#### So we can see here that b has an edge, but its certaintly possible if we pick two random points according to the histograms for A and B, that A might actually be higher than B! <Br>
    
#### As we’re interested in the average # of sells, this averaging of an underlying distribution means our final estimate will be well approximated by a normal distribution. So let’s reformulate, using the normal approximation here:


```python
from scipy.stats import norm

# Where does this come from? See this link: https://en.wikipedia.org/wiki/Binomial_distribution#Normal_approximation
std_a = np.sqrt(rate_a * (1 - rate_a) / num_a)
std_b = np.sqrt(rate_b * (1 - rate_b) / num_b)

click_rate = np.linspace(0, 0.2, 200)
prob_a = norm(rate_a, std_a).pdf(click_rate)
prob_b = norm(rate_b, std_b).pdf(click_rate)

# Make the bar plots.
plt.plot(click_rate, prob_a, label="A")
plt.plot(click_rate, prob_b, label="B")
plt.legend(frameon=False)
plt.xlabel("Purchase rate"); plt.ylabel("Probability")
```




    Text(0, 0.5, 'Probability')




![png](output_39_1.png)


#### This is also a better plot than the first one, because we’ve removed the confusing effect of site A and site B having a slightly different number of visitors had. So our question is still the same: What is the chance that a draw from B is higher than a draw from A. Is it significant? <br>
#### To answer this, let us utilise the handy fact that the sum (or difference) of normally distributed random numbers is also a normal. This is simple - take the difference in the means and sum the variance. We’ll do two things below: First, get the z-score, and second, plot the proper distribution.




```python
z_score = (rate_b - rate_a) / np.sqrt(std_a**2 + std_b**2)
p = norm(rate_b - rate_a, np.sqrt(std_a**2 + std_b**2))

x = np.linspace(-0.05, 0.15, 1000)
y = p.pdf(x)
area_under_curve = p.sf(0)
plt.plot(x, y, label="PDF")
plt.fill_between(x, 0, y, where=x>0, label="Prob(b>a)", alpha=0.3)
plt.annotate(f"Area={area_under_curve:0.3f}", (0.02, 5))
plt.legend()
plt.xlabel("Difference in purchase rate"); plt.ylabel("Prob");

print(f"zscore is {z_score:0.3f}, with p-value {norm().sf(z_score):0.3f}")
```

    zscore is 1.890, with p-value 0.029
    


![png](output_41_1.png)


#### we can say that given the null hypothesis ("B is less than or equal to A") is true , we would expect to get this result or a result more extreme only 2.9% of the time. As that is a significant result (typically p < 5%), we reject the null hypothesis, and state that we have evidence that B > A. <br>
#### we’ve made a lot of plots for this to try and explain the concept. You can easily write a tiny function to simplify all of this. Whether you want the confidence or the p-value just means changing the final "norm.cdf" to "norm.sf".


```python
def get_confidence_ab_test(click_a, num_a, click_b, num_b):
    rate_a = click_a / num_a
    rate_b = click_b / num_b
    std_a = np.sqrt(rate_a * (1 - rate_a) / num_a)
    std_b = np.sqrt(rate_b * (1 - rate_b) / num_b)
    z_score = (rate_b - rate_a) / np.sqrt(std_a**2 + std_b**2)
    return norm.sf(z_score)

print(get_confidence_ab_test(click_a, num_a, click_b, num_b))
```

    0.029402650172421833
    

#### Remember Non-parametric Statistical Hypothesis Tests? We can use them here as well! <br>
#### Imagine we have the raw results of clicks (purchases), as 0s or 1s, as our distribution.


```python
from scipy.stats import mannwhitneyu

a_dist = np.zeros(num_a)
a_dist[:click_a] = 1
b_dist = np.zeros(num_b)
b_dist[:click_b] = 1

stat, p_value = mannwhitneyu(a_dist, b_dist, alternative="less")
print(f"Mann-Whitney U test for null hypothesis B <= A is {p_value:0.3f}")
```

    Mann-Whitney U test for null hypothesis B <= A is 0.028
    

___

### Example: Times Roman or Times New Roman- That is the question! <br>
![](https://media-exp1.licdn.com/dms/image/C4E1BAQEr76SyZsyo2w/company-background_10000/0/1553614927942?e=2159024400&v=beta&t=UKNhG-wjqdLnaYir1kVvVRyHdJodkMriZe_Wltqp424) <br>
#### The Daily Planet newspaper is considering swiching from the Times Roman Font to the Times New Roman as an attempt to to make it easier for their audience to read the newspaper and hence, increase the online purchases. 
*hint: The Daily Planet is a fictional broadsheet newspaper appearing in American comic books published by DC Comics, commonly in association with Superman. Read more @ https://en.wikipedia.org/wiki/Daily_Planet<br>

![](https://news-cdn.softpedia.com/images/fitted/620x/Times-New-Roman-The-Newpaper-Font-That-Took-Over-Windows-480938-3.jpg) <br>

#### They have prepared two versions of their newspapers, one of each font. On the first day, they had a total of 1398 visitors. Randonmly, half of them (699 visitors) saw the original version (Time Roman) and the other half saw the alternative version (Times New Roman).    <br>
#### The first group purchased a total of 175 copies of the newspaper. This number was 200 copies for the second group. Based on the observations of the first day, first, calculate the purchase rate for each group and then, decide whether the Daily Planet should change their font in order to increase the online engagement time?    <br>


```python
#Day 1
group1= 699
group2= 699
sold1= 175
sold2 = 200
rate1=  sold1/group1
rate2 = sold2/group2

print(f"The ratio for the first group is {rate1:0.4f} copies sold per person")
print(f"The ratio for the second group is {rate2:0.4f} copies sold per person")
from scipy.stats import mannwhitneyu
import numpy as np
a_dist = np.zeros(group1)
a_dist[:sold1] = 1
b_dist = np.zeros(group2)
b_dist[:sold2] = 1

stat, p_value = mannwhitneyu(a_dist, b_dist, alternative="less")
print(f"Mann-Whitney U test for null hypothesis B <= A is {p_value:0.3f}")
```

    The ratio for the first group is 0.2504 copies sold per person
    The ratio for the second group is 0.2861 copies sold per person
    Mann-Whitney U test for null hypothesis B <= A is 0.066
    

#### After a week, they had a total of 10086 visitors. Randonmly, half of them (5043 visitors) saw the original version (Time Roman) and the other half saw the alternative version (Times New Roman).    <br>
#### The first group purchased a total of 1072 copies of the newspaper. This number was 1190 copies for the second group. Based on the observations of the first week, first, calculate the purchase rate for each group and then, decide whether the Daily Planet should change their font in order to increase the online engagement time?    <br>


```python
#Week 1
group1= 5043
group2= 5043
sold1= 1072
sold2 = 1190
rate1=  sold1/group1
rate2 = sold2/group2

print(f"The ratio for the first group is {rate1:0.3f} copies sold per person")
print(f"The ratio for the second group is {rate2:0.3f} copies sold per person")
from scipy.stats import mannwhitneyu
import numpy as np
a_dist = np.zeros(group1)
a_dist[:sold1] = 1
b_dist = np.zeros(group2)
b_dist[:sold2] = 1

stat, p_value = mannwhitneyu(a_dist, b_dist, alternative="less")
print(f"Mann-Whitney U test for null hypothesis B <= A is {p_value:0.3f}")
```

    The ratio for the first group is 0.213 copies sold per person
    The ratio for the second group is 0.236 copies sold per person
    Mann-Whitney U test for null hypothesis B <= A is 0.002
    

#### After a month, they had a total of 42000 visitors. Randonmly, half of them (21000 visitors) saw the original version (Time Roman) and the other half saw the alternative version (Times New Roman).    <br>
#### The first group purchased a total of 4300 copies of the newspaper. This number was 5700 copies for the second group. Based on the observations of the first month, first, calculate the purchase rate for each group and then, decide whether the Daily Planet should change their font in order to increase the online engagement time?    <br>


```python
#Month 1
group1= 21000
group2= 21000
sold1= 4300
sold2 = 5700
rate1=  sold1/group1
rate2 = sold2/group2

print(f"The ratio for the first group is {rate1:0.3f} copies sold per person")
print(f"The ratio for the second group is {rate2:0.3f} copies sold per person")
from scipy.stats import mannwhitneyu
import numpy as np
a_dist = np.zeros(group1)
a_dist[:sold1] = 1
b_dist = np.zeros(group2)
b_dist[:sold2] = 1

stat, p_value = mannwhitneyu(a_dist, b_dist, alternative="less")
print(f"Mann-Whitney U test for null hypothesis B <= A is {p_value:0.15f}")
```

    The ratio for the first group is 0.205 copies sold per person
    The ratio for the second group is 0.271 copies sold per person
    Mann-Whitney U test for null hypothesis B <= A is 0.000000000000000
    

___
![](https://media2.giphy.com/media/5nj4ZZWl6QwneEaBX4/source.gif) <br>


__*Here are some great reads on this topic:*__ 
- __"Hypothesis testing in Machine learning using Python"__ by __Yogesh Agrawal__ available at *https://towardsdatascience.com/hypothesis-testing-in-machine-learning-using-python-a0dc89e169ce* <br>
- __"Quick Guide To Perform Hypothesis Testing"__ available at *https://www.analyticsvidhya.com/blog/2020/12/quick-guide-to-perform-hypothesis-testing/*<br>
- __"A Gentle Introduction to Statistical Hypothesis Testing"__ by __Jason Brownlee__ available at *https://machinelearningmastery.com/statistical-hypothesis-tests/*<br>
- __"17 Statistical Hypothesis Tests in Python (Cheat Sheet)"__ by __Jason Brownlee__ available at *https://machinelearningmastery.com/statistical-hypothesis-tests-in-python-cheat-sheet/*<br>


__*Some great reads on A/B Testing:*__
-  __"Implementing A/B Tests in Python"__ by __Robbie Geoghegan__ available at* https://medium.com/@robbiegeoghegan/implementing-a-b-tests-in-python-514e9eb5b3a1 <br>
-  __"The Math Behind A/B Testing with Example Python Code"__ by __Nguyen Ngo__ available at* https://towardsdatascience.com/the-math-behind-a-b-testing-with-example-code-part-1-of-2-7be752e1d06f <br>
-  __"A/B Testing"__ available at* https://www.optimizely.com/optimization-glossary/ab-testing/ <br>
-  __"A/B Testing Guide"__ available at* https://vwo.com/ab-testing/ <br>

__*Some great videos:*__
-  __"What is A/B Testing? | Data Science in Minutes"__ by __Data Science Dojo__ available at* https://www.youtube.com/watch?v=zFMgpxG-chM <br>
-  __"A/B Testing Intro: Why, What, Where, & How to A/B Test"__ by __Testing Theory__ available at* https://www.youtube.com/watch?v=CH89jd4haRE <br>
-  __"A/B Testing"__ by __Udacity__ available at* https://www.youtube.com/watch?v=8H6QmMQWPEI <br>
- __"Statistical Hypothesis Testing- Data Science with Python"__ by __Technology for Noobs__ available at *https://www.youtube.com/watch?v=kd6zKBa9Rfk* <br>
- __"Hypothesis Testing, p-value & Confidence Intervals, Exploratory Data Analysis In Python Statistics"__ by __TheEngineeringWorld__ available at *https://www.youtube.com/watch?v=kz1IXqcFVCo* <br>
- __"Python Tutorial : Hypothesis tests"__ by __DataCamp__ available at *https://www.youtube.com/watch?v=6wbldEMpRXc* <br>

___
![](https://media2.giphy.com/media/dNgK7Ws7y176U/200.gif) <br>


## Exercise: Wait a minute ... Isn't The Kruskal-Wallis test missing something?  <br>

### We used the Kruskal-Wallis to check whether the three sets belong to the same distribution or at least one of them is different. The question is, how can we find the sets that are different? What is the missing piece in tests such as The Kruskal-Wallis Test?  

#### _Make sure to cite any resources that you may use._ 


```python

```

![](http://img.picturequotes.com/2/124/123499/one-finds-the-truth-by-making-a-hypothesis-and-comparing-observations-with-the-hypothesis-quote-1.jpg)
