
"""Build a Test Framework with Encapsulation + Inheritance

🎯 Goal:
Create a simple automation structure that uses:
A BaseTest class for setup/teardown (Parent class)
A LoginTest class that inherits BaseTest (Child class
Encapsulate sensitive data (like credentials) as private variables

✅ Requirements:
Create a BaseTest class:
Has a protected variable _driver = "Chrome".
Method setup() prints "Launching browser: Chrome".
Method teardown() prints "Closing browser".
Create a LoginTest class that inherits BaseTest:
Has private variables for username and password.
Method run_test() that prints:
"Running login test with user: <username>".
Use encapsulation: access private vars only through a method (e.g., get_user()).
Create an object of LoginTest and call:
setup()
run_test()
teardown()"""



class BaseTest1:

    __driver= "Chrome"
    def setup(self):
        print(f"Launching browser:  {self.__driver}")
    def teardown(self):
        print("Closing browser")
class LoginTest1(BaseTest1):
    def __init__(self):
        self.__username= "admin"
        self.__password= "Pass123"


    def get_username(self):
        return self.__username

    def run_test(self):
        user= self.get_username()
        print(f"Running login test with user: {user}")


login_test = LoginTest1()
login_test.setup()
login_test.run_test()
login_test.teardown()

