
class Excelreader:
    @staticmethod

    def readExcelFile(self):
        print("Reading Excel File")
class MYSQLDBConnection:
    @staticmethod
    def readMySQLFile(self):
        print("Reading MYSQL read")

class TC1:
    def run(self):
        Excelreader.readExcelFile(self)
        MYSQLDBConnection.readMySQLFile(self)
        print("Finished")

t=TC1()
t.run()


