#This is purely a replicate from the panda helpfile...
#Source: http://pandas.pydata.org/pandas-docs/stable/options.html

#*****************************************************************************************************************
#Motivation: sometimes we encounter problems of importing East Asian languages as Python data, but python treats
#those characters into 2 alphabets...
#*****************************************************************************************************************

# Example
df = pd.DataFrame({u'国籍': ['UK', u'日本'], u'名前': ['Alice', u'しのぶ']})
print(df)

# What to do?

pd.set_option('display.unicode.east_asian_width', True)
print(df)

