#!/usr/bin/env python
# coding: utf-8

# <div class="alert alert-block alert-info">
#     <b><h1>ENGR 1330 Computational Thinking with Data Science </h1></b> 
# </div> 
# 
# Copyright © 2021 Theodore G. Cleveland and Farhang Forghanparast
# 
# Last GitHub Commit Date: 
#     
# # 22: Testing Hypothesis - Comparing Collections
# - Comparing two (or more) collections
# - Parametric and Non-Parametric Tests
# - Type 1 & Type 2 errors

# ## Background

# In engineering, when we wish to start asking questions about the data and interpret the results, we use statistical methods that provide a confidence or likelihood about the answers. In general, this class of methods is called statistical hypothesis testing, or significance tests. The material for today's lecture is inspired by and gathered from several resources including:
# 
# - *Hypothesis testing in Machine learning using Python* by *Yogesh Agrawal* available at https://towardsdatascience.com/hypothesis-testing-in-machine-learning-using-python-a0dc89e169ce
# - *Demystifying hypothesis testing with simple Python examples* by *Tirthajyoti Sarkar* available at https://towardsdatascience.com/demystifying-hypothesis-testing-with-simple-python-examples-4997ad3c5294
# - *A Gentle Introduction to Statistical Hypothesis Testing* by *Jason Brownlee* available at https://machinelearningmastery.com/statistical-hypothesis-tests/
# 
# Let's go over a few important concepts first.

# ### <font color=crimson>What is hypothesis testing ?</font><br>
# 
# Hypothesis testing is a statistical method that is used in making statistical decisions (about population) using experimental data (samples). Hypothesis Testing is basically an assumption that we make about the population parameter.<br>
# Ex : you say on average, students in the class are taller than 5 ft and 4 inches or an average boy is taller than girls or a specific treatment is effective in treating COVID-19 patients. <br>
# We need some mathematical conclusion that whatever we are assuming is true. We will validate our hypotheses, basing our conclusion on random samples and empirical distributions._

# ### <font color=crimson>Why do we use it ?</font><br>
# 
# Hypothesis testing is an essential procedure in statistics. A hypothesis test evaluates two mutually exclusive statements about a population to determine which statement is best supported by the sample data. When we say that a finding is statistically significant, it’s thanks to a hypothesis test._

# ![](https://luminousmen.com/media/demystifying-hypothesis-testing.jpg)

# ### <font color=crimson>Which are important elements of hypothesis testing ?</font><br>
# 
# **Null hypothesis:**<br> 
# 
# The assertion of a statistical test is called the null hypothesis, or hypothesis 0 (H0 for short). It is often called the default assumption, or the assumption that nothing has changed. In inferential statistics, the null hypothesis is a general statement or default position that there is no relationship between two measured phenomena, or no association among groups. In other words it is a basic assertion made based on domain or problem knowledge.
# 
# Example : a company's gadget production is = 50 unit/per day.
#     
# **Alternative hypothesis:**<br> 
# 
# A violation of the test’s assertion is often called the first hypothesis, hypothesis 1 or H1 for short. H1 is really a short hand for “some other hypothesis,” as all we know is that the evidence suggests that the H0 can be rejected. The alternative hypothesis is the hypothesis used in hypothesis testing that is contrary to the null hypothesis. It is usually taken to be that the observations are the result of a real effect (with some amount of chance variation superposed). 
# Example : a company's production is !=50 unit/per day.
# 
#     

# ### <font color=crimson>What are basic of hypothesis ?</font><br>
# 
# A fundamental stipulation  is normalisation and standard normalisation. all our assertions and alternatives revolve around these 2 terms.<br>
# 
# ![](https://miro.medium.com/max/350/1*U-cR-vP8pYUmLUDwCPv23A.png) <br>
# ![](https://miro.medium.com/max/350/1*2vTwIrqdELKJY-tpheO7GA.jpeg) <br>
# 
# in the 1st image, you can see there are different normal curves. Those normal curves have different means and variances. In the 2nd image if you notice the graph is properly distributed with a mean =0 and variance =1. Concept of z-score comes in picture when we use standardized normal data.
# 
# #### Normal Distribution:
#     A variable is said to be normally distributed or have a normal distribution if its distribution has the shape of a normal curve — a special bell-shaped curve. The graph of a normal distribution is called the normal curve, for which the mean, median, and mode are equal. (The 1st Image)
# #### Standardised Normal Distribution:
#     A standard normal distribution is a normal distribution with mean 0 and standard deviation 1 (The 2nd Image)

