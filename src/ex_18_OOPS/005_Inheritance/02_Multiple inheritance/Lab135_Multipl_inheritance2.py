
class Father1:
    def money(self):
        print("Money 1")

class Father2:
    def money(self):
        print("Money 2")
class Child(Father2, Father1):
    def run(self):
        self.money()
        print("Testcase Running")
C= Child()
C.run()