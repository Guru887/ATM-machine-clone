# atm.py
from user import User

class ATM:
    def __init__(self):
        self.users = {}  # store by username instead of raw pin

    def add_user(self, user: User):
        if user.name in self.users:
            print(f"Warning: replacing existing user with name {user.name}")
        self.users[user.name] = user

    def authenticate(self, name: str, pin: str):
        """Authenticate by username and pin"""
        user = self.users.get(name)
        if user and user.check_pin(pin):   # check hashed pin
            return user
        return None

    def run_session(self, user: User):
        print(f"\nWelcome, {user.name}!\n")

        if not user.accounts:
            print("No accounts attached to this user. Exiting session.")
            return

        while True:
            print("\n--- Menu ---")
            print("1. View Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            choice = input("Select option: ")

            if choice == "1":
                for acc in user.accounts:
                    print(f"Account {acc.acc_num}: Balance = {acc.balance}")
            elif choice == "2":
                acc_num = input("Enter account number: ")
                amount = float(input("Enter deposit amount: "))
                for acc in user.accounts:
                    if acc.acc_num == acc_num:
                        acc.deposit(amount)
                        break
            elif choice == "3":
                acc_num = input("Enter account number: ")
                amount = float(input("Enter withdraw amount: "))
                for acc in user.accounts:
                    if acc.acc_num == acc_num:
                        acc.withdraw(amount)
                        break
            elif choice == "4":
                print("Thank you! Exiting session.")
                break
            else:
                print("Invalid option, try again.")
