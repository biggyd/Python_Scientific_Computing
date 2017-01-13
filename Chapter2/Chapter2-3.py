# *************************************************************************************************************
# Chapter 2.3 Mapping and Dataframe via Panda
# *************************************************************************************************************
# *************************************************************************************************************
# Mapping (I): via Dictionary
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
# Exercise 2.6 Now try to delete the India and its mapped results from the dictionary using one line of code.
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
