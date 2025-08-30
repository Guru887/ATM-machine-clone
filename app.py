from flask import Flask, render_template, request, redirect, url_for, session
from atm import ATM
from user import User
from bank_account import BankAccount

app = Flask(__name__)
app.secret_key = "supersecretkey"   # required for session

# Create ATM system and seed users
atm = ATM()
user1 = User("Guru", "1234")
user1.add_account(BankAccount(101, 5000))
atm.add_user(user1)

user2 = User("Madhu", "5678")
user2.add_account(BankAccount(102, 10000))
atm.add_user(user2)


@app.route("/")
def home():
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        pin = request.form["pin"]
        user = atm.authenticate(pin)
        if user:
            session["pin"] = pin
            return redirect(url_for("dashboard"))
        else:
            return render_template("login.html", error="Invalid PIN")
    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    pin = session.get("pin")
    if not pin:
        return redirect(url_for("login"))
    user = atm.authenticate(pin)
    if not user:
        return redirect(url_for("login"))
    return render_template("dashboard.html", user=user)


@app.route("/deposit", methods=["POST"])
def deposit():
    pin = session.get("pin")
    if not pin:
        return redirect(url_for("login"))
    user = atm.authenticate(pin)
    account = list(user.accounts.values())[0]  # first account only
    amount = float(request.form["amount"])
    account.deposit(amount)
    return redirect(url_for("dashboard"))


@app.route("/withdraw", methods=["POST"])
def withdraw():
    pin = session.get("pin")
    if not pin:
        return redirect(url_for("login"))
    user = atm.authenticate(pin)
    account = list(user.accounts.values())[0]
    amount = float(request.form["amount"])
    try:
        account.withdraw(amount)
    except ValueError as e:
        return render_template("dashboard.html", user=user, error=str(e))
    return redirect(url_for("dashboard"))


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        pin = request.form["pin"]
        acc_num = request.form["acc_num"]
        balance = float(request.form["balance"])

        # create new user
        user = User(name, pin)
        user.add_account(BankAccount(acc_num, balance))
        atm.add_user(user)

        return redirect(url_for("login"))  # go back to login after signup

    return render_template("register.html")


if __name__ == "__main__":
    app.run(debug=True)