# #### <font color=crimson>Z score:</font><br>
#    It is a method of expressing data in relation to the group mean. To obtain the Z-score of a particular data, we calculate its deviation from the mean and then divide it by the SD.<br> 
# ![](https://clavelresearch.files.wordpress.com/2019/03/z-score-sample.png) <br>
# 
# The Z score is one way of standardizing a score so that it can be referred to a standard normal distribution curve.<br>  
# ![](https://datalabbd.com/wp-content/uploads/2019/05/4a.png) <br>
# 
# _Read more on Z-Score @_
# - __*Z-Score: Definition, Formula and Calculation* available at https://www.statisticshowto.com/probability-and-statistics/z-score/__
# - __*Z-Score: Definition, Calculation and Interpretation* by *Saul McLeod* available at https://www.simplypsychology.org/z-score.html__
# 

# #### <font color=crimson>Tailing of Hypothesis:</font><br>
# 
# Depending on the research question hypothesis can be of 2 types. In the Nondirectional (two-tailed) test the Research Question is like: Is there a (statistically) significant difference between scores of Group-A and Group-B in a certain competition? In Directional (one-tailed) test the Research Question is like: Do Group-A score significantly higher than Group-B in a certain competition?<br> 
#    
# ![](https://datalabbd.com/wp-content/uploads/2019/05/4d.png) <br>
# 
# _Read more on Tailing @_
# - *One- and two-tailed tests* available at https://en.wikipedia.org/wiki/One-_and_two-tailed_tests
# - *Z-Score: Definition, Calculation and Interpretation* by *Saul McLeod* available at https://www.simplypsychology.org/z-score.html

# #### <font color=crimson>Level of significance:</font><br>
# ![](https://saffold.com/blog/wp-content/uploads/2014/04/significance.png)<br>
# 
# Refers to the degree of significance in which we accept or reject the null-hypothesis. 100% accuracy is not possible for accepting or rejecting a hypothesis, so we therefore select a level of significance.
# 
# This significance level is usually denoted with alpha $\alpha$ and often it is set to 0.05 or 5% , which means your output should be 95% confident to give similar kind of result in each sample. A smaller alpha value suggests a more robust interpretation of the null hypothesis, such as 1% or 0.1%.

# #### <font color=crimson>P-value :</font><br>
# 
# The P value, or attained (calculated) probability, is the probability (p-value) of the collected data, given that the null hypothesis was true. The p-value reflects the strength of evidence against the null hypothesis. Accordingly, we’ll encounter two situations: the strength is strong enough or not strong enough to reject the null hypothesis.
# 
# The p-value is compared to the pre-chosen alpha value. A result is statistically significant when the p-value is less than alpha. If your P value is less than the chosen significance level then you reject the null hypothesis i.e. accept that your sample gives reasonable evidence to support the alternative hypothesis.
# 
# ```{note}
# If p-value > alpha: Do not reject the null hypothesis (i.e. not significant result).<br>
# If p-value <= alpha: Reject the null hypothesis (i.e. significant result).<br>
# ```
# 
# 
# ![](https://www.simplypsychology.org/p-value.png)<br>
# 
# 
# For example, if we were performing a test of whether a data sample was normally distributed and we calculated a p-value of .07, we could state something like:
# 
#     "The test found that the data sample was normal, failing to reject the null hypothesis at a 5% significance level.""
# 
# The significance level can be inverted by subtracting it from 1 to give a **confidence level** of the hypothesis given the observed sample data.
# Therefore, statements such as the following can also be made:
# 
#     "The test found that the data was normal, failing to reject the null hypothesis at a 95% confidence level.""

