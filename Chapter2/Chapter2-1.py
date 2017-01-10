#*************************************************************************************************************
#Chapter 2.1 Two Dimension Data set
#*************************************************************************************************************
#The numpy package transfer lists into arrays
import numpy as np
math = [91, 56, 72, 87, 99, 73, 44, 63, 21, 95]
np_math = np.array(math)
gpa = [3.8, 2.1, 2.8, 3.1, 4.0, 2.5, 2.9, 2.9, 0.8, 3.9]
np_gpa = np.array(gpa)

print(np_math[8])

#*************************************************************************************************************
# What is the difference between list and nparray?
# Good answer: http://stackoverflow.com/questions/176011/python-list-vs-array-when-to-use
# But, let's try our example
#*************************************************************************************************************

list1 = [1, 2, 3]
list2 = [3, 4, 5]
np_array1 = np.array([1, 2, 3])
np_array2 = np.array([3, 4, 5])
print(list1+list2)
print(np_array1 + np_array2)

#*************************************************************************************************************
# Exercise 2.1: Based on the reading above, what is the difference between array of NumPy and list? Why in
# data science we use array?
#*************************************************************************************************************
