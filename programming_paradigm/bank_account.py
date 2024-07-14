class BankAccount:
  def __init__(self, initial_balance=0.0):
    self.__account_balance = initial_balance
  def deposit(self, amount):
    if amount > 0:
      self.__account_balance += amount
      print("Deposited ${}. New balance: ${}".format(amount, self.__account_balance))
    else:
      print("Invalid deposit amount.")
  def withdraw(self, amount):
    if amount > 0 and amount <= self.__account_balance:
      self.__account_balance -= amount
      print("Withdrew ${}. New balance: ${}".format(amount, self.__account_balance))
    else:
      print("Invalid withdrawal amount or insufficient balance.")
  def display_balance(self):
    print(f"Current Balance: ${self.account_balance:.2f}")
account = BankAccount(initial_balance=100.0)
account.display_balance()
account.deposit(50.0)
account.withdraw(20.0)
account.withdraw(150.0)
account.display_balance()

