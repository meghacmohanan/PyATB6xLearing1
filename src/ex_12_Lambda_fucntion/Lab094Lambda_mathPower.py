import math
# num= int(input("Enter a number: "))
#
# output= lambda num: pow(num,2)
# print(output(num))
# # do this in one line

op2= lambda: math.pow(int(input("Enter a number: ")),3)()
print (op2)
