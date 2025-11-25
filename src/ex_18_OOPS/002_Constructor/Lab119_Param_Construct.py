
class Dog:
    name= None
    height= None
    weight= None
    breed= None

    def __init__(self,nameGiven,heightGiven):
        print("Parameterized Constructor")
        self.name = nameGiven
        self.height = heightGiven



    def bark(self):
        print("Barking")
        print(self.name)

    def sleep(self):
        print("who is sleeping: ", self.name)
    def talk(self):
        pass


print("Outside")
chow=Dog("chow", 120 )
chow.sleep()
#chow.bark()