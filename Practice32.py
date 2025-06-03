class BankAccount:
    def __init__(self,pin,balance = 0):
        self.pin = pin
        self.balance = balance
    Bank_Name = "Allied Bank"
    Account_Holder = "Harris"

    def deposit_money(self,amount):
         self.balance += amount
         print(f"{amount} deposited to your account")
    
    def withdraw(self,amount):
        if self.balance > amount:
            self.balance -=amount
            print(f"{amount} withdrawn account")

        elif self.balance < amount or self.balance == 0:
            print("Balance Insufficent")
        
    def display_balance(self):
        print(f"Your balance is {self.balance}")

    @staticmethod
    def validate_amount(amount):
        return amount > 0
    
    @classmethod
    def display_info(cls):
        return f"Bank Name : {cls.Bank_Name}, Account Holder : {cls.Account_Holder}"
    
print(BankAccount.validate_amount(2000))
print(BankAccount.display_info())
acc1 = BankAccount(21032)
acc1.deposit_money(40000)
acc1.display_balance()
acc1.withdraw(20000)
acc1.display_balance()
acc1.deposit_money(1500)
acc1.display_balance()






