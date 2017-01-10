#*************************************************************************************************************
#Chapter 1.2 Python Data Type Transformation
#*************************************************************************************************************

# using int(), str(), float() can change the data to the type desired.
pig3 = "2.85"

#*************************************************************************************************************
#Exercise 1.2 Search and describe the difference between float, integer and string variable.
# What is the data type of the variable 'pig3'? Write a line of code to convert it to float.
#*************************************************************************************************************


#Beware you cannot add a float or an integer directly after a string like:
# print("the number of pig is" + 3) <- you can try and see what error it creates...
# alternatively, you can do something such as
print("the number of pig is " + "3")


#*************************************************************************************************************
# List
#*************************************************************************************************************

#Create a list, using bracket

fruit1 = "apple"
fruit2 = "pear"
fruit3 = "melon"
fruit4 = "berries"

salad = [fruit1,fruit2,fruit3,fruit4]
print(salad) # also works for int and float, try that on your self

#Important: Python counts list from 0 as the first... for example:

print(salad[1])
print(salad[-1]) #What does "-1" here means?
#Combine data type??
# Example: area variables (in square meters)
hall = 6.25
kit = 11.0
liv = 40.0
bed = 17.75
bath = 11.50

# Adapt list areas
areas = [str("hallway"),hall, "kitchen", kit, str("living room"), liv, "bedroom",bed, str("bathroom"),bath]

#*************************************************************************************************************
# Exercise 1.3: Now calculate the sum of areas for the bedroom and bathroom for this house. It must be read as
# "The sum area of bedroom and bathroom is 29.25 square meters".
#*************************************************************************************************************

# Print areas
print (areas)
#Others also work, pay attention how 'a' worked in Example list 1(eg1)...
eg1 = [1 + 2, "a" * 5, 3]
print(eg1)
eg2 = [["a","bot"],[1,2]]
print(eg2)

#*************************************************************************************************************
# Data Slicing
# Let us create a list for Soc 300 grades, taught by Zhihang. Assumes Zhihang mixed letter grades and numeric
# grades in this case, but he ranked them...
#*************************************************************************************************************

Jerry = 102
Jason = 100
Mary = "A"
Molly = "A-"
Martin = "B+"
Shin = "C-"
Shook = 65
Foster = 51

grades = ["Jerry", Jerry, "Jason", Jason, "Mary", Mary, "Molly", Molly, "Martin", Martin,
          "Shin", Shin,"Shook", Shook, "Foster", Foster]
print (grades)

#*************************************************************************************************************
# Now let's slice the students getting grade higher than B as "goodstudent", and lower as "badstudent"
#*************************************************************************************************************
goodstudent=grades[0:10]
badstudent=grades[10:16]
print(goodstudent)
print(badstudent)
#*************************************************************************************************************
# Here, python only counts the 1th (grades[0]) to the 10th variable (grades[9]) in grades[0:10]
# so grades [0:10] actually does not count grades[10] (which is the 11th variable). This needs extra caution.
#*************************************************************************************************************
#You can also replace the value, for example, let's say the grade for Foster is actually 81
grades[-1]= 81
print(grades)
# can also extend a list by appending a list to the list

grades_new = grades + ["Piggy", "A++"]
print(grades_new)
# and you want to kick out the student who fails (got lower than C-), so
del(grades_new[-6:-4])
#*************************************************************************************************************
# Exercise 1.4:Here, an alternative way to work on slicing is to use list[:X] as to slice the list from the
#  1st variable to the Xth variable. Using the grades data to slice the student getting passing grades or
#  better as a list 'okstudent' (passing means C- or better)... create another list called 'notokstudent' by
#  using only one number and one list statement for those who got worse than C-. Guess how to do it?
#*************************************************************************************************************
#You can also slice the slice from the list, go back to our simple eg2 list, what does the following code produced?
print(eg2[1][1])


