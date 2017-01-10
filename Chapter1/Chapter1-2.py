#Chapter 1.2 Data Type and Data Transformation
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