# ### Example :<br>
# You have a coin and you don’t know whether that is fair or tricky so let’s decide null and alternate hypothes is<br>
# 
# 1. H0 : a coin is a fair coin.<br>
# 2. H1 : a coin is a tricky coin. <br>
# 3. alpha = 5% or 0.05<br>
# 
# Now let’s toss the coin and calculate p-value (probability value).<br>
# 
# Toss a coin 1st time (sample size =1) and result is tail
# 
# - P-value = 50% (as head and tail have equal probability)<br>
# 
# Toss a coin 2nd time (sample size =2) and result is tail, now 
# 
# - P-value = 50/2 = 25%<br>
# 
# and similarly suppose we Toss 6 consecutive times (sample size =6) and got result as P-value = 1.5% 

# In[1]:


print("probability of 6 tails in 6 tosses if coin is fair",round((0.5)**6,3))


# but we set our significance level as 5%. Here we see we are beyond that level i.e. our null- hypothesis does not hold good so we need to reject and propose that this coin is not fair.  It does not necessarily mean that the coin is tricky, but 6 tails in a row is quite unlikely with a fair coin, and a good "bet" would be to reject the coin as unfair, and 95% of the time you would be correct.
# 
# Alternatively, one could phrase the result as a fair coin would produce a result **other** than 6 tails in a row 98.5% of the time.
# 
# Read more on p-value @<br>
# 
# - *P-values Explained By Data Scientist For Data Scientists* by *Admond Lee* available at https://towardsdatascience.com/p-values-explained-by-data-scientist-f40a746cfc8<br>
# - *What a p-Value Tells You about Statistical Data* by *Deborah J. Rumsey* available at https://www.dummies.com/education/math/statistics/what-a-p-value-tells-you-about-statistical-data/<br>
# - *Key to statistical result interpretation: P-value in plain English* by *Tran Quang Hung* available at https://s4be.cochrane.org/blog/2016/03/21/p-value-in-plain-english-2/<br>
# 
# Watch more on p-value @<br>
# 
# - *StatQuest: P Values, clearly explained* available at https://www.youtube.com/watch?v=5Z9OIYA8He8<br>
# - *Understanding the p-value - Statistics Help* available at https://www.youtube.com/watch?v=eyknGvncKLw<br>
# - *What Is A P-Value? - Clearly Explained* available at https://www.youtube.com/watch?v=ukcFrzt6cHk<br>

# 

# #### <font color=crimson>“Reject” vs “Failure to Reject”</font><br>
#   
# The p-value is probabilistic. This means that when we interpret the result of a statistical test, we do not know what is true or false, only what is likely. Rejecting the null hypothesis means that there is sufficient statistical evidence (from the samples) that the null hypothesis does not look likely (for the population). Otherwise, it means that there is not sufficient statistical evidence to reject the null hypothesis.<br>
# 
# We may think about the statistical test in terms of the dichotomy of rejecting and accepting the null hypothesis. The danger is that if we say that we “accept” the null hypothesis, the "language" implies that the null hypothesis is true. Instead, it is more preferred to say that we “fail to reject” the null hypothesis, as in, there is insufficient statistical evidence to reject it.<br>

