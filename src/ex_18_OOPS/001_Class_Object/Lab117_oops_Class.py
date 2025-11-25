
class student:
    #Attributes

    name= None
    age= None
    location= None
    color= None
   #Methods
    # These are called methods- means methods are within the class
    def talk(self):
        print("I can talk")
    def sleep(self,name): # Argument with no return
        print("I am a Method!")
        print("Sleep", name)
    def sleep2(self,name):
        print("I am another Method!")
        return None

    def walk(self):
        print("I can walk")
    def walk_return(self,name):
        return "I am walking"

#This is called functions - means the functions are outside the class
def outside():
    print("I am outside")

#Create an object of a class

object = student()
print(object.name)
object.talk()

