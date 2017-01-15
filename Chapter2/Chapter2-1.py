#*************************************************************************************************************
#Chapter 2.1 Two Dimensional Data set
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


# Now, let's create a real 2-dimensional data, by combining the math score and gpa together
np_score = np.array([[91, 3.8],
                     [56, 2.1],
                     [72, 2.8],
                     [87, 3.1],
                     [99, 4.0],
                     [73, 2.5],
                     [44, 2.9],
                     [63, 2.9],
                     [21, 0.8],
                     [95, 3.9]])
print (np_score.shape)
print (np_score[1])
#*************************************************************************************************************
# Exercise 2.2 What does the output of np_score.shape described? Using np_score and bracket "[]" to find the GPA
# of the exact student with the 73 math exam score (which is a 2.5 GPA). (Hint: you may use more than one bracket).
#*************************************************************************************************************


# Print mean height (first column)
avg = np.mean(np_score[:, 0])
print("The Average of math exam grades is " + str(avg))

# Print median height. Replace 'None'
med = np.median(np_score[:, 0])
print("The Median of math exam grades is " + str(med))

# Print out the standard deviation on height. Replace 'None'
stddev = np.std(np_score[:, 0])
print("The Standard Deviation of math exam grades is: " + str(stddev))

# Print out correlation between first and second column. Replace 'None'
corr = np.corrcoef(np_score[:, 0], np_score[:, 1])
print("Correlation of math exam grades and overall GPA is: " + str(corr))

#*************************************************************************************************************
# Exercise 2.3 Calculate the median of GPA for the array np.score. Print the results (followed my example above).
#*************************************************************************************************************