# #### <font color=crimson>Errors in Statistical Tests</font><br>
# 
# The interpretation of a statistical hypothesis test is probabilistic. That means that the evidence of the test may suggest an outcome and be mistaken. For example, if alpha was 5%, it suggests that (at most) 1 time in 20 that the null hypothesis would be mistakenly rejected or failed to be rejected (e.g., because of the statistical noise in the data sample).<br>
# 
# Having a small p-value (rejecting the null hypothesis) either means that the null hypothesis is false (we got it right) or it is true and some rare and unlikely event has been observed (we made a mistake). If this type of error is made, it is called a false positive. We falsely rejected of the null hypothesis. 
# 
# Alternately, given a large p-value (failing to reject the null hypothesis), it may mean that the null hypothesis is true (we got it right) or that the null hypothesis is false and some unlikely event occurred (we made a mistake). If this type of error is made, it is called a false negative. We falsely believe the null hypothesis or assumption of the statistical test.<br>
# 
# ![](https://res.cloudinary.com/data-science-dojo/image/upload/v1527879483/type1and2error_bglnqy.gif)<br>
# 
# Each of these two types of error has a specific name:<br>
#    
#    - Type I Error: The incorrect rejection of a true null hypothesis or a false positive.<br>
#    - Type II Error: The incorrect failure of rejection of a false null hypothesis or a false negative.<br>
# 
# ![](https://miro.medium.com/max/619/1*T5mfQqhcn-nB-n7LOiPv6A.png)<br>
# 
# All statistical hypothesis tests have a risk of making either of these types of errors. False findings are more than just possible; they are probable!<br>
# 
# Ideally, we want to choose a significance level that minimizes the likelihood of one of these errors. E.g. a very small significance level. Although significance levels such as 0.05 and 0.01 are common in many fields of science, harder sciences (as defined by Dr. Sheldon Cooper), such as physics, are more aggressive.
# 
# Read more on Type I and Type II Errors @<br>
# 
# - *Type I and type II errors* available at https://en.wikipedia.org/wiki/Type_I_and_type_II_errors#:~:text=In%20statistical%20hypothesis%20testing%2C%20a,false%20negative%22%20finding%20or%20conclusion<br>
# - *To Err is Human: What are Type I and II Errors?* available at https://www.statisticssolutions.com/to-err-is-human-what-are-type-i-and-ii-errors/<br>
# - *Statistics: What are Type 1 and Type 2 Errors?* available at https://www.abtasty.com/blog/type-1-and-type-2-errors/<br>

# #### <font color=crimson>Some Important Statistical Hypothesis Tests</font><br>
# 
# __Variable Distribution Type Tests (Gaussian)__
# - Shapiro-Wilk Test
# - D’Agostino’s K^2 Test
# - Anderson-Darling Test
# 
# __Compare Sample Means (parametric)__
# - Student’s t-test
# - Paired Student’s t-test
# - Analysis of Variance Test (ANOVA)
# - Repeated Measures ANOVA Test
# 
# __Compare Sample Means (nonparametric)__
# - Mann-Whitney U Test
# - Wilcoxon Signed-Rank Test
# - Kruskal-Wallis H Test
# - Friedman Test
# 
# Check these excellent links to read more on different Statistical Hypothesis Tests:_<br>
# - *17 Statistical Hypothesis Tests in Python (Cheat Sheet)* by *Jason Brownlee * available at https://machinelearningmastery.com/statistical-hypothesis-tests-in-python-cheat-sheet/<br>
# - *Statistical Tests — When to use Which ?* by *vibhor nigam* available at https://towardsdatascience.com/statistical-tests-when-to-use-which-704557554740<br>
# - *Comparing Hypothesis Tests for Continuous, Binary, and Count Data* by *Jim Frost* available at https://statisticsbyjim.com/hypothesis-testing/comparing-hypothesis-tests-data-types/<br>

# *****
# #### <font color=crimson>Normality Tests: Shapiro-Wilk Test</font><br>
# Tests whether a data sample has a Gaussian distribution.<br>
# 
# Assumptions:<br>
# 
# Observations in each sample are independent and identically distributed (iid).<br>
# 
# Interpretation:<br>
# 
# - H0: the sample has a Gaussian distribution.
# - H1: the sample does not have a Gaussian distribution.

# In[2]:


# Example of the Shapiro-Wilk Normality Test
from scipy.stats import shapiro
data = [0.873, 2.817, 0.121, -0.945, -0.055, -1.436, 0.360, -1.478, -1.637, -1.869]
stat, p = shapiro(data)
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
	print('Probably Gaussian')
else:
	print('Probably not Gaussian')


