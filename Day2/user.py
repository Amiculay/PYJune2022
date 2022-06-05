class User:
    def __init__(self, name):
        self.name = name
        self.balance = 0
    
    def make_deposit(self, amount):
        self.balance += amount
    
    def make_withdrawal(self, amount):
        self.balance -= amount
    
    def display_user_balance(self):
        print("{}'s balance: ${}\n" .format(self.name, self.balance))

    def make_transfer(self, amount, user):
        self.balance -= amount
        user.balance += amount
        print("{}'s balance: ${}\n{}'s Balance: ${}" .format(self.name, self.balance, user.name, user.balance))


aaron = User("Aaron Nguyen")
corbin = User("Corbin Crawford")
cassidy = User("Cassidy Smith")

aaron.make_deposit(100)
aaron.make_deposit(500)
aaron.make_deposit(50)
aaron.make_withdrawal(150)
aaron.display_user_balance()

corbin.make_deposit(1000)
corbin.make_deposit(250)
corbin.make_withdrawal(200)
corbin.make_withdrawal(50)
corbin.display_user_balance()

cassidy.make_deposit(2000)
cassidy.make_withdrawal(150)
cassidy.make_withdrawal(100)
cassidy.make_withdrawal(50)
cassidy.display_user_balance()

aaron.make_transfer(100, cassidy)