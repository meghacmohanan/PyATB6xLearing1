"""Write a programm to calculate even and odd
using lamba"""

def find_even_odd(num):
    if num%2==0:
        return "Even"
    else:
        return "Odd"

number=int(input("Enter a number: "))
check_even_odd=lambda number:"Even" if number % 2 == 0 else "odd"
print(check_even_odd(number))