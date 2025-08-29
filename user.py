# user.py
import hashlib
from typing import Dict
from bank_acc import BankAccount

class User:
    def __init__(self, name: str, pin: str):
        self.name = name
        self.pin_hash = self._hash_pin(pin)   # store hash instead of plain pin
        self.accounts: Dict[int, BankAccount] = {}

    def _hash_pin(self, pin: str) -> str:
        """Convert PIN into a SHA-256 hash."""
        return hashlib.sha256(pin.encode()).hexdigest()

    def check_pin(self, pin: str) -> bool:
        """Verify entered PIN against stored hash."""
        return self._hash_pin(pin) == self.pin_hash

    def add_account(self, account: BankAccount):
        """Attach a BankAccount object to this user."""
        self.accounts[account.account_number] = account

    def get_account(self, account_number: int):
        """Retrieve account by account number."""
        return self.accounts.get(account_number)

    def list_accounts(self):
        
        return list(self.accounts.keys())
