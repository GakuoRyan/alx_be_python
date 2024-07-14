import sys
from bank_account import BankAccount

class BankAccount:

    def __init__(self, account_balance=0):
        self.account_number = BankAccount.account_number
        self.account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount
            print(f"Withdrew ${amount}")
        else:
            print("Insufficient funds")

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")
