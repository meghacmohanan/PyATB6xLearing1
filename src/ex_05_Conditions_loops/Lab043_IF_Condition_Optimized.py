"""
Write a program to take a user age and
let him know if he can go to clud

Logic buidling formaula
i/p = age, int
o/p- String(result)
"""


age= float(input("Enter the age: ").strip())
if age<=0 or age>120:
    print("Enter a valid age")
else:
    if age >= 21:
        print("Yes, ca go to club")
    else:
        print("No, cant go to club")

# step - check for the

