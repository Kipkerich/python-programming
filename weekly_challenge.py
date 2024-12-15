#Week two challenge
#a program that accepts user input to create a list of integers
list = []

update =[2,5,7,8,9]
list.extend(update)
print(list)

#sum of all the integers in the list.
total = sum(list)
print(total)


#Week three challenge
#Large power

def large_power(base, exponent):
    
    result = base ** exponent
    if result > 5000:
        return True
    return False

print(large_power(300,800))

#divisible by ten

def divisible_by_ten(num):
    if num % 10 == 0:
        return True
    return False

print(divisible_by_ten(45))