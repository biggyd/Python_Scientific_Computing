#Chapter 1.1 Python as a calculator
#Python can do common calculating problems, just like R.

#For example,

print (5 / 8)
print (7 + 10)
print (2 * 6)

# Exponentiation
print(4 ** 2)

# Modulo
print(18 % 7)

# Exercise 1.1 Little Pig invests 1000 dollars in BOA with an annual rate of 2%, what will little pig gets by pulling
# all monies from the bank after 8 years?

# Of course, you may want to create a variable to store some values
pig1 = 100

# Print out savings
print (pig1)

# Create a variable for the population of pigs
pig_pop = 100

# Each pig creates two offsprings
factor = 2

# How many pigs do we end up after 1 year, assuming zero mortality and morbidity?
result = pig_pop * (factor+1)

# Print out result
print(result)


# Python also accepts string variable, which is a text message quoted in single quotation mark
# or double, also boolean variable which is a TRUE/FALSE statement...

passcode = 'piggy is cute'
# Create a variable profitable
piggy_is_cute = True
# Note: Only True and False are accepted, TRUE, true, FALSE, falsE, false, etc. will NOT be accepted
print (passcode)
print (piggy_is_cute)

# Several variables to experiment with
savings = 100
factor = 1.1
pig2 = "piggy is"
desc = " very"
desr = " cute"

# Assign product of factor and savings to year1

year1 = savings*factor

# Print the type of year1

print(type(year1))
# Assign sum of desc and desc to doubledesc

words = pig2+desc+desc+desc+desr
# Print out doubledesc
print(words)

#What if...
print("Alice is" + desc * 3 + " cute!")

# see how did I play around with this?