# #### <font color=crimson>Normality Tests: D’Agostino’s K^2 Test</font><br>
# Tests whether a data sample has a Gaussian distribution.<br>
# 
# Assumptions:<br>
# 
# Observations in each sample are independent and identically distributed (iid).<br>
# 
# Interpretation:<br>
# 
# - H0: the sample has a Gaussian distribution.
# - H1: the sample does not have a Gaussian distribution.

# In[3]:


# Example of the D'Agostino's K^2 Normality Test
from scipy.stats import normaltest
data = [0.873, 2.817, 0.121, -0.945, -0.055, -1.436, 0.360, -1.478, -1.637, -1.869]
stat, p = normaltest(data)
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
	print('Probably Gaussian')
else:
	print('Probably not Gaussian')


# _Read more on Normality Tests @_<br>
# - __*A Gentle Introduction to Normality Tests in Python* by *Jason Brownlee* available at https://machinelearningmastery.com/a-gentle-introduction-to-normality-tests-in-python/__<br>

# #### <font color=crimson>Parametric Statistical Hypothesis Tests: Student’s t-test</font><br>
# Tests whether the means of two independent samples are significantly different.
# 
# Assumptions:<br>
# 
# - Observations in each sample are independent and identically distributed (iid).<br>
# - Observations in each sample are normally distributed.<br>
# - Observations in each sample have the same variance.<br>
# 
# Interpretation:
# 
# - H0: the means of the samples are equal.<br>
# - H1: the means of the samples are unequal.<br>

# In[4]:


# Example of the Student's t-test
from scipy.stats import ttest_ind
data1 = [0.873, 2.817, 0.121, -0.945, -0.055, -1.436, 0.360, -1.478, -1.637, -1.869]
data2 = [1.142, -0.432, -0.938, -0.729, -0.846, -0.157, 0.500, 1.183, -1.075, -0.169]
stat, p = ttest_ind(data1, data2)
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
	print('Probably the same distribution')
else:
	print('Probably different distributions')


# 
# #### <font color=crimson>Parametric Statistical Hypothesis Tests: Paired Student’s t-test</font><br>
# Tests whether the means of two paired samples are significantly different.<br>
# 
# Assumptions:<br>
# 
# - Observations in each sample are independent and identically distributed (iid).<br>
# - Observations in each sample are normally distributed.<br>
# - Observations in each sample have the same variance.<br>
# - Observations across each sample are paired.<br>
# 
# Interpretation:<br>
# 
# - H0: the means of the samples are equal.<br>
# - H1: the means of the samples are unequal.<br>

# In[5]:


# Example of the Paired Student's t-test
from scipy.stats import ttest_rel
data1 = [0.873, 2.817, 0.121, -0.945, -0.055, -1.436, 0.360, -1.478, -1.637, -1.869]
data2 = [1.142, -0.432, -0.938, -0.729, -0.846, -0.157, 0.500, 1.183, -1.075, -0.169]
stat, p = ttest_rel(data1, data2)
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
	print('Probably the same distribution')
else:
	print('Probably different distributions')


# 
# #### <font color=crimson>Parametric Statistical Hypothesis Tests: Analysis of Variance Test (ANOVA)</font><br>
# Tests whether the means of two or more independent samples are significantly different.<br>
# 
# Assumptions:<br>
# 
# - Observations in each sample are independent and identically distributed (iid).<br>
# - Observations in each sample are normally distributed.<br>
# - Observations in each sample have the same variance.<br>
# 
# Interpretation:<br>
# 
# - H0: the means of the samples are equal.<br>
# - H1: one or more of the means of the samples are unequal.<br>

# In[6]:


# Example of the Analysis of Variance Test
from scipy.stats import f_oneway
data1 = [0.873, 2.817, 0.121, -0.945, -0.055, -1.436, 0.360, -1.478, -1.637, -1.869]
data2 = [1.142, -0.432, -0.938, -0.729, -0.846, -0.157, 0.500, 1.183, -1.075, -0.169]
data3 = [-0.208, 0.696, 0.928, -1.148, -0.213, 0.229, 0.137, 0.269, -0.870, -1.204]
stat, p = f_oneway(data1, data2, data3)
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
	print('Probably the same distribution')
