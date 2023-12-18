from datetime import datetime

class Transaction:
    """The tranzaction(action)"""
    def __init__(self, transaction_type, amount):
        self.timestamp = datetime.now()
        self.type = transaction_type
        self.amount = amount


class BankAccount:
    """The bank account where the tranzactions and the action below are stored."""
    def __init__(self):
        self.balance = 0
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(Transaction("Deposit", amount))

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(Transaction("Withdrawal", amount))
        else:
            print("Insufficient funds!")

    def get_balance(self):
        return self.balance

    def get_transaction_history(self):
        return self.transactions