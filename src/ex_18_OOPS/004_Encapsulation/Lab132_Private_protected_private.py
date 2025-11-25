
class TestExample:
    def __init__(self):
        self.driver="Chrome"
        self._enviornment="STAGING"
        self.__api__key= "test1234"

    def show(self):
        print(self.driver)
        print(self.__api__key)
        print(self._enviornment)


obj_ref= TestExample()
obj_ref.show()