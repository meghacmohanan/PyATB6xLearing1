from abc import ABC, abstractmethod

class ExcelReader(ABC):
    @abstractmethod
    def readFromExcel(self):
        pass

class Browser(ExcelReader):
    @abstractmethod
    def startBrowser(self):
        pass

    @abstractmethod
    def stopBrowser(self):
        pass

class TC1(Browser):

    def readFromExcel(self):
        print("Reading from Excel")
    def startBrowser(self):
        print("Starting Browser")
    def stopBrowser(self):
        print("Stopping Browser")
    def runTC1(self):
        self.startBrowser()
        self.readFromExcel()
        self.stopBrowser()


tc1= TC1()
tc1.runTC1()
