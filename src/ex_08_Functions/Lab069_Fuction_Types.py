def test(name, age):
    print( name ,age)

test("Megha", 2)

# 1. built in functions
import math
result= max(2,3)
print(result)

#2. No returnt type and no paramenter
def greek():
    print("Hi")
greek()

#3 No return type but argument

def greet_by_name(name):
    print("Hello", name)
greet_by_name("Megha")

# not return type and with default parameter

def say_hello(name= "Megha"):
    print("Welcome", name)
say_hello()
say_hello("Megha Mohanan")

def mult_arg(name1= "A", name2= "B"):
    print(name1, name2)
mult_arg()
mult_arg(name1="John", name2= "Als")
mult_arg("Jacob", "Fa")
mult_arg("Meg")
