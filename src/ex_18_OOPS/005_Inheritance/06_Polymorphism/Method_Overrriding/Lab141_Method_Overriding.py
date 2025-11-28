
class TestSuite():
    def info(self):
        print("Test Suite information")
class BaseTest(TestSuite):
    def setUp(self):
        print("Setup BaseTest")
    def run_test(self):
        print("Running Base Test")
class LoginTest(BaseTest):
    def run_test(self):
        print("Running Login Test")
class APITest(BaseTest):
    def run_test(self):
        print("Running API Test")

t= LoginTest()
t.run_test()

s= APITest()
s.run_test()