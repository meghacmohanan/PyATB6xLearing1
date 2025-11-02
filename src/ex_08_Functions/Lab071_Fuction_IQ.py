"""
Crea a programm to 
sum of 3 numbers with default value= 100, 2--, 300"""
#
#
# num1=int(input("Enter the first number: "))
# num2=int(input("Enter the second number: "))
# num3=int(input("Enter the third number: "))

num1= int(input("Enter the first number: "))
num2= int(input("Enter the second number: "))
num3= int(input("Enter the third number: "))

def sum_of_three_numbers(a,b,c):
    return num1+num2+num3


result1=sum_of_three_numbers()
result2=sum_of_three_numbers(30,40,50)
result3=sum_of_three_numbers(num1=1,num2=2)


print(result1)
print(result2)
print(result3)
