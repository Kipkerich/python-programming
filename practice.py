# Takes string input and returns the reversed version
def resverse_string(s):
    return s[::-1]

print(resverse_string("Hello World"))


#Check for palindrome
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("racecar"))
print(is_palindrome("hello"))


#Fizz Buzz Problem

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
        
#Finding the second largest number in a list
def second_largest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort(reverse=True)
    return unique_numbers[1] if len(unique_numbers) > 1 else None

print('Second largest number:' , second_largest([10, 20, 4, 45, 99]))