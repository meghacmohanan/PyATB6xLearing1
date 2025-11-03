#write a pyhton program to clauclate
#area of a circle

# area= pi*r^2
#i/p= float
#o/p - string formated o/p of area

radius=float(input("enter radius :"))

area = 3.1498* pow(radius,2)
print("The area is ",area)

#STRING DATA FORMATING
print("Area of the circle is -> {area:.2f}")

print(f"Area of the circle is -> {area:.2f}")