else:
	print('Probably different distributions')


# _Read more on Parametric Statistical Hypothesis Tests @_<br>
# - __*How to Calculate Parametric Statistical Hypothesis Tests in Python* by *Jason Brownlee* available at https://machinelearningmastery.com/parametric-statistical-significance-tests-in-python/__<br>

# 
# #### <font color=crimson>Nonparametric Statistical Hypothesis Tests: Mann-Whitney U Test</font><br>
# Tests whether the distributions of two independent samples are equal or not.<br>
# 
# Assumptions:<br>
# 
# - Observations in each sample are independent and identically distributed (iid).<br>
# - Observations in each sample can be ranked.<br>
# 
# Interpretation:<br>
# 
# - H0: the distributions of both samples are equal.<br>
# - H1: the distributions of both samples are not equal.<br>

# In[7]:


# Example of the Mann-Whitney U Test
from scipy.stats import mannwhitneyu
data1 = [0.873, 2.817, 0.121, -0.945, -0.055, -1.436, 0.360, -1.478, -1.637, -1.869]
data2 = [1.142, -0.432, -0.938, -0.729, -0.846, -0.157, 0.500, 1.183, -1.075, -0.169]
stat, p = mannwhitneyu(data1, data2)
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
	print('Probably the same distribution')
else:
	print('Probably different distributions')


# 
# #### <font color=crimson>Nonparametric Statistical Hypothesis Tests: Wilcoxon Signed-Rank Test</font><br>
# Tests whether the distributions of two paired samples are equal or not.<br>
# 
# Assumptions:<br>
# 
# - Observations in each sample are independent and identically distributed (iid).:<br>
# - Observations in each sample can be ranked.<br>
# - Observations across each sample are paired.<br>
# 
# Interpretation:<br>
# 
# - H0: the distributions of both samples are equal.<br>
# - H1: the distributions of both samples are not equal.<br>

# In[8]:


# Example of the Wilcoxon Signed-Rank Test
from scipy.stats import wilcoxon
data1 = [0.873, 2.817, 0.121, -0.945, -0.055, -1.436, 0.360, -1.478, -1.637, -1.869]
data2 = [1.142, -0.432, -0.938, -0.729, -0.846, -0.157, 0.500, 1.183, -1.075, -0.169]
stat, p = wilcoxon(data1, data2)
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
	print('Probably the same distribution')
else:
	print('Probably different distributions')


# 
# #### <font color=crimson>Nonparametric Statistical Hypothesis Tests: Kruskal-Wallis H Test</font><br>
# Tests whether the distributions of two or more independent samples are equal or not.<br>
# 
# Assumptions:<br>
# 
# - Observations in each sample are independent and identically distributed (iid).<br>
# - Observations in each sample can be ranked.<br>
# 
# Interpretation:<br>
# 
# - H0: the distributions of all samples are equal.<br>
# - H1: the distributions of one or more samples are not equal.<br>

# In[9]:


# Example of the Kruskal-Wallis H Test
from scipy.stats import kruskal
data1 = [0.873, 2.817, 0.121, -0.945, -0.055, -1.436, 0.360, -1.478, -1.637, -1.869]
data2 = [1.142, -0.432, -0.938, -0.729, -0.846, -0.157, 0.500, 1.183, -1.075, -0.169]
stat, p = kruskal(data1, data2)
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
	print('Probably the same distribution')
else:
	print('Probably different distributions')


# _Read more on Nonparametric Statistical Hypothesis Tests @_<br>
# - __*How to Calculate Nonparametric Statistical Hypothesis Tests in Python* by *Jason Brownlee* available at https://machinelearningmastery.com/nonparametric-statistical-significance-tests-in-python/__<br>

# </hr>
# #### <font color=crimson>Example with REAL data: Do construction activities impact stormwater solids metrics?</font><br>
# 

