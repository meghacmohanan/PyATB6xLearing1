
class BaseTest:
    def run_test(self):
        print("Running Base-Parent Test-Generic")

class LoginTest(BaseTest):
    def run_test(self):
        print("Running Login Test-Personal")

t= LoginTest()
t.run_test()