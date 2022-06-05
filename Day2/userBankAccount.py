class BankAccount:
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        self.balance -= amount
        return self

    def display_account_info(self):
        accountInfo = ("Balance: ${}" .format(self.balance))
        return accountInfo

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

class User:
    def __init__(self, name):
        self.name = name
        self.bank_account = BankAccount(0.5, 500)
    
    def make_deposit(self, amount):
        self.bank_account.deposit(amount)
        return self
    
    def make_withdrawal(self, amount):
        self.bank_account.withdraw(amount)
        return self
    
    def display_user_balance(self):
        print("User: {}, {}" .format(self.name, self.bank_account.display_account_info()))
        return self

    def make_transfer(self, amount, user):
        self.make_withdrawal(amount)
        user.make_deposit(amount)
        self.display_user_balance()
        user.display_user_balance()
        return self

# Add separate accounts?

aaron = User("Aaron Nguyen")
cassidy = User("Cassidy Smith")
aaron.display_user_balance()
aaron.bank_account.yield_interest()
aaron.display_user_balance().make_deposit(600).make_withdrawal(50).make_transfer(50, cassidy).make_deposit(500).display_user_balance()
cassidy.bank_account.yield_interest()
cassidy.display_user_balance()