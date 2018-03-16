"""
Module demonstrates template method pattern.
Problem:
1. Need to execute code in the base that class that can't be changed
2. Need to give possibility for subclasses to override part of base class behavior
"""
from abc import ABC, abstractmethod
import sys

class BankDeposit(ABC):
    
    __fee = 0.01
    
    def __init__(self, initial_amount, deposit_name):
        self._balance = initial_amount
        self._deposit_name = deposit_name
    
    def __str__(self):
        return "{0} deposit. Balance: {1}".format(self._deposit_name, self._balance)
    
    def __print_executing_code(self, frame):
        name = frame.f_code.co_name
        print("{0} {1}".format(self.__class__.__name__, name))
    
    # Template method
    def withdraw_money(self, amount_to_withdraw):
        self.__always_check_balance(amount_to_withdraw)
        real_sum = self.__always_take_fee(amount_to_withdraw)
        self.do_withdraw(real_sum)
    
    def __always_check_balance(self, amount_to_withdraw):
        self.__print_executing_code(sys._getframe())
        if amount_to_withdraw > self._balance:
            raise Exception("Can't withdraw: not enough money")
    
    def __always_take_fee(self, amount_to_withdraw):
        self.__print_executing_code(sys._getframe())    
        return (1.0 - self.get_fee())*amount_to_withdraw
    
    def get_balance(self):
        return self._balance
    
    def get_fee(self):
        return self.__fee
    
    @abstractmethod
    def do_withdraw(self, amount_to_withdraw):
        pass

class StateBankDeposit(BankDeposit):
    __fee = 0.1
    
    def do_withdraw(self, amount_to_withdraw):
        self._balance -= amount_to_withdraw

    def get_fee(self):
        return self.__fee        
        
class MafiaBankDeposit(BankDeposit):
    __fee = 0.05
    
    def do_withdraw(self, amount_to_withdraw):
        self._balance -= amount_to_withdraw
        
    def get_fee(self):
        return self.__fee
        

def main():  
    d1 = StateBankDeposit(100, "First State Deposit")
    d1.withdraw_money(10)
    print(d1)
    d2 = MafiaBankDeposit(100, "Billy Willy Deposit")
    d2.withdraw_money(10)
    print(d2)
    

if __name__ == "__main__":
    main()        