import os
file = open("password.pub", 'r')

print(file.read())

#Writing a new file
newfile = open("demo.txt", 'w')
newfile.write('Hello World!')

