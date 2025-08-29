
from atm import ATM
from storage import save_data, load_data
from getpass import getpass

def main():
    atm = ATM()
    atm.users = load_data()  

    print("=== ATM System Ready ===")
    pin = getpass("Enter your PIN (or type 'new' to create user): ").strip()

    if pin.lower() == "new":
        from user import User
        from bank_acc import BankAccount

        name = input("Enter your name: ")
        pin = input("Set a 4-digit PIN: ")
        user = User(name, pin)

        acc_num = int(input("Enter new account number: "))
        opening_balance = float(input("Enter opening balance: "))
        user.add_account(BankAccount(acc_num, opening_balance))

        atm.add_user(user)
        save_data(atm.users)   
        print("User created successfully! Please restart to login.")
        return

    user = atm.authenticate(pin)
    if not user:
        print("Invalid PIN.")
        return

    atm.run_session(user)
    save_data(atm.users)   

if __name__ == "__main__":
    main()
