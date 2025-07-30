class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance
        
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")   
    

    # do wyboru opcja:

    #def withdraw(self, amount):
     #   if amount > self.__balance:
      #      print("Insufficient funds")
       # else:
        #    self.__balance -= amount
         #   print("Withdrew:", amount, "New balance:" , self.__balance)

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount} New balance:  {self.__balance}")
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance

account = BankAccount("Jan Nowak", 1000)
#input_amount = input(f"Podaj kwotę wpłaty, mniejszą niż saldo({account.get_balance}): ")
#output_amount = float(input)

account.deposit(300)
account.withdraw(500)
account.deposit(600)
account.withdraw(1000)
print("---")
print(f"Saldo końcowe: {account.get_balance()}")
print("---")