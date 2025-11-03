# Q - Create a function which will take a positive number from the user and perform square of the number?
#
# i/o = 3
#
# o/p = 9


def sqare_of_number(number):
    square=  number**2
    print("The square is",square)


sqare_of_number(int(input("Enter a number: ")))