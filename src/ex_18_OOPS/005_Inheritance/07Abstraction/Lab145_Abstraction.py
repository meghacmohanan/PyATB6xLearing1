
class Mathclass:
    def add(self,a,b):
        return a+b
    def add(self,a,b,c=3):
        return a+b+c
m= Mathclass()
a=m.add(1,2)
b=m.add(10,10,20)
print(a)
print(b)
