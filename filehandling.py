#reading a file
file = open("password.pub", 'r')

print(file.read())

#Writing a new file
newfile = open("demo.txt", 'w')
newfile.write('Hello World!')


#appending a file
newfile = open("demo.txt", 'a')
newfile.write("This is a demo file")


#OPENING OF PHOTOS(BINARY FILES)
f = open("car.jpg", 'rb')

f1 = open('pic.jpg', 'wb')

for photo in f:
    f1.write(photo)

