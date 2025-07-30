class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance
        
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            #print(f"Deposited {amount}. New balance: {self.__balance}")
            return self.__balance
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
            #print(f"Withdrew: {amount} New balance:  {self.__balance}")
            return self.__balance
        else:
            print("Insufficient funds")
            

    def get_balance(self):
        return self.__balance

account = BankAccount("Jan Nowak", 1000)



while True:
    Menu_amount = input("Wpisz polecenie (wplata / wyplata / wyjscie): ")
    if Menu_amount == "wyjscie" :
        break
    elif Menu_amount == "wyplata" :
        input_amount = input(f"Podaj kwotę wypłaty, mniejszą niż saldo( {account.get_balance()} ): ")
        output_amount = float(input_amount)

        if output_amount > account.get_balance():
            print("---")
            print("Poucinam paluszki ;P ")
            print("---")
            break
        else :
            new_account = account.withdraw(output_amount)
            print(f"Saldo po wypłacie wynosi: {new_account} ")

    elif Menu_amount == "wplata":
        input_amount = input("Podaj kwotę wpłaty : ")
        output_amount = float(input_amount)
        new_account = account.deposit(output_amount)
        if output_amount <= 0:
            print("Nie można wpłacać ujemnych kwot, zera również...")
        else:
            print(f"Saldo po wpłacie: {new_account}")
    else: 
        print("Halo, halo co tu się odpierdziela?")
        break


#account.deposit(300)
#account.withdraw(500)
#account.deposit(600)
#account.withdraw(1000)
#print("---")
#print(f"Saldo końcowe: {account.get_balance()}")
#print("---")