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

def sum_of_three_numbers(a=1,b=2,c=1):
    return a+b+c

result1=sum_of_three_numbers(30,40,50)
result2=sum_of_three_numbers(30,40)
result3=sum_of_three_numbers()
result4=sum_of_three_numbers(b=20,c=10)



print(result1)
print(result2)
print(result3)
print(result4)
#prin#t(result4)
