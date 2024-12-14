my_list = []

new =[10, 20, 30, 40]
#adding mutiple values using append()
for values in new:
    my_list.append(values)

print(my_list)

#inserting a value at the second position
my_list.insert(1, 15)

print(my_list)

#using extend method to insert mutiple values

numbers = [50, 60, 70]

my_list.extend(numbers)

print(my_list)
#sorting the list in ascending order
my_list.sort()
print(my_list)

#find and print the index of 30
index_of_30 = my_list.index(30)
print(index_of_30)