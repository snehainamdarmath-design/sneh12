class bankAccount:
    def __init__(self,balance):
        self.__balance=balance

    def withdraw(self,amount):
        if amount>0:
            self.__balance-=amount
    def deposit(self,amount):
             if amount>0:
                 self.__balance+=amount       
          
    def get_balance(self):
        return self.__balance
account= bankAccount(10000)
account.withdraw(5000)
account.deposit(3000)
print(account.get_balance())