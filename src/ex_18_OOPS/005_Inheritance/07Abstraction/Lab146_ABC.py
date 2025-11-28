from abc import ABC, abstractmethod
from tkinter.font import names


class Father:
    def __init__(self, name):
        print("Name is",name)

    def car(self):
        pass
class Child(Father):
    def car(self):
        print("New car-Audi")

ob= Child("Megha")
ob.car()