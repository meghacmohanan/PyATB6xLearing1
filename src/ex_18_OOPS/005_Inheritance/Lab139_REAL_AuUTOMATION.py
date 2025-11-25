
class BaseTest:
    def __init__(self, browser):
        self.browser=browser
    def startup(self, ):
        print(f"Staring Execution in {self.browser}")
class LoginTest(BaseTest):
    def run_test(self):
        self.startup()
        print("Running Login Test")
class SignUpTest(BaseTest):
    def run_test(self):
        self.startup()
        print("Runnging Sign Up Test")
t= LoginTest("Chrome")
t.run_test()
t=LoginTest("Firefox")
t.run_test()

s= SignUpTest("IE")
s.run_test()
