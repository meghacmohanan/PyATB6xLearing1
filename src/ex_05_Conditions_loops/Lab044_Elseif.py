
"""
Find a number is even or not
"""
num= int(input("Enter a number: "))

if(num>=0):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
else:
    print("Negative number")

# we can wrote short one-liner condtition using ternary operator
print("----------------------")
if(num>=0):
    print("Even" if num % 2 == 0 else "Odd")

else:
    print("Negative number")
