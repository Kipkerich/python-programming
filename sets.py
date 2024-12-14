#creating an empty set

empty_set = set()

#creating an empty dictionary

empty_dictionary = { }

print('Data type of empty set', type(empty_set))

print('Data type of empty dictionary', type(empty_dictionary))

numbers = {2, 4, 6, 6, 2, 8}
print('Initial set:',numbers)

#using add() method
numbers.add(32)

print('Updated set:', numbers)

#using update method
companies = {'Lacoste', 'Ralph Lauren'}

tech_companies = ['apple', 'google', 'apple']

companies.update(tech_companies)

print(companies)

languages = {'Swift', "Java", 'Python'}
print('Initial set:', languages)
#remove Java from a set

removedValue = languages.discard('Java')

print('Set after removal:', languages)

fruits = {'apple', 'peach', 'mango'}
#for loop to access each fruits

for fruit in fruits:

    print(fruit)

#set union in python

#first set
A = {1,3,5}

#second set
B= {0,2,4}

#performing union operation
print('Union using |:', A | B)

#performing union operation using union()
print('Union using union():',A.union(B))

#set intersection in python

#first set
A ={1,3,5}


#second set
B={1,2,3}
#performing intersection using &
print('Intersection using &:', A & B)

#performing instersection using intersection()
print('intersection using intersection():', A.intersection(B))

#set difference in python

#first set
A = {2,3,5}

#second set
B = {1,2,6}

print('using ^:', A ^ B)

print('Using symmetric_difference:',A.symmetric_difference(B))