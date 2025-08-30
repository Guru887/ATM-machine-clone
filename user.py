# user.py
from typing import Dict
from bank_account import BankAccount

class User:
    def __init__(self, name: str, pin: str):
        self.name = name
        self.pin = pin  # For learning project only; DO NOT store plain PINs in real apps
        self.accounts: Dict[int, BankAccount] = {}

    def add_account(self, account: BankAccount):
        self.accounts[account.account_number] = account

    def get_account(self, account_number: int):
        return self.accounts.get(account_number)

    def list_accounts(self):
        return list(self.accounts.keys())
