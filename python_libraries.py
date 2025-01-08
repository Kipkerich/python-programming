
"""NumPy arrays are a fundamental data structure in the NumPy 
library, which is a powerful tool for numerical computing in Python

 A NumPy array is similar to a Python list, but it has the following properties:

Homogeneous data type: All elements of a NumPy array must have the same data type, which is typically a numeric data type such as int or float.
Fixed size: The size of a NumPy array is fixed when it is created, and it cannot be changed without creating a new array.
Efficient: NumPy arrays are designed to be efficient for numerical operations, and they are implemented in C, which makes them faster than Python lists. 

"""


import numpy as np
import pandas as pd

a = np.array([1,2,3,4,5,6,7,8,9])
#Indexing
print("Index 0:",a[0])
print("Last index",a[-1])

#Slicing
print("Index 1 to 4:",a[1:4])

#Reshaping
r = a.reshape((3, 3))
print("Reshaped:",r)

b = np.array([[1,2,3],[4,5,6]])
print("2D array:",b)

c = np.array([1, 2, 3])
d = np.array([4, 5, 6])

#Addition
print("Sum:", c + d)

#Subtraction
print("Subtraction:",c -d)

#Multiplication
print("Multiplication:",c * d)

#Division
print("Division:",d/c)


data = {'name':['Alice', 'Bob', 'Charlie'],
         'age': [25, 30, 35],
         'city': ['New York', 'Los Angeles',
         'Chicago']}

df = pd.DataFrame(data)
print(df)

#Select a single column
print(df['name'])

#Select mutiple columns
print(df[['name', 'age']])

#Select rows by index
print(df.loc[0])

#Select rows by condition
print(df[df['age']>30])

#Add a new column
df['salary'] = [50000, 60000, 70000]
print(df)