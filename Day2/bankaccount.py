class BankAccount:
    def __init__(self, name, int_rate, balance): 
        self.name = name
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
        print("{}'s Balance: ${}" .format(self.name, self.balance))
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

aaron = BankAccount("Aaron Nguyen", 0.1, 0)
cassidy = BankAccount("Cassidy Smith", 0.5, 100)
aaron.display_account_info().deposit(100).deposit(50).deposit(100).withdraw(545).display_account_info()
print("")
cassidy.display_account_info().deposit(500).withdraw(50).withdraw(50).deposit(500).withdraw(100).withdraw(100).yield_interest().display_account_info()

# Print instances?