# ### Background
# The Clean Water Act (CWA) prohibits storm water discharge from construction sites
# that disturb 5 or more acres, unless authorized by a National Pollutant Discharge
# Elimination System (NPDES) permit. Permittees must provide a site description,
# identify sources of contaminants that will affect storm water, identify appropriate
# measures to reduce pollutants in stormwater discharges, and implement these measures.
# The appropriate measures are further divided into four classes: erosion and
# sediment control, stabilization practices, structural practices, and storm water management.
# Collectively the site description and accompanying measures are known as
# the facility’s Storm Water Pollution Prevention Plan (SW3P).
# The permit contains no specific performance measures for construction activities,
# but states that ”EPA anticipates that storm water management will be able to
# provide for the removal of at least 80% of the total suspended solids (TSS).” The
# rules also note ”TSS can be used as an indicator parameter to characterize the
# control of other pollutants, including heavy metals, oxygen demanding pollutants,
# and nutrients commonly found in stormwater discharges”; therefore, solids control is
# critical to the success of any SW3P.
# Although the NPDES permit requires SW3Ps to be in-place, it does not require
# any performance measures as to the effectiveness of the controls with respect to
# construction activities. The reason for the exclusion was to reduce costs associated
# with monitoring storm water discharges, but unfortunately the exclusion also makes
# it difficult for a permittee to assess the effectiveness of the controls implemented at
# their site. Assessing the effectiveness of controls will aid the permittee concerned
# with selecting the most cost effective SW3P.<br>
# 
# ### Problem Statement <br>
# The files precon.CSV and durcon.CSV contain observations of cumulative
# rainfall, total solids, and total suspended solids collected from a construction
# site on Nasa Road 1 in Harris County. <br>
# The data in the file precon.CSV was collected `before` construction began. The data in the file durcon.CSV were collected `during` the construction activity.<br>
# The first column is the date that the observation was made, the second column the total solids (by standard methods), the third column is is the total suspended solids (also by standard methods), and the last column is the cumulative rainfall for that storm.<br>
# 
# 
# 
# ```{note}
# Script to get the files automatically is listed below this note:
# ```
# 
# ```
# import requests # Module to process http/https requests
# remote_url="http://54.243.252.9/engr-1330-webroot/9-MyJupyterNotebooks/41A-HypothesisTests/precon.csv"  # set the url
# rget = requests.get(remote_url, allow_redirects=True)  # get the remote resource, follow imbedded links
# open('precon.csv','wb').write(rget.content) # extract from the remote the contents, assign to a local file same name
# remote_url="http://54.243.252.9/engr-1330-webroot/9-MyJupyterNotebooks/41A-HypothesisTests/durcon.csv"  # set the url
# rget = requests.get(remote_url, allow_redirects=True)  # get the remote resource, follow imbedded links
# open('durcon.csv','wb').write(rget.content) # extract from the remote the contents, assign to a local file same name
# 
# ```
# 
# These data are not time series (there was sufficient time between site visits that you can safely assume each storm was independent.
# __Our task is to analyze these two data sets and decide if construction activities impact stormwater quality in terms of solids measures.__

# In[10]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Read and examine the files, see if we can understand their structure

# In[11]:


precon = pd.read_csv("precon.csv")
durcon = pd.read_csv("durcon.csv") 


# In[12]:


precon


# In[13]:


durcon


# In[14]:


precon.describe()


# In[15]:


durcon.describe()


# In[16]:


precon.plot.box()


# In[17]:


durcon.plot.box()


# Here we see that the scales of the two data sets are quite different. Let's see if  the two construction phases represent approximately the same rainfall conditions? 

# In[18]:


precon['RAIN.PRE'].describe()


# In[19]:


durcon['RAIN.DUR'].describe()


# If we look at the summary statistics, we might conclude there is more rainfall during construction, which could bias our interpretation, a box plot of just rainfall might be useful, as would hypothesis tests.

# In[20]:


precon['RAIN.PRE'].plot.box()


# In[21]:


durcon['RAIN.DUR'].plot.box()


# Hard to tell from the plots, they look a little different, but are they? Lets apply some hypothesis tests

# In[22]:


