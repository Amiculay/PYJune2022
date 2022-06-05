class User:
    def __init__(self, name):
        self.name = name
        self.balance = 0
    
    def make_deposit(self, amount):
        self.balance += amount
        return self
    
    def make_withdrawal(self, amount):
        self.balance -= amount
        return self
    
    def display_user_balance(self):
        print("{}'s balance: ${}" .format(self.name, self.balance))

    def make_transfer(self, amount, user):
        self.balance -= amount
        user.balance += amount
        self.display_user_balance()
        user.display_user_balance()


aaron = User("Aaron Nguyen")
corbin = User("Corbin Crawford")
cassidy = User("Cassidy Smith")

aaron.make_deposit(100).make_deposit(500).make_deposit(50).make_withdrawal(150).display_user_balance()
corbin.make_deposit(1000).make_deposit(250).make_withdrawal(200).make_withdrawal(50).display_user_balance()
cassidy.make_deposit(2000).make_withdrawal(150).make_withdrawal(100).make_withdrawal(50).display_user_balance()
aaron.make_transfer(100, cassidy)