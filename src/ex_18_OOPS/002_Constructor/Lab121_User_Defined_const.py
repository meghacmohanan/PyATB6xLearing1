# What the oupput

class Person:
    def __init__(self):
        print("Let's enter the detail of an employee  with name, age, phone number and Occupation")
        self.name=input("Enter your name: ")
        self.age=input("Enter your age: ")
        self.phone_number=input("Enter your phone number: ")
        self.occupation=input("Enter your occupation: ")

    def display_values(self):
        print("Name: ",self.name, "age :", self.age,
              "phone number: ", self.phone_number, "occupation: ", self.occupation)

employee=Person()
employee.display_values()


