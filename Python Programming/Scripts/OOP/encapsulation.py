class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
