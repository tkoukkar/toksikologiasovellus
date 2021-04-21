from app import app
from flask import redirect, render_template, request, session
from db import db

import users
import substs
import intacs

@app.route("/")
def index():
    """
    sql = "SELECT id, name FROM substances ORDER BY id ASC"
    result = db.session.execute(sql)
    substances = result.fetchall()
    """
    substances = substs.getall()

    return render_template("index.html", substances=substances)

@app.route("/login",methods=["POST"])
def login():
    usr = request.form["username"]
    pwd = request.form["password"]

    if users.confirm_login(usr, pwd):
        session["username"] = usr
        session["userrole"] = users.get_role(usr)
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
    role = request.form["role"]

    users.create(username, password, role)

    session["username"] = username
    session["userrole"] = role

    return redirect("/")

@app.route("/view/<int:id>")
def view(id):
    substance = substs.get(id)
    substclass = substs.getclass(id)
    interactions = intacs.getlist(id)

    return render_template("view.html", substance=substance, substclass=substclass, interactions=interactions)

@app.route("/newsubst")
def newsubst():
    classes = substs.classlist()

    return render_template("newsubst.html", classes=classes)

@app.route("/addsubstance", methods=["POST"])
def addsubstance():
    class_id = request.form["class"]
    name = request.form["name"]
    target = request.form["target"]
    mechanism = request.form["mechanism"]
    metabolism = request.form["metabolism"]
    eff_duration = request.form["eff_duration"]
    notes = request.form["notes"]
    risks = request.form["risks"]

    substs.add(class_id, name, target, mechanism, metabolism, eff_duration, notes, risks)

    return redirect("/")

@app.route("/editsubst/<int:id>")
def editsubst(id):
    substance = substs.get(id)
    classes = substs.classlist()

    return render_template("editsubst.html", substance=substance, classes=classes)

@app.route("/update/<int:id>", methods=["POST"])
def update(id):
    class_id = request.form["class"]
    name = request.form["name"]
    target = request.form["target"]
    mechanism = request.form["mechanism"]
    metabolism = request.form["metabolism"]
    eff_duration = request.form["eff_duration"]
    notes = request.form["notes"]
    risks = request.form["risks"]

    substs.update(id, class_id, name, target, mechanism, metabolism, eff_duration, notes, risks)

    return redirect("/")

@app.route("/newia")
def newia():
    """
    sql = "SELECT id, name FROM substances ORDER BY id ASC"
    result = db.session.execute(sql)
    substances = result.fetchall()
    """
    substances = substs.getall()

    return render_template("newia.html", substances=substances)

@app.route("/addinteraction", methods=["POST"])
def addinteraction():
    combination = request.form.getlist("substance")
    description = request.form["description"]

    # print(combination)

    intacs.add(combination, description)

    return redirect("/")

@app.route("/cancel")
def cancel():
    return redirect("/")

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")
