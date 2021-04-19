from app import app
from db import db

def get(id):
    sql = "SELECT * FROM substances WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    substance = result.fetchone()

    return substance

def add(name, target, mechanism, metabolism, eff_duration, notes, risks):
    sql = "INSERT INTO substances(name, target, mechanism, metabolism, eff_duration, notes, risks) VALUES (:name, :target, :mechanism, :metabolism, :eff_duration, :notes, :risks)"
    db.session.execute(sql, {"name":name,"target":target,"mechanism":mechanism,"metabolism":metabolism,"eff_duration":eff_duration,"notes":notes,"risks":risks})
    db.session.commit()