from scipy.stats import mannwhitneyu # import a useful non-parametric test
stat, p = mannwhitneyu(precon['RAIN.PRE'],durcon['RAIN.DUR'])
print('statistic=%.3f, p-value at rejection =%.3f' % (stat, p))
if p > 0.05:
    print('Probably the same distribution')
else:
    print('Probably different distributions')


# In[23]:


from scipy import stats
results = stats.ttest_ind(precon['RAIN.PRE'], durcon['RAIN.DUR'])
print('statistic=%.3f, p-value at rejection =%.3f ' % (results[0], results[1]))
if p > 0.05:
    print('Probably the same distribution')
else:
    print('Probably different distributions')


# From these two tests (the data are NOT paired) we conclude that the two sets of data originate from the same distribution. Thus the question "Do the two construction phases represent approximately the same rainfall conditions?" can be safely answered in the affirmative.
# 
# Continuing, lets ask the same about total solids, first plots:

# In[24]:


precon['TS.PRE'].plot.box()


# In[25]:


durcon['TS.DUR'].plot.box()


# Look at the difference in scales, the during construction phase, is about 5 to 10 times greater.
# But lets apply some tests to formalize our interpretation.

# In[26]:


stat, p = mannwhitneyu(precon['TS.PRE'],durcon['TS.DUR'])
print('statistic=%.3f, p-value at rejection =%.3f' % (stat, p))
if p > 0.05:
    print('Probably the same distribution')
else:
    print('Probably different distributions')


# In[27]:


results = stats.ttest_ind(precon['TS.PRE'], durcon['TS.DUR'])
print('statistic=%.3f, p-value at rejection =%.3f ' % (results[0], results[1]))
if p > 0.05:
    print('Probably the same distribution')
else:
    print('Probably different distributions')


# Both these tests indicate that the data derive from distirbutions with different measures of central tendency (means). Lets now ask the question about normality, we will apply a test called normaltest. This function tests a null hypothesis that a sample comes from a normal distribution. It is based on D’Agostino and Pearson’s test that combines skew and kurtosis to produce an omnibus test of normality. We will likely get a warning because our sample size is pretty small.

# In[28]:


stat, p = stats.normaltest(precon['TS.PRE'])
print('statistic=%.3f, p-value at rejection =%.3f' % (stat, p))
if p > 0.05:
    print('Probably normal distributed')
else:
    print('Probably Not-normal distributed')


# In[29]:


stat, p = stats.normaltest(durcon['TS.DUR'])
print('statistic=%.3f, p-value at rejection =%.3f' % (stat, p))
if p > 0.05:
    print('Probably normal distributed')
else:
    print('Probably Not-normal distributed')


# #### References
# 
# D’Agostino, R. B. (1971), “An omnibus test of normality for moderate and large sample size”, Biometrika, 58, 341-348
# 
# D’Agostino, R. and Pearson, E. S. (1973), “Tests for departure from normality”, Biometrika, 60, 613-622
# 

# In[ ]:





# In[ ]:





# ## References

# In[ ]:





# <hr>
# 
# ## Laboratory 22
# 
# **Examine** (click) Laboratory 22 as a webpage at [Laboratory 22.html](http://54.243.252.9/engr-1330-webroot/8-Labs/Lab21/Lab22.html)
# 
# **Download** (right-click, save target as ...) Laboratory 22 as a jupyterlab notebook from [Laboratory 21.ipynb](http://54.243.252.9/engr-1330-webroot/8-Labs/Lab22/Lab22.ipynb)
# 

# <hr><hr>
# 
# ## Exercise Set 22
# 
# **Examine** (click) Exercise Set 22 as a webpage at [Exercise 22.html](http://54.243.252.9/engr-1330-webroot/8-Labs/Lab22/Lab22-TH.html)
# 
# **Download** (right-click, save target as ...) Exercise Set 21 as a jupyterlab notebook at  [Exercise Set 22.ipynb](http://54.243.252.9/engr-1330-webroot/8-Labs/Lab22/Lab22-TH.ipynb)
# 
# 
