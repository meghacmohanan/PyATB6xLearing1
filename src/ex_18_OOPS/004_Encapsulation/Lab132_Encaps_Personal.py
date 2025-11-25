
class Home:
    def __init__(self):
        self.public_var = "Father"
        self.__private_var = "Baby"

    def mom(self):
        print(self.public_var)
        print(self.__private_var)
        self.__wife()

    def __wife(self):
        print("Private Wife")


obj_ref= Home()
obj_ref.mom()