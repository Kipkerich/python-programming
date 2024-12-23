#creating a new file
file =open ("new.txt", 'w')

#writing on the file
file.write("Welcome to this page")

#reading the file

try:
    file = open("new.txt", 'r')
    print(file.read())
except:
    print("File not found")
finally:
    print("Thank you")
