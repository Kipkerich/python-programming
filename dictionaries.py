capital_city = { "Nepal": "Kathmandu", "Italy": "Rome",
                "England": "London"}

print(capital_city)

numbers = {1: "One", 2: "Two", 3: "Three"}

print(numbers)

#Adding elements to a python dictionary

print("Initial Dictionary:", capital_city)

capital_city["Japan"] = "Tokyo"

print("Updated Dictionary:", capital_city)

#Accessing elements from dictionary
print(capital_city["England"])

#Deleting elements in  a dictionary
student_id = {111: "Eric", 112:"Kyle", 113:"Butters"}

print("Initial Dictionary: ", student_id)


del student_id[111]

print("Updated Dictionary ", student_id)

#Membership Test for Dictionary Keys

squares = {1:1, 3:9, 5:25, 7:49, 9:81}
print(1 in squares)
print(2 not in squares)
print( 49 in squares)

#iterating through a dictionary
for i in squares:

    print(squares[i])