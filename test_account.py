from pytest import *
from account import *


class TestAccount:
    def setup_method(self):
        self.account1 = Account('Fred')
        self.account2 = Account('Martha')
        self.account3 = Account('35')

    def teardown_method(self):
        del self.account1
        del self.account2

    def test_init(self):
        assert self.account1.get_name() == 'Fred'
        assert self.account1.get_balance() == 0

        assert self.account2.get_name() == 'Martha'
        assert self.account2.get_balance() == 0

        assert self.account3.get_name() == '35'
        assert self.account3.get_balance() == 0

    def test_deposit(self):
        assert raises(TypeError, self.account3.deposit, '1')
        assert self.account1.deposit(-10) == False
        assert self.account2.deposit(-1.1) == False

        assert self.account1.deposit(10) == True
        assert self.account1.get_balance() == 10

        assert self.account2.deposit(5.5) == True
        assert self.account2.get_balance() == 5.5

        assert self.account3.deposit(1000000) is True
        assert self.account3.get_balance() == 1000000

    def test_withdraw(self):
        self.account1.deposit(10)
        self.account2.deposit(10)
        self.account3.deposit(10)

        assert self.account1.withdraw(-10) is False
        assert self.account1.withdraw(11) is False
        assert self.account2.withdraw(-1.1) is False
        assert raises(TypeError, self.account3.withdraw, '1')

        self.account1.withdraw(5)
        assert self.account1.get_balance() == 5

        self.account2.withdraw(4.3)
        assert self.account2.get_balance() == 5.7

        self.account3.withdraw(10)
        assert self.account3.get_balance() == 0
