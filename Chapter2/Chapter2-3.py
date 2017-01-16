# *************************************************************************************************************
# Chapter 2.3 Data frame Handling using Panda Package
# *************************************************************************************************************
# *************************************************************************************************************
# Handling Dataframe (I): via Dictionary
# *************************************************************************************************************

# The Philosophy of 1:1 onto mapping
animal = ['piggy','dog','cat', 'kangaroo','duck']
impression = ['lovely','royal','smart','swaggy','yummy']
ind_anim = animal.index('kangaroo')
print(impression[ind_anim])

# *************************************************************************************************************
# Exercise 2.5 Write a short code to map piggy to lovely, following the example above. What is the index of
# piggy?
# Let's now create a dictionary
# *************************************************************************************************************

food = {'China':'dumpling', 'Korea':'bibimbap', 'Japan':'sashimi', 'India':'curry' }

# Print out the keys in food
print(food.keys())

# Print out value that belongs to key 'norway'
print(food['Japan'])

# Did you feel how it works?, Now, what if we matched wrong?

food['Japan'] = 'bibimbap' # a good way to examine variables...

# add dictionary items

food['Thailand'] = 'Tom Yum Kun'
print('Thailand' in food)
print(food)

# *************************************************************************************************************
# Exercise 2.6 Now try to delete the India and its mapped results from the dictionary using 1 line of code.
# *************************************************************************************************************

gradebook = { 'Jack': { 'gender':'M', 'grade':80 },
           'Mary': { 'gender':'F', 'grade':20},
           'Alice': { 'gender':'F', 'grade':100},
           'John': { 'gender':'M', 'grade':60} }
print(gradebook['John']['grade'])

# *************************************************************************************************************
# Dictionary mapped to Dataframe
# Let's continue using the dictionary example, and check out how DataFrame work...
# *************************************************************************************************************

name = ['John','Sonata','Mark','Alice','David','Morgan']
gender = ['M','F','M','F','M','M']
grade = [84, 72, 90, 100, 88, 100]

import pandas as pd
gradesheet = {'StudentName':name, 'Gender':gender, 'Grade Overall': grade}

finalgrade=pd.DataFrame(gradesheet)
print(finalgrade)

# Try to change the row index (to let it instead of counting from Row 0)...

row_labels = ['Class 1', 'Class 2','Class 3', 'Class 4', 'Class 5', 'Class 6']

# Specify row labels of finalgrade
finalgrade.index = row_labels

# Print cars again
print(finalgrade)

# Now let's practice a second method of loading some data: importing data from a random place in your computer...

grade = pd.read_csv("/Users/zdong/Docs/schoolgrade.csv", index_col = 0)  # this is the way to import
                                                                         # files inside your Mac
#example of importing files inside your WINDOWS
#grade = pd.read_csv("C:/Users/zdong/Docs/schoolgrade.csv", OPTIONS)

print(grade)

print(grade[2:7])  # importing the third until the seventh student


# *************************************************************************************************************
# Finding locations in Python using loc, iloc, ix and query
# These are the four most common types of location finder
# A more comprehensive reading of location finder is available in the link below (optional reading):
# http://pandas.pydata.org/pandas-docs/stable/indexing.html#different-choices-for-indexing
# *************************************************************************************************************

df = pd.DataFrame({'A':['m', 'n', 'o','p'], 'B':[54, 67, 89, 72], 'C':[True, False, False, False]},
                  index=[100, 200, 300, 500])
print(df)

# demo of four location finders, you may want to try them one-by-one, and examine how each line of code translates
# to its respective outcome

# loc finder
print(df.loc[500])

# iloc finder
print(df.iloc[2])

# ix finder
# The use of ix is illustrated here: http://stackoverflow.com/questions/31593201/pandas-iloc-vs-ix-vs-loc-explanation
# How to use ix specifically has been left as a homework problem.

# query finder
print(df.query('B<80'))

# *************************************************************************************************************
# Exercise 2.7 In your words, explain briefly how loc, iloc and query works. This answer must be posted to
# 'Using Chapter 2' Issue tab if you are enrolled in this course.
# *************************************************************************************************************

# *************************************************************************************************************
# Exercise 2.8 Using the schoolgrade.csv file (this is available in our Chapter 2 folder on Github), using the
# location finders to produce some meaningful outputs. The outputs must demonstrate your understanding of all
# four finders, and this is also an opportunity for you to practice uploading files from your local drives.
# *************************************************************************************************************

import numpy as np
df2 = pd.DataFrame({'a': list('aabbccddeeff'), 'b': list('aaaabbbbcccc'), 'c': np.random.randint(5, size=12),
                   'd': np.random.randint(9, size=12)})

print(df2[df2.a.isin(df2.b)]) # What did this do? Think about it...

print(df2[~df2.a.isin(df2.b)]) # ~ means a negative turn... which means getting those rows where column 'a'
                               # does not have the values presented in column 'b' out.

print(df2.query('a in b and c < d')) #combine with other types of expressions

# *************************************************************************************************************
# Exercise 2.9: Using no more than 1 line of code, query the rows in the dataset 'ex2_9' below where column 'a'
# has values from column 'b' AND the value of column 'c' is smaller than the value of column 'd'.
# *************************************************************************************************************

#Preparatory Codes
ex2_9 = pd.DataFrame({'a': list('aabbccddeeffbcdefd'), 'b': list('aaaabbbbccccdabccd'),
                      'c': np.random.randint(5, size=18), 'd': np.random.randint(9, size=18)})
print(ex2_9)
