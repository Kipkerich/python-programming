
#Inheritance - classes can inherit attributes and methods from other classes.
class Vehicle:
    def __init__(self, wheels):
        self.wheels = wheels

class Car(Vehicle):
    pass

car = Car(4)
print(car.wheels)

# polymorphism -Derived classes can behave differently 
# for the same method inherited from a base class
class Dog:
    def speak(self):
        return "Woof!"
    
class Cat:
    def speak(self):
        return "Meow!"
    
#polymorphism in action
for animal in [ Dog(), Cat()]:
    print(animal.speak())


#Encapsulation - his is the practice of keeping attributes and methods private to prevent 
# unwanted interference from outside the class.

class SecretStash:
    def __init__(self):
        self.__choclates = 10 #Private attribute

    def take_choclate(self):
        if self.__choclates > 0:
            self.__choclates -= 1
            print("One choclate taken!")
        else:
            print("No cholcate left")

stash = SecretStash()
stash.take_choclate()        