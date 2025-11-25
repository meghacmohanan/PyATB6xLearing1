
a= 10  # gloabal varaible

class Person:
    b= 11 # Instance variable

    def print_info(self):
        c= 3 # local varaible
        print("Global varaible is: ", a)
        print("Local Varaible: ", c)
        print("Instance Variable: ", self.b)

person=Person()
person.print_info()

# print(b)
# print(c)