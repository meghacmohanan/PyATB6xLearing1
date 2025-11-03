"""
Given a Number a number you need to calculate the factorial of that number
n = 5

Fact = 5×4×3*2*1 = 120

Fact = 0 → 1,
"""

fact =1
num= int(input("Enter a first number: "))
if num > 1:
    while num > 1:
        fact = fact * num
        num = num - 1
    print(fact)
elif num == 0:
    print("Factorial of 0 is 1")

else:
    print("negative number")

print("*****************- IF_Loop*********")


fact1= 1
num= int (input("Enter a second number: "))

if num<0:
    print("Factorial is not defined ")
if num==0:
    print("Factorial of second number is one")
else:
    for i in range(1,num+1):
        fact1= fact1*i
    print("factorial of",num,"is",fact1)

