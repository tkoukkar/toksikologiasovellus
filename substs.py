from app import app
from db import db

def get(id):
    """
    Hakee parametrina saatua tunnistetta vastaavan aineen tiedot tietokannasta.
    """
    sql = "SELECT * FROM substances WHERE id=:id AND visible=TRUE"
    result = db.session.execute(sql, {"id":id})
    substance = result.fetchone()

    return substance

def getall():
    """
    Hakee kaikkien aineiden tunnisteet ja nimet tietokannasta.
    """
    sql = "SELECT id, name FROM substances WHERE visible=TRUE ORDER BY id ASC"
    result = db.session.execute(sql)
    allsubsts = result.fetchall()

    return allsubsts

def cls(id):
    """
    Hakee parametrina saatua tunnistetta vastaavan aineen luokan nimen tietokannasta.
    """
    sql = "SELECT classes.name FROM substances, classes WHERE substances.id=:id AND classes.id=substances.class_id"
    result = db.session.execute(sql, {"id":id})
    classname = result.fetchone()

    return classname.name

def moas(id):
    """
    Hakee parametrina saatua tunnistetta vastaavan aineen vaikutusmekanismin tietokannasta.
    """
    sql = "SELECT moas.id, moas.target, moas.effect FROM substances, moas, substanceMoa WHERE substanceMoa.substance_id = :id AND substanceMoa.moa_id = moas.id"
    result = db.session.execute(sql, {"id":id})
    rows = result.fetchall()

    ids = []
    mechanisms = []

    for mechanism in rows:
        if not mechanism[0] in ids:
            mechanisms.append([mechanism[0], mechanism[1], mechanism[2]])
            ids.append(mechanism[0])

    return mechanisms

def ind(id):
    """
    Hakee parametrina saatua tunnistetta vastaavan aineen käyttötarkoitukset tietokannasta.
    """
    sql = "SELECT indications.id, indications.name, substanceIndication.route, substanceIndication.notes FROM substances, indications, substanceIndication WHERE substanceIndication.substance_id = :id AND substanceIndication.indication_id = indications.id"
    result = db.session.execute(sql, {"id":id})
    rows = result.fetchall()

    indications = []
    ids = []

    for indication in rows:
        if not indication[0] in ids:
            indications.append(indication)
            ids.append(indication[0])

    return indications

def add(class_id, name, metabolism, eff_duration, notes, risks):
    """
    Lisää tietokantaan parametreina saadut uuden aineen tiedot
    """
    sql = "INSERT INTO substances(class_id, name, metabolism, eff_duration, notes, risks, visible) VALUES (:class_id, :name, :metabolism, :eff_duration, :notes, :risks, TRUE) RETURNING id"
    result = db.session.execute(sql, {"class_id":class_id, "name":name, "metabolism":metabolism, "eff_duration":eff_duration, "notes":notes, "risks":risks})
    id = result.fetchone()[0]

    db.session.commit()

    return id

def update(id, class_id, name, metabolism, eff_duration, notes, risks):
    """
    Päivittää parametrina saatua tunnistetta vastaavan aineen tiedot tietokantaan.
    """
    sql = "UPDATE substances SET class_id=:class_id, name=:name, metabolism=:metabolism, eff_duration=:eff_duration, notes=:notes, risks=:risks WHERE id=:id"
    db.session.execute(sql, {"class_id":class_id, "name":name, "metabolism":metabolism, "eff_duration":eff_duration, "notes":notes, "risks":risks, "id":id})
    db.session.commit()

def add_moa(substance_id, moalist):
    """
    Päivittää parametrina saatua tunnistetta vastaavan aineen vaikutusmekanismin tietokantaan.
    """
    for moa_id in moalist:
        sql = "INSERT INTO substanceMoa (substance_id, moa_id) VALUES (:substance_id, :moa_id)"
        db.session.execute(sql, {"substance_id":substance_id, "moa_id":moa_id})
        db.session.commit()

def add_indications(substance_id, indications):
    """
    Päivittää parametrina saatua tunnistetta vastaavan aineen käyttötarkoitukset tietokantaan.
    """
    for indication_id in indications:
        sql = "INSERT INTO substanceIndication (substance_id, indication_id) VALUES (:substance_id, :indication_id)"
        db.session.execute(sql, {"substance_id":substance_id, "indication_id":indication_id})
        db.session.commit()

def delete(id):
    """
    Merkitsee aineen tietokannassa poistetuksi, jolloin se ei enää näy aloitusnäkymässä eikä haun tuloksissa.
    """
    sql = "UPDATE substances SET visible=FALSE WHERE id = :id"
    db.session.execute(sql, {"id":id})
    db.session.commit()

def uncreate(id):
    """
    Poistaa aineen lopullisesti tietokannasta.
    """
    sql = "DELETE FROM substances WHERE id = :id"
    db.session.execute(sql, {"id":id})
    db.session.commit()

def classlist():
    """
    Palauttaa listan tietokantaan syötetyistä aineluokista.
    """
    sql = "SELECT id, name FROM classes ORDER BY id DESC"
    result = db.session.execute(sql)
    classlist = result.fetchall()

    return classlist

def classmoas(class_id):
    """
    Hakee parametrina saatua tunnistetta vastaavaa aineluokkaa vastaavat vaikutusmekanismit tietokannasta.
    Jos luokkaa vastaavia vaikutusmekanismeja ei löydy, palauttaa kaikki tietokantaan syötetyt vaikutusmekanismit.
    """
    sql = "SELECT id, target, effect FROM moas WHERE class_id = :class_id ORDER BY id ASC"
    result = db.session.execute(sql, {"class_id":class_id})
    moas = result.fetchall()

    if not moas:
        sql_n = "SELECT id, target, effect FROM moas ORDER BY id ASC"
        result_n = db.session.execute(sql_n)
        moas = result_n.fetchall()

    return moas

def indlist():
    """
    Palauttaa listan tietokantaan syötetyistä aineiden käyttötarkoituksista.
    """
    sql = "SELECT id, name FROM indications ORDER BY type ASC"
    result = db.session.execute(sql)
    indications = result.fetchall()

    return indications
