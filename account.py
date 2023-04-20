class Account:
    def __init__(self, name):
        self.__account_name: str = name
        self.__account_balance: float = 0

    def deposit(self, amount: float):
        if amount > 0:
            self.__account_balance += amount
            return True
        return False

    def withdraw(self, amount: float):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def get_balance(self):
        return self.__account_balance

    def get_name(self):
        return self.__account_name

