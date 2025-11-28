
from abc import ABC, abstractmethod

class Gearbox(ABC):
    @abstractmethod
    def setGearbox(self):
        pass
class Engine:
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class Car(Gearbox, Engine):
    def start(self):
        print("Starting")
    def setGearbox(self):
        print("Setting Gearbox")
    def stop(self):
        print("Stopping")

    def go(self):
        self.start()
        self.setGearbox()
        self.stop()

tesla= Car()
tesla.go()
