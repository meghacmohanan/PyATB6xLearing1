from dotenv import load_dotenv
import os


class VWOLoginPage:

    def __init__(self, email_args, passwrd_args):
        self.email= email_args
        self.passwrd= passwrd_args
    def login(self):
        load_dotenv()

        if self.email == os.getenv("USERNAME") and self.passwrd == os.getenv("PASSWORD"):
            print("Login Successful")
        else:
            print("Login Failed")

email1= input("Enter your Email:")
passwrd1= input("Enter your Password:")

vwo =VWOLoginPage(email1, passwrd1)
vwo.login()



