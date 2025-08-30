# bank_account.py
from datetime import datetime

class BankAccount:
    def __init__(self, account_number: int, balance: float = 0.0):
        self.account_number = account_number
        self.balance = float(balance)
        self.history = []  # list of (timestamp, type, amount, balance_after)

    def _record(self, ttype: str, amount: float):
        self.history.append((datetime.now().isoformat(), ttype, amount, self.balance))

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        self._record("DEPOSIT", amount)
        return self.balance

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount
        self._record("WITHDRAW", amount)
        return self.balance

    def get_balance(self):
        return self.balance

    def get_history(self):
        # return a copy so callers don't mutate internal list
        return list(self.history)
