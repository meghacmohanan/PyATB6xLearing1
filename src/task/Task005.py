"""
Write a program to check the reponse in
an API program
and check
response= 404 - Failed API request
response= 200 ,Passed API request
"""


try:
    response = int(input("Enter a number: "))
    if response == 200:
        print("Passed API request")
    elif response == 404:
        print("Failed API request")
    else:
        print("Invalid respose")
except ValueError:
    print("Error: Please enter a valid input")


