
class BaseClass:

    driver= "Chrome"
    driver2= "ENV"
    def setup(self):
        print("Base Setup with browser and env")
class LoginTest(BaseClass):
    def run(self):
        self.setup()
        print("Running login test in :-> " , self.driver)

org_obj=LoginTest()
org_obj.run()