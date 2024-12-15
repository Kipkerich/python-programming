#list comprehension in python is a concise and elegant way to create and manipulate lists

#traditional loop
squares = []
for x in range(5):
    squares.append(x**2)
print(squares)

#list comprehension
squares = [x**2 for x in range (5)]
print(squares)

#list comprehension with a condition
even_numbers = [x for x in range(10) if x %2 == 0]
print(even_numbers)

#create a 3x3 matrix using nested list comprehensions
matrix = [[i*j for j in range(1, 4)] for i in range (1,4)]
print(matrix)