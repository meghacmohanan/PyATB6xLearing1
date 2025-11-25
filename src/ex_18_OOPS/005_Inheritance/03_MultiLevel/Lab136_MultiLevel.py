
class TestSuit:
    def info(self):
        print("This is GrandFather class- Step1")
class BaseTest(TestSuit):
    def setup(self):
        print("This is Father class- Step2")
class UITest(BaseTest):
        def run(self):
            self.info()
            self.setup()
            print("This is Son class- Step3")

tes= UITest()
tes.run()