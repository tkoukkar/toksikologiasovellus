from app import app
from flask import redirect, render_template, request, session
# from werkzeug.security import check_password_hash, generate_password_hash

from db import db

import users

@app.route("/")
def index():
    sql = "SELECT id, name FROM substances ORDER BY id ASC"
    result = db.session.execute(sql)
    substances = result.fetchall()

    return render_template("index.html", substances=substances)

@app.route("/login",methods=["POST"])
def login():
    usr = request.form["username"]
    pwd = request.form["password"]

    if users.confirm_login(usr, pwd):
        session["username"] = usr
    else:
        return render_template("youshallnotpass.html")

    return redirect("/")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/createaccount", methods=["POST"])
def createaccount():
    username = request.form["username"]
    password = request.form["password"]

    users.create(username, password)

    session["username"] = username

    return redirect("/")

@app.route("/view/<int:id>")
def view(id):
    sql = "SELECT * FROM substances WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    substance = result.fetchone()

    name = substance[1]
    target = substance[2]
    mechanism = substance[3]
    metabolism = substance[4]
    eff_duration = substance[5]
    notes = substance[6]

    return render_template("view.html", name=name, target=target, mechanism=mechanism, metabolism=metabolism, eff_duration=eff_duration, notes=notes)

@app.route("/cancel")
def cancel():
    return redirect("/")

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")
