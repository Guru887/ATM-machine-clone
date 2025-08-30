# main.py
from bank_account import BankAccount
from user import User
from atm import ATM

def main():
    atm = ATM()

    print("=== ATM System Setup ===")
    num_users = int(input("Enter number of users to create: "))

    for i in range(num_users):
        print(f"\n--- Creating User {i+1} ---")
        name = input("Enter your name (or 'q' to cancel user creation): ").strip()
        if name.lower() == "q":
            print("Skipping this user.")
            continue

        pin = input("Set a 4-digit PIN: ").strip()
        user = User(name, pin)

        while True:  # repeat until valid accounts are added
            num_accounts_input = input(f"How many bank accounts for {name}? (type 'undo' to retry user setup): ").strip()
            if num_accounts_input.lower() == "undo":
                print("Undoing account setup... restart user creation.")
                break  # go back and restart this user
            try:
                num_accounts = int(num_accounts_input)
            except ValueError:
                print("Enter a valid number.")
                continue

            if num_accounts <= 0:
                print("Must have at least 1 account.")
                continue

            for j in range(num_accounts):
                print(f"\n--- Creating Account {j+1} for {name} ---")
                acc_in = input("Enter account number (or type 'undo' to restart accounts): ").strip()
                if acc_in.lower() == "undo":
                    print("Undoing accounts... restart account creation.")
                    break  # break out of account loop
                try:
                    acc_num = int(acc_in)
                except ValueError:
                    print("Account number must be numeric.")
                    continue

                opening_balance_input = input("Enter opening balance (or 'undo'): ").strip()
                if opening_balance_input.lower() == "undo":
                    print("Undoing accounts... restart account creation.")
                    break
                try:
                    opening_balance = float(opening_balance_input)
                except ValueError:
                    print("Opening balance must be a number.")
                    continue

                account = BankAccount(acc_num, opening_balance)
                user.add_account(account)
            else:
                # only executed if no break inside the loop
                atm.add_user(user)
                break  # user created successfully
        # if loop breaks due to undo, user will restart creation process

    print("\n=== ATM System Ready ===")
    pin = input("Enter your PIN to login: ").strip()
    user = atm.authenticate(pin)
    if not user:
        print("Invalid PIN. Exiting.")
        return

    atm.run_session(user)


if __name__ == "__main__":
    main()
