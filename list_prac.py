# A list of three numbers
numbers = [1, 2, 3]
print(numbers)

#empty list
my_list =[]

#list with mixed data types
my_list = [1, "Hello", 3.4]
print(my_list)

languages = ["Python", "Swift", "C++", 'Java', 'Rust', 'R']

#access item at index 0
print(languages[0])
print(languages[-1])
#changing the item to C
languages[2] ='C'
languages.append('C++')
print(languages)
#deleting the second item
del languages[2]
print(languages)

#slicing in python
slice_demo = ['p','r','o','g','r','o','g','r','a','m','m','i','n','g']

#items from index 2 to 4
print(slice_demo[2:5])
print(slice_demo[5:])
print(slice_demo[:])

integers = [21, 34, 54, 23]

print("Before append:", integers)
#using append method
integers.append(32)
print("After append", integers)


prime_numbers = [2,3,5]
print("List 1:", prime_numbers)

even_numbers = [4,6,8]
print("List 2:", even_numbers)
# Join two lists
prime_numbers.extend(even_numbers)

print("List after append:", prime_numbers)

#iterating through the list
languages = ["Python", "Swift", "Swift", "C++"]
for language in languages:
    print(language)