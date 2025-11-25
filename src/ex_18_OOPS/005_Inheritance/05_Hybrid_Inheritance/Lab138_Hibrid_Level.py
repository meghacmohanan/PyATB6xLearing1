
class A:
    def a_method(self):
        print("This is 'A' method")
class B:
    def b_method(self):
        print("This is 'B' method")
class C(A,B):
    def c_method(self):
        print("This is 'C' method")

obj_c= C()
obj_c.a_method()
obj_c.b_method()
obj_c.c_method()
