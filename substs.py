from app import app
from db import db

def get(id):
    sql = "SELECT * FROM substances WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    substance = result.fetchone()

    return substance

def getclass(id):
    sql = "SELECT classes.name FROM substances, classes WHERE substances.id=:id AND classes.id=substances.class_id"
    result = db.session.execute(sql, {"id":id})
    classname = result.fetchone()

    return classname

def getmoa(id):
    sql = "SELECT moas.target, moas.effect FROM substances, moas, substanceMoa WHERE substanceMoa.substance_id = :id AND substanceMoa.moa_id = moas.id"
    result = db.session.execute(sql, {"id":id})
    moa = result.fetchone()

    return moa

def getall():
    sql = "SELECT id, name FROM substances ORDER BY id ASC"
    result = db.session.execute(sql)
    allsubsts = result.fetchall()

    return allsubsts

def add(class_id, name, target, mechanism, metabolism, eff_duration, notes, risks):
    sql = "INSERT INTO substances(class_id, name, target, mechanism, metabolism, eff_duration, notes, risks) VALUES (:class_id, :name, :target, :mechanism, :metabolism, :eff_duration, :notes, :risks)"
    db.session.execute(sql, {"class_id":class_id, "name":name, "target":target, "mechanism":mechanism, "metabolism":metabolism, "eff_duration":eff_duration, "notes":notes, "risks":risks})
    db.session.commit()

def update(id, class_id, name, target, mechanism, metabolism, eff_duration, notes, risks):
    sql = "UPDATE substances SET class_id=:class_id, name=:name, target=:target, mechanism=:mechanism, metabolism=:metabolism, eff_duration=:eff_duration, notes=:notes, risks=:risks WHERE id=:id"
    db.session.execute(sql, {"class_id":class_id, "name":name, "target":target, "mechanism":mechanism, "metabolism":metabolism, "eff_duration":eff_duration, "notes":notes, "risks":risks, "id":id})
    db.session.commit()

def classlist():
    sql = "SELECT id, name FROM classes ORDER BY id ASC"
    result = db.session.execute(sql)
    classlist = result.fetchall()

    return classlist
