from traceback import print_tb


class VWOLoginPage:

    def __init__(self, email_args, passwrd_args):
        self.email= email_args
        self.passwrd= passwrd_args
    def login(self):
        if self.email == "megha@123" and self.passwrd == "1234":
            print("Login Successful")
        else:
            print("Login Failed")
email= input("Enter Email: ")
passwrd= input("Enter Password: ")

vwo =VWOLoginPage(email, passwrd)
vwo.login()



