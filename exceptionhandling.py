try:
    file = open("test.txt", "r")
    print(file.read())
except:
    print("This file is not found")
finally:
    print("Thank you for your time")