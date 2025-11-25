

class Car:

    def __init__(self):
        self.public_car= "Alto"
        self.__private_car= "BMW"

    def private_car_fn(self):
        self.__private_car= "BENZ"
    def get_latest_private_car(self):
        return self.__private_car

obj_ref= Car()
print(obj_ref.public_car)
obj_ref.private_car_fn()
print(obj_ref.get_latest_private_car())

