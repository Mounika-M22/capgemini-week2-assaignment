#  Design a `BankAccount` class with `deposit()` and `withdraw()` methods. Implement logic to prevent overdraft.
from abc import ABC,abstractmethod
class Bankaccount:
    def __init__(self,balance=4000):
        self.balance=balance
    @abstractmethod
    def Deposit(self,deposit_money):
        pass
    @abstractmethod
    def Withdraw(self,withdraw_money):
        pass
    
class Money_deposit(Bankaccount):
    def Deposit(self,deposit_money):
        self.deposit_money=deposit_money
        print(f'we are depositing {self.deposit_money}\n')
        self.balance+=deposit_money
        print(f"the balance is {self.balance}\n")


class Money_withdraw(Bankaccount):
    def Withdraw(self,withdraw_money):
        self.withdraw_money=withdraw_money
        if self.balance<self.withdraw_money:
            print('cant withdraw money because the balance is low\n')
        else:
            print(f'we are withdrawing {self.withdraw_money}\n')
            self.balance-=withdraw_money
            print(f"the balance is {self.balance}\n")

        
    

obj1=Money_deposit()
obj1.Deposit(500)
obj2=Money_withdraw()
obj2.Withdraw(6000)
