from ast import ExceptHandler


class Bank:
    def __init__(self, initial_amount=0.00):
        self.balance=initial_amount
        print(self.balance)



    def log_transaction(self,transaction_string):
        with open("transaction.txt","a") as file:
            file.write(f"{transaction_string}\t\t Balance:{self.balance}\n")
        


    
    def withdrawal(self,amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0
        if amount:
            self.balance = self.balance - amount
            self.log_transaction(f"Withdrawal Amount:{amount}")
        
    
    def deposit(self,amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0
        if amount:
            self.balance = self.balance +amount
            self.log_transaction(f"Deposit Amount:{amount}")
        

account = Bank(70.24)
while True:
    try:
        action = input("What Kind of action do you want to take??")
    except KeyboardInterrupt:
        print("\n Leaving the ATM")
        break


    if action in ["withdrawal","deposit"]:
        if action == "withdrawal":
            amount = float(input("how much do you want to withdrawal???"))
            print(amount)
            account.withdrawal(amount)
        else:
            amount = float(input("how much do you want to deposit???"))
            account.deposit(amount)
        print("Your balance is",account.balance)
    else:
        print("That is not a valid action Try Again")





            