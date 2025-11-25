# Create a Person class where we will have
# #five attributes and five behaviors.
# #Make sure that each type of function is used, and I want
# you to also create the print function, which will print all the instance variable values.

class Person:
    def __init__(self, name, age,gender, city,profession):
        self.name=name
        self.age=age
        self.gender=gender
        self.city=city
        self.profession=profession

    def walk(self,name):
        print(name + " is walking")
