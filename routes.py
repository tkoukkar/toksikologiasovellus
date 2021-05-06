from app import app
from flask import redirect, render_template, request, session
from db import db

import users
import substs
import intacs

@app.route("/")
def index():
    """
    Aloitusnäkymä
    """
    substances = substs.getall()

    return render_template("index.html", substances=substances)

@app.route("/login", methods=["POST"])
def login():
    """
    Käsittelee sisäänkirjautumisen. Jos tunnus ja salasana ovat oikein, kirjaa käyttäjän sisään; muutoin näyttää virheilmoituksen.
    """
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
    """
    Siirtyy uuden käyttäjän luontinäkymään.
    """
    return render_template("signup.html")

@app.route("/createaccount", methods=["POST"])
def createaccount():
    """
    Luo uuden käyttäjän kutsumalla users-moduulin funktiota create, kirjaa tämän sisään ja palaa aloitusnäkymään.
    """
    username = request.form["username"]
    password = request.form["password"]
    role = request.form["role"]

    users.create(username, password, role)

    session["username"] = username
    session["userrole"] = role

    return redirect("/")

@app.route("/search", methods=["POST"])
def search():
    """
    Kutsuu aineen hakufunktiota ja siirtyy haun tulokset -näkymään.
    """
    srchstring = request.form["srchstring"]
    srchres = []

    substances = substs.getall()

    for substance in substances:
        if srchstring in substance[1]:
            srchres.append(substance)

    return render_template("srchres.html", substances=srchres)

@app.route("/view/<int:id>")
def view(id):
    """
    Siirtyy aineen tietonäkymään.
    """
    substance = substs.get(id)

    if not substance:
        return render_template("notfound.html")

    substclass = substs.cls(id)
    indications = substs.ind(id)
    mechanisms = substs.moa(id)

    interactions = intacs.getlist(id)

    return render_template("view.html", substance=substance, substclass=substclass, indications=indications, mechanisms=mechanisms, interactions=interactions)

@app.route("/newsubst")
def newsubst():
    """
    Siirtyy aineen luontinäkymään.
    """
    classes = substs.classlist()
    indications = substs.indlist()

    return render_template("newsubst.html", classes=classes)

@app.route("/addsubstance", methods=["POST"])
def addsubstance():
    """
    Käsittelee aineen luonnin ensimmäisen vaiheen ja siirtyy indikaatioiden ja vaikutusmekanismien muokkausnäkymään.
    """
    class_id = request.form["class"]
    name = request.form["name"]
    # target = request.form["target"]
    # effect = request.form["effect"]
    metabolism = request.form["metabolism"]
    eff_duration = request.form["eff_duration"]
    notes = request.form["notes"]
    risks = request.form["risks"]

    subst_id = substs.add(class_id, name, metabolism, eff_duration, notes, risks)

    moas = substs.classmoas(class_id)
    indications = substs.indlist()

    return render_template("editp2.html", subst_id=subst_id, moas=moas, indications=indications)

@app.route("/editsubst/<int:id>")
def editsubst(id):
    """
    Siirtyy aineen muokkausnäkymään.
    """
    substance = substs.get(id)
    classes = substs.classlist()

    return render_template("editsubst.html", substance=substance, classes=classes)

@app.route("/update/<int:id>", methods=["POST"])
def update(id):
    """
    Käsittelee aineen tietojen muokkaamisen ensimmäisen vaiheen ja siirtyy indikaatioiden ja vaikutusmekanismien muokkausnäkymään.
    """
    class_id = request.form["class"]
    name = request.form["name"]
    # target = request.form["target"]
    # mechanism = request.form["mechanism"]
    metabolism = request.form["metabolism"]
    eff_duration = request.form["eff_duration"]
    notes = request.form["notes"]
    risks = request.form["risks"]

    substs.update(id, class_id, name, metabolism, eff_duration, notes, risks)

    moas = substs.classmoas(class_id)
    indications = substs.indlist()

    return render_template("editp2.html", subst_id=id, moas=moas, indications=indications)

@app.route("/editlts/<int:subst_id>", methods=["POST"])
def editlts(subst_id):
    """
    Käsittelee aineen luonnin tai muokkaamisen toisen vaiheen ja palaa aloitusnäkymään.
    """
    moa = request.form.getlist("moa")
    indications = request.form.getlist("indication")

    substs.add_moa(subst_id, moa)
    substs.add_indications(subst_id, indications)

    return redirect("/")

@app.route("/delete/<int:id>")
def delete(id):
    substs.delete(id)

    return redirect("/")

@app.route("/newia")
def newia():
    """
    Siirtyy yhteisvaikutusten muokkausnäkymään.
    """
    substances = substs.getall()

    return render_template("newia.html", substances=substances)

@app.route("/addinteraction", methods=["POST"])
def addinteraction():
    """
    Käsittelee yhteisvaikutusten lisäämisen ja palaa aloitusnäkymään.
    """
    combination = request.form.getlist("substance")
    description = request.form["description"]

    intacs.add(combination, description)

    return redirect("/")

@app.route("/cancel")
def cancel():
    """
    Palaa aloitusnäkymään.
    """
    return redirect("/")

@app.route("/logout")
def logout():
    """
    Kirjaa käyttäjän ulos ja palaa aloitusnäkymään.
    """
    del session["username"]
    return redirect("/")
