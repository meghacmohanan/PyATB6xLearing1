# What the oupput

class Dog:
    name= None
    height= None
    weight= None
    breed= None

    def __init__(self):
        print("I will be called")


    def bark(self):
        print("Barking")


    def sleep(self):
        print("Sleeping")


chow=Dog()
rencho= Dog()


print(chow.name)
print(rencho.name)
Dog.bark(self=chow)