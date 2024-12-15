#function is a block of code designed to perform a specific task

#built-in functions are prededined functions eg print()
# user-defined functions are created by the user

# Exampple of a user defined function
#function definition
def greet(name):

    return f"Hello , {name}"
#function call
print(greet("Alice"))

"""
Key Components of a function;
1. Function name- Should be descriptive and follow naming conventions
2 Parameters - Variables passed into the function
3. Docstring - An optional description of what the function does
4. Return statement - Outputs a value from the function(optional)

"""
#Positional arguments
def add(a, b):
    return a + b
print(add(3, 5))

#Default arguments
def greet(name = "Guest"):
    return f"Hello  , {name}!"

print(greet())
print(greet("World"))

#keyword arguments
def introduce(name, age):
    return f"My name is {name} and I'm {age} years old."

print(introduce(age=25, name="Bob"))

#returning values
def square(number):
    return number ** 2

result = square(4)
print(result)

#lamda function for adding two numbers
add = lambda x,y: x + y
print(add(3,5))

#Using lamda with map()
numbers = [1,2,3,4]
squares = list(map(lambda x: x**2, numbers))
print(squares)

#recursive functions
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
print(factorial(5))