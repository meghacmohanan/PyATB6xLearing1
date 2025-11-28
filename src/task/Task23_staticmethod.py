from src.task.Task22_Encapsulation_Inheriatance import BaseTest1


# - Create a framework base counter that counts test execution instances:



class baseCounter:
    counter = 0

    @staticmethod
    def excecutionCount():
        baseCounter.counter =baseCounter.counter + 1
        print(baseCounter.counter)

baseCounter.excecutionCount()
baseCounter.excecutionCount()