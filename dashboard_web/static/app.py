from flask import Flask, render_template, request, redirect, session
from auth import check_login

app = Flask(__name__)
app.secret_key = "phishguard_secret_key"

@app.route("/")
def home():
    if not session.get("logged_in"):
        return redirect("/login")
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["username"]
        pwd = request.form["password"]
        if check_login(user, pwd):
            session["logged_in"] = True
            return redirect("/")
        return "Invalid username or password!"
    return render_template("login.html")

@app.route("/logout")
def logout():
    session["logged_in"] = False
    return redirect("/login")

if __name__ == "__main__":
    app.run(port=8000, debug=True)
