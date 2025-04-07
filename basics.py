
#List of student names
names = ["Todd", "Jake", "Bill", "Sally", "Anna"]
print(names[1])

print(names[2:])


print(names[:2])


print(names[-4])

print(names[-3:])


#Splitting of  values in an array

ssn = "123-12-1234"

ssnList = ssn.split("-")
print(ssnList)

b = "a,b,c,d,e,f,g"

print(b.split(","))


#Joining an array

names = ["Todd", "Jake", "Bill", "Sally", "Anna"]
print(" ".join(names))  

b = "a" ,"b","c","d","e","f","g"
print(" ".join(b))