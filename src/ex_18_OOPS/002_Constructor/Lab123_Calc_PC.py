
class Calc:
    a= None
    b= None

    def __init__(self, a, b):
        self.a=a
        self.b=b

    def sum(self):
        return  self.a+self.b
    def substract(self):
        return self.a-self.b
    def mult(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b


a=int(input("Enter value of a: "))
b=int(input("Enter value of b: "))
obj_ref= Calc(a,b)

output_sum=obj_ref.sum()
output_sub=obj_ref.substract()
output_mul=obj_ref.mult()
output_div=obj_ref.div()

print(output_sum,output_sub,output_mul,output_div)