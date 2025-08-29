# storage.py
import json
from user import User
from bank_acc import BankAccount

def save_data(users, filename="data.json"):
    data = []
    for user in users.values():
        user_data = {
            "name": user.name,
            "pin": user.pin,  # (will secure later)
            "accounts": [
                {"acc_num": acc.account_number, "balance": acc.balance}
                for acc in user.accounts.values()
            ]
        }
        data.append(user_data)

    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def load_data(filename="data.json"):
    users = {}
    try:
        with open(filename, "r") as f:
            data = json.load(f)

        for u in data:
            user = User(u["name"], u["pin"])
            for acc in u["accounts"]:
                account = BankAccount(acc["acc_num"], acc["balance"])
                user.add_account(account)
            users[user.pin] = user
    except FileNotFoundError:
        pass
    return users
