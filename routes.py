from app import app
from flask import redirect, render_template, request, session
from db import db

import users
import substs
import intacs

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
    interactions = intacs.getlist(id)
    """
    sql = "SELECT * FROM substances WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    substance = result.fetchone()

    sql = "SELECT * FROM substances, interactions, substanceInteraction WHERE substanceInteraction.substance_id = :id AND substanceInteraction.interaction_id = interactions.id"
    result = db.session.execute(sql, {"id":id})
    substance = result.fetchall()
    """

    return render_template("view.html", substance=substance, interactions=interactions)

@app.route("/newsubst")
def newsubst():
    return render_template("newsubst.html")

@app.route("/addsubstance", methods=["POST"])
def addsubstance():
    name = request.form["name"]
    target = request.form["target"]
    mechanism = request.form["mechanism"]
    metabolism = request.form["metabolism"]
    eff_duration = request.form["eff_duration"]
    notes = request.form["notes"]
    risks = request.form["risks"]

    substs.add(name, target, mechanism, metabolism, eff_duration, notes, risks)

    return redirect("/")

@app.route("/newia")
def newia():
    sql = "SELECT id, name FROM substances ORDER BY id ASC"
    result = db.session.execute(sql)
    substances = result.fetchall()

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
