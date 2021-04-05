from flask import Flask
from flask import redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from os import getenv

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login",methods=["POST"])
def login():
    usr = request.form["username"]
    pwd = request.form["password"]
    # TODO: check username and password
    session["username"] = usr
    return redirect("/")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/createaccount", methods=["POST"])
def createaccount():
    username = request.form["username"]
    password = request.form["password"]

    hash_value = generate_password_hash(password)

    sql = "INSERT INTO users (username,password,role) VALUES (:username,:password,'user')"
    db.session.execute(sql, {"username":username,"password":hash_value})
    db.session.commit()

    session["username"] = username

    return redirect("/")

@app.route("/cancel")
def cancel():
    return redirect("/")

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")

