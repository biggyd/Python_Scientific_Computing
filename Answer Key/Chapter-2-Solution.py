#*************************************************************************************************************
#Chapter 2 Exercise Solutions
#*************************************************************************************************************
import numpy as np
# 2.1
# No need for a solution

# 2.2
# (2,10) means two columns 10 rows data...
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
print (np_score[5,1])

#2.3
med = np.median(np_score[:, 1])
print("The Median of GPA is " + str(med))
