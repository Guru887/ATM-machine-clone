# app.py
from flask import Flask, request, session, redirect, url_for, render_template
from atm import ATM, User  # adjust import if atm.py is in another folder

app = Flask(__name__)
app.secret_key = "supersecretkey"   # required for session management

# Create ATM instance
atm = ATM()

# Example user for testing
u1 = User("Guru", "1234")   # name, pin
atm.add_user(u1)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        pin = request.form["pin"]   # only pin needed
        user = atm.authenticate(pin)
        if user:
            session["pin"] = pin   # store pin in session
            return redirect(url_for("dashboard"))
        else:
            return "Invalid credentials", 401
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
    account = list(user.accounts.values())[0]  # use first account for now
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


if __name__ == "__main__":
    app.run(debug=True)
