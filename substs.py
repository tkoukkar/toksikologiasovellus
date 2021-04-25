from app import app
from db import db

def get(id):
    sql = "SELECT * FROM substances WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    substance = result.fetchone()

    return substance

def getall():
    sql = "SELECT id, name FROM substances ORDER BY id ASC"
    result = db.session.execute(sql)
    allsubsts = result.fetchall()

    return allsubsts

def search(name):
    print(name)
    sql = "SELECT id, name FROM substances WHERE name=:name ORDER BY id ASC"
    result = db.session.execute(sql, {"name":name})
    srchres = result.fetchall()

    print(srchres)

    return srchres

def cls(id):
    sql = "SELECT classes.name FROM substances, classes WHERE substances.id=:id AND classes.id=substances.class_id"
    result = db.session.execute(sql, {"id":id})
    classname = result.fetchone()

    return classname

def moa(id):
    sql = "SELECT moas.target, moas.effect FROM substances, moas, substanceMoa WHERE substanceMoa.substance_id = :id AND substanceMoa.moa_id = moas.id"
    result = db.session.execute(sql, {"id":id})
    mechanism = result.fetchone()

    return mechanism

def ind(id):
    sql = "SELECT indications.name, substanceIndication.route, substanceIndication.notes FROM substances, indications, substanceIndication WHERE substanceIndication.substance_id = :id AND substanceIndication.indication_id = indications.id"
    result = db.session.execute(sql, {"id":id})
    indication = result.fetchone()

    return indication

def add(class_id, name, metabolism, eff_duration, notes, risks):
    sql = "INSERT INTO substances(class_id, name, metabolism, eff_duration, notes, risks) VALUES (:class_id, :name, :metabolism, :eff_duration, :notes, :risks) RETURNING id"
    result = db.session.execute(sql, {"class_id":class_id, "name":name, "metabolism":metabolism, "eff_duration":eff_duration, "notes":notes, "risks":risks})
    id = result.fetchone()[0]

    db.session.commit()

    return id

def update(id, class_id, name, metabolism, eff_duration, notes, risks):
    sql = "UPDATE substances SET class_id=:class_id, name=:name, metabolism=:metabolism, eff_duration=:eff_duration, notes=:notes, risks=:risks WHERE id=:id"
    db.session.execute(sql, {"class_id":class_id, "name":name, "metabolism":metabolism, "eff_duration":eff_duration, "notes":notes, "risks":risks, "id":id})
    db.session.commit()


def add_moa(substance_id, moalist):
    for moa_id in moalist:
        sql = "INSERT INTO substanceMoa (substance_id, moa_id) VALUES (:substance_id, :moa_id)"
        db.session.execute(sql, {"substance_id":substance_id, "moa_id":moa_id})
        db.session.commit()

def add_indications(substance_id, indications):
    for indication_id in indications:
        sql = "INSERT INTO substanceIndication (substance_id, indication_id) VALUES (:substance_id, :indication_id)"
        db.session.execute(sql, {"substance_id":substance_id, "indication_id":indication_id})
        db.session.commit()

"""
def set_moa(substance_id, moa_id):
    sql = "UPDATE substanceMoa SET moa_id=:moa_id WHERE substance_id=:substance_id"
    db.session.execute(sql, {"moa_id":moa_id, "substance_id":substance_id})
    db.session.commit()
"""

def classlist():
    sql = "SELECT id, name FROM classes ORDER BY id ASC"
    result = db.session.execute(sql)
    classlist = result.fetchall()

    return classlist

def classmoas(class_id):
    sql = "SELECT id, target, effect FROM moas WHERE class_id = :class_id ORDER BY id ASC"
    result = db.session.execute(sql, {"class_id":class_id})
    moas = result.fetchall()

    return moas

def indlist():
    sql = "SELECT id, name FROM indications ORDER BY type ASC"
    result = db.session.execute(sql)
    indications = result.fetchall()

    return indications
