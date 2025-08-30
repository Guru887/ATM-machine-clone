# atm.py
from user import User
from bank_account import BankAccount

class ATM:
    def __init__(self):
        self.users = {}  # key: pin -> User

    def add_user(self, user: User):
        if user.pin in self.users:
            print(f"Warning: replacing existing user with pin {user.pin}")
        self.users[user.pin] = user

    def authenticate(self, pin: str):
        return self.users.get(pin)

    def run_session(self, user: User):
        print(f"\nWelcome, {user.name}!\n")
        if not user.accounts:
            print("No accounts attached to this user. Exiting session.")
            return

        # Let user choose an account (if multiple)
        while True:
            print("Your accounts:", user.list_accounts())
            acc_in = input("Enter account number to use (or 'q' to quit): ").strip()
            if acc_in.lower() == 'q':
                print("Exiting. Bye!")
                return
            try:
                acc_no = int(acc_in)
            except ValueError:
                print("Enter a numeric account number.")
                continue
            account = user.get_account(acc_no)
            if not account:
                print("Account not found. Try again.")
                continue

            # account menu
            while True:
                print("\nATM Menu:")
                print("1. Check Balance")
                print("2. Deposit")
                print("3. Withdraw")
                print("4. Transaction History")
                print("5. Switch Account")
                print("6. Exit")
                choice = input("Enter choice: ").strip()

                try:
                    if choice == "1":
                        print(f"Available balance: ₹{account.get_balance():.2f}")
                    elif choice == "2":
                        amt = float(input("Enter deposit amount: ").strip())
                        account.deposit(amt)
                        print(f"Deposited ₹{amt:.2f}. New balance: ₹{account.get_balance():.2f}")
                    elif choice == "3":
                        amt = float(input("Enter withdrawal amount: ").strip())
                        account.withdraw(amt)
                        print(f"Withdrew ₹{amt:.2f}. New balance: ₹{account.get_balance():.2f}")
                    elif choice == "4":
                        hist = account.get_history()
                        if not hist:
                            print("No transactions yet.")
                        else:
                            print("Time\t\t\tType\tAmount\tBalanceAfter")
                            for rec in hist:
                                print(f"{rec[0]}\t{rec[1]}\t₹{rec[2]:.2f}\t₹{rec[3]:.2f}")
                    elif choice == "5":
                        break  # go back to account selection
                    elif choice == "6":
                        print("Thank you for using the ATM. Session ended.")
                        return
                    else:
                        print("Invalid choice. Try again.")
                except ValueError as e:
                    print("Error:", e)
