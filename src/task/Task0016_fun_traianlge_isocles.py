# Q Q- Create a function which will take the 3 values from the user, which are length of the triangle.  side1, side2, side2
# i/p - int side1 == side2 =side3 → isoceles
# o/p = result in string - iso, eq, scalene
# Refer Lab088 - Corrected version
def triangle_type(side1, side2,side3):
    if side1==side2==side3:
        print("The triangle is Equilateral")
    elif side1==side2 or side2==side3 or side3==side1:
        print("The triangle is Isocean")
    else:
        print("The triangle is Scalene")

a= int(input("Enter first side  of the triangle:"))
b= int(input("Enter second side of the triangle:"))
c= int(input("Enter third side of the  triangle:"))
result= triangle_type(a, b, c)
print(f"The triangle is classsified as: {result} ", result)
# Refer Lab088