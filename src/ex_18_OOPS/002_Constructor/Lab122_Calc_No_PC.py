
class Calc:
    def __init__(self):
        print("Default constructor")
    def sum(self,a,b):
        return a+b
    def substract(self,a,b):
        return a-b
    def mult(self,a,b):
        return a*b
    def div(self,a,b):
        return a/b


a=float(input("Enter value of a: "))
b=float(input("Enter value of b: "))
obj_ref= Calc()

output_sum=obj_ref.sum(a,b)
output_sub=obj_ref.substract(a,b)
output_mul=obj_ref.mult(a,b)
output_div=obj_ref.div(a,b)

print(output_sum,output_sub,output_mul,output_div)