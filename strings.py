#creating a string using double quotes

string1 = "Python programming"

#creating a string using single quote

string1 = 'python programming'


print(string1[2])
print(string1[0:9])

#multiline string

message = """
Never gonna give up

Never gonna give up
"""
print(message)

str1 = "Hello world!"


str2 ="I love python."

str3 ="Hello world!"

#compare str1 and str2
print(str1 == str2)
print(str1 == str3)

greet = "Hello"
name = "Jack"

#using + operator
result = greet + name

print(result)

#iterating through greet string
for letter in greet:
    print(letter)

print(len(greet))

name = "Jacob"
country = "UK"

print(f'{name} is from {country}')