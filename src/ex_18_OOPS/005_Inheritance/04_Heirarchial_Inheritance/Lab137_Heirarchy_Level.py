
class BaseTest:
    def setup(self):
        print("setup from BaseTest")
class LoginTest(BaseTest):
    def run(self):
        print("Running Login Test")
class SignUpTest(BaseTest):
        def run(self):
            print("Running SignUp -RunTest")

LoginTest().setup()
LoginTest().run()
SignUpTest().setup()
SignUpTest().run()