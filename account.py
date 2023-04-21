class Account:
    """
   This class creates an object that stores a name and monetary balance,
   with various methods to allow editing of balance and reading of both value
    """
    def __init__(self, name):
        """
        Initializes class attributes
        :param name: This is the name of the account holder
        """
        self.__account_name: str = name
        self.__account_balance: float = 0

    def deposit(self, amount: float):
        """
        Deposits a positive real value of money into the balance

        :param amount: Amount of money to deposit
        :return: True if desired deposit amount is positive, else False
        :raise TypeError: raises if input is not numerical
        """
        if not isinstance(amount, (float, int)):
            raise TypeError
        if amount > 0:
            self.__account_balance += amount
            return True
        return False

    def withdraw(self, amount: float):
        """
        Withdraws a positive real value of money from the balance

        :param amount: Amount of money to withdraw
        :return: True if desired deposit amount is positive and less than the balance, else False
        :raise TypeError: raises if input is not numerical
        """
        if not isinstance(amount, (float, int)):
            raise TypeError
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def get_balance(self):
        """
        :return: Amount of money in the account
        """
        return self.__account_balance

    def get_name(self):
        """
        :return: Name of the account holder
        """
        return self.__account_name

