# Q Q- Create a function which will take the 3 values from the user, which are length of the triangle.  side1, side2, side2
# i/p - int side1 == side2 =side3 → isoceles
# o/p = result in string - iso, eq, scalene

def triangle_type(side1, side2,side3):
    if side1>0 and side2>0 and side3>0:
        if side1+side2>side3 and side1+side3>side2 and side2+side3>side1:
            if side1==side2==side3:
                return "Equilateral"
            elif side1==side2 or side2==side3 or side3==side1:
                return "Isocean"
            else:
                return "Scalene"
        else:
            return "Not a triangle"
    else:
        return "Not a valid length"

a= int(input("Enter first side  of the triangle:"))
b= int(input("Enter second side of the triangle:"))
c= int(input("Enter third side of the  triangle:"))
result= triangle_type(a, b, c)
print(f"The triangle is classsified as: {result} ")