# *************************************************************************************************************
# Chapter 2.2 Descriptive Plots using MatPlotlib
# *************************************************************************************************************
# *************************************************************************************************************
# Source: https://archive.ics.uci.edu/ml/datasets/Housing
# Open the link to examine the data!!
# Attributes:
# 1. CRIM      per capita crime rate by town
# 2. ZN        proportion of residential land zoned for lots over
#                 25,000 sq.ft.
# 3. INDUS     proportion of non-retail business acres per town
# 4. CHAS      Charles River dummy variable (= 1 if tract bounds
#                 river; 0 otherwise)
# 5. NOX       nitric oxides concentration (parts per 10 million)
# 6. RM        average number of rooms per dwelling
# 7. AGE       proportion of owner-occupied units built prior to 1940
# 8. DIS       weighted distances to five Boston employment centres
# 9. RAD       index of accessibility to radial highways
# 10. TAX      full-value property-tax rate per $10,000
# 11. PTRATIO  pupil-teacher ratio by town
# 12. B        1000(Bk - 0.63)^2 where Bk is the proportion of blacks
#                 by town
# 13. LSTAT    % lower status of the population
# 14. MEDV     Median value of owner-occupied homes in $1000's
# *************************************************************************************************************
# Importing the Data set
# In this section, and this chapter throughout, we will be using this housing data. Chapter 3 will present a
# more comprehensive introduction of data management and databases in Python. Currently, we are just interested
# in importing data from the website...
# *************************************************************************************************************
import pandas as pd  # Pd.read_csv from the panda package reads the data from the website into csv form

housing = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/'
                      'housing/housing.data',
                      header=None,
                      sep='\s+')  # header = None is the default unless your data has the name of variables in Row 0

housing.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS',
              'NOX', 'RM', 'AGE', 'DIS', 'RAD',
              'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV'] # Rename the columns
print(housing.head()) # read first five rows of the data
# *************************************************************************************************************
# Using Matplotlib to make some plots
# First, let's introduce the matplotlib into the program
import matplotlib.pyplot as plt
# *************************************************************************************************************
plt.plot(housing.AGE, housing.TAX) # first define the data set, and then write the variable, unless you derail
                                   #it in another variable
plt.show()
plt.clf()

# *************************************************************************************************************
# Exercise 2.4 Why the plot above is so messy? What is a better scenario case to use the plt.plot() command?
# For our data, scatter plot may be a better visualization of relationships between two variables.
# *************************************************************************************************************
plt.scatter(housing.CRIM, housing.MEDV)
plt.show()
plt.clf()
# *************************************************************************************************************
# Histogram
# In addition, we may want to make some configuration on graphs
# *************************************************************************************************************

plt.hist(housing.TAX, facecolor='green', bins=10, alpha=0.5)#define color, number of bins...
plt.axvline(housing.TAX.mean(), color='b', linestyle='dashed', linewidth=2)#add an average line
plt.title("Boston Housing Tax Histogram")
plt.xlabel("Property Tax")
plt.ylabel("Value")


# Display histogram
plt.show()
plt.clf()

#Maybe you want to customize the classification of your x axis...

plt.scatter(housing.CRIM, housing.MEDV)
plt.xscale('log')
tick_val = [0.1,0.3,1,2,5,30]
tick_lab = ['A','B','C','D','E', 'F'] #customizing a safety 'grade' for your community
plt.xticks(tick_val, tick_lab)
plt.show()
plt.clf()

# *************************************************************************************************************
# Bubble plots
# adding a third variable to change the size of scatter...
# *************************************************************************************************************
# Import numpy as np
import numpy as np

# Store pop as a numpy array: np_pop
np_indus = np.array(housing.INDUS)
np_indus = np_indus * 3 # see what happens if you don't do this multiplication
plt.scatter(housing.CRIM, housing.MEDV, s=np_indus) #s = size
plt.xscale('log')
tick_val = [0.1,0.3,1,2,5,30]
tick_lab = ['A','B','C','D','E', 'F'] #customizing a safety 'grade' for your community
plt.xticks(tick_val, tick_lab)
plt.title("Boston Housing Value and Neighborhood Crime")
plt.xlabel("Crime Grade")
plt.ylabel("Median Housing Value of a Neighborhood")
plt.grid(True) # what does this did?
plt.show()
plt.clf()


