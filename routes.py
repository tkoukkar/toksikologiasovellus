from distutils.util import strtobool

from app import app
from flask import redirect, render_template, request, session
from db import db

import users
import substs
import intacs
import srch

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
        return render_template("error.html", message="Virheellinen käyttäjätunnus tai salasana.")

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

    if users.exists(username):
        return render_template("error.html", message="Antamasi nimi on jo käytössä.")

    role = request.form["role"]

    users.create(username, password, role)

    session["username"] = username
    session["userrole"] = role

    return redirect("/")

@app.route("/userlist")
def userlist():
    """
    Siirtyy käyttäjälistaan.
    """
    usrl = users.getall()

    return render_template("userlist.html", userlist=usrl)

@app.route("/makeadmin/<int:id>")
def makeadmin(id):
    users.make_admin(id)

    return redirect("/")

@app.route("/deleteaccount/<int:id>")
def deleteaccount(id):
    users.delete(id)

    return redirect("/")

@app.route("/search", methods=["POST"])
def search():
    """
    Kutsuu srch-moduulin nimen perusteella -hakufunktiota, jolle annetaan parametrina käyttäjän syöttämä aineen nimi tai sen osa, ja siirtyy haun tulokset -näkymään.
    """
    srchstring = request.form["srchstring"]
    srchres = srch.by_name(srchstring)

    return render_template("srchres.html", substances=srchres)

@app.route("/advsearch", methods=["POST"])
def advsearch():
    class_id = request.form["class"]
    name = request.form["name"]
    metabolism = request.form["metabolism"]
    ind_id = request.form["indication"]
    moa_id = request.form["moa"]
    
    srchres = srch.adv(int(class_id), name, metabolism, int(ind_id), int(moa_id))

    return render_template("srchres.html", substances=srchres)

@app.route("/openadvsrch")
def openadvsrch():
    classes = substs.classlist()
    moas = substs.classmoas(1)
    indications = substs.indlist()

    return render_template("advsrch.html", classes=classes, moas=moas, indications=indications)

@app.route("/view/<int:id>")
def view(id):
    """
    Siirtyy aineen tietonäkymään.
    """
    substance = substs.get(id)

    if not substance:
        return render_template("error.html", message="Sivua ei löydy.")

    substclass = substs.cls(id)
    indications = substs.ind(id)
    mechanisms = substs.moas(id)

    interactions = intacs.getlist(id)

    return render_template("view.html", substance=substance, substclass=substclass, indications=indications, mechanisms=mechanisms, interactions=interactions)

@app.route("/newsubst")
def newsubst():
    """
    Siirtyy aineen luontinäkymään.
    """
    classes = substs.classlist()

    return render_template("newsubst.html", classes=classes)

@app.route("/addsubst", methods=["POST"])
def addsubst():
    """
    Käsittelee aineen luonnin ensimmäisen vaiheen ja siirtyy indikaatioiden ja vaikutusmekanismien muokkausnäkymään.
    """
    class_id = request.form["class"]
    name = request.form["name"]
    metabolism = request.form["metabolism"]
    eff_duration = request.form["eff_duration"]
    notes = request.form["notes"]
    risks = request.form["risks"]

    subst_id = substs.add(class_id, name.lower(), metabolism.lower(), eff_duration, notes, risks)

    moas = substs.classmoas(class_id)
    indications = substs.indlist()

    return render_template("createp2.html", subst_id=subst_id, moas=moas, indications=indications)

@app.route("/editnew/<int:id>")
def editnew(id):
    """
    Siirtyy aineen muokkausnäkymään.
    """
    substance = substs.get(id)
    substclass = substs.cls(id)
    classes = substs.classlist()

    return render_template("editsubst.html", substance=substance, substclass=substclass, classes=classes, new=True)

@app.route("/editsubst/<int:id>")
def editsubst(id):
    """
    Siirtyy aineen muokkausnäkymään.
    """
    substance = substs.get(id)
    substclass = substs.cls(id)
    classes = substs.classlist()

    return render_template("editsubst.html", substance=substance, substclass=substclass, classes=classes, new=False)

@app.route("/update/<int:id>", methods=["POST"])
def update(id):
    """
    Käsittelee aineen tietojen muokkaamisen ensimmäisen vaiheen ja siirtyy indikaatioiden ja vaikutusmekanismien muokkausnäkymään.
    Jos kyseessä on uusi aine (tieto lomakkeelta, tallennetaan muuttujaan creating), käytetään sivua createp2.html, jolle ei syötetä aineen aiempia tietoja.
    Muussa tapauksessa haetaan tiedot aineelle aiemmin syötetyistä indikaatioista ja vaikutusmekanismeista ja siirrytään sivulle editp2.html.
    """
    class_id = request.form["class"]
    name = request.form["name"]
    metabolism = request.form["metabolism"]
    eff_duration = request.form["eff_duration"]
    notes = request.form["notes"]
    risks = request.form["risks"]
    creating = strtobool(request.form["new"])

    substs.update(id, class_id, name.lower(), metabolism.lower(), eff_duration, notes, risks)

    classmoas = substs.classmoas(class_id)
    allind = substs.indlist()

    if creating:
        return render_template("createp2.html", subst_id=id, moas=classmoas, indications=allind)

    substmoas = substs.moas(id)
    substind = substs.ind(id)
    moa_ids = []
    ind_ids = []

    for moa in substmoas:
        moa_ids.append(moa[0])

    for ind in substind:
        ind_ids.append(ind[0])

    return render_template("editp2.html", subst_id=id, classmoas=classmoas, indications=allind, moa_ids=moa_ids, ind_ids=ind_ids)

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

@app.route("/uncreate/<int:id>")
def uncreate(id):
    substs.uncreate(id)

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
