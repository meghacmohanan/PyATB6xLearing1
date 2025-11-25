
class Car:
    name= None
    make= None
    model= None
    def  __init__(self, name, make, model):
        self.name = name
        self.make = make
        self.model = model
    def start_engine(self):
        print("Starting a car with name: ", self.name)
        print("Starting a car with Make: ", self.make)
        print("Starting a car with model: ", self.model)

lambo= Car("Lambo", "V6", 2023)
lambo.start_engine()

