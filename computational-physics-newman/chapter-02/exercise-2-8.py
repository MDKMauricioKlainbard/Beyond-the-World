"""
Exercise 2.8: Suppose arrays a and b are defined as follows:

from numpy import array
a = array([1,2,3,4],int)
b = array([2,4,6,8],int)

What will the computer print upon executing the following lines?

a) print(b/a+1)
b) print(b/(a+1))
c) print(1/a)
"""

import numpy as np
a = np.array([1,2,3,4], int)
b = np.array([2,4,6,8], int)
print(b/a+1)
print(b/(a+1))
print(1/a)