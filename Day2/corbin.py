class BankAccount: 
   def __init__(self, int_rate, balance):
      # assign our parameters accordingly
      self.int_rate = int_rate
      self.balance = balance

   def deposit(self, amount):
      self.balance += amount
      return self

   def withdraw(self, amount):
      self.balance -= amount 
      return self

   def display_account_info(self):
      return (f"Balance: {self.balance}")

   def yield_interest(self):
      if self.balance > 0:
         self.balance = self.balance + (self.int_rate * self.balance)
      return self

class User:    
   bank_name = "First National Dojo"

   def __init__(self, name, email):
      self.name = name
      self.email = email
      self.account = BankAccount(int_rate=0.1, balance=0)

   # deposit
   def make_deposit(self, amount):    # takes an argument that is the amount of the deposit
      self.account.balance += amount    # the specific user's account increases by the amount of the value received
      return self

   # withdrawal
   def make_withdrawal(self, amount):
      self.account.balance -= amount
      return self

   # display
   def display_user_balance(self):
      print(f"User: {self.name}, Balance {self.account.display_account_info()}")
      return self.account.balance


# ACCOUNTS
guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
murphy = User("Murphy Merf", "murphy@merf.aol")

monty.make_deposit(100).make_deposit(500).make_deposit(400).make_withdrawal(900).display_user_balance()
guido.make_deposit(100).make_deposit(500).make_withdrawal(100).make_withdrawal(100).make_withdrawal(150).make_withdrawal(150).display_user_balance()
murphy.make_deposit(100).make_deposit(500).make_deposit(1400).make_withdrawal(900).display_user_balance()