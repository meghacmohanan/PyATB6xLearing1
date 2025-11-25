
class Bank:
    def __init__(self, balance, accountNumber):
        self.balance= balance
        self.__accountNumber= accountNumber
    def check_balance(self):
        return self.balance
    def deposit(self,amount):
        self.balance = self.balance + amount
        return self.balance
    def show_me_account_number(self, is_auth):
        if is_auth:
            print(self.__accountNumber)
        else:
            print("Not Allowed")

icic= Bank(10000, 435345345)
icic.deposit(100)
print(icic.balance)
icic.show_me_account_number(True)

