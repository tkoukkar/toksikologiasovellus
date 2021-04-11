from app import app
from db import db

def get(id):
    sql = "SELECT * FROM substances WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    substance = result.fetchone()

    return substance

def list_interactions(id):
    interactions = []

    sql = "SELECT interactions.id, interactions.description FROM substances, interactions, substanceInteraction WHERE substanceInteraction.substance_id = :id AND substanceInteraction.interaction_id = interactions.id"
    result = db.session.execute(sql, {"id":id})
    interaction = result.fetchone()

    if interaction:
       cmb = get_combination(interaction[0])
       interactions.append((interaction[0], cmb, interaction[1]))

    return interactions

def get_combination(interaction_id):
    sql = "SELECT substances.name FROM substances, substanceInteraction WHERE substanceInteraction.substance_id = substances.id AND substanceInteraction.interaction_id = :interaction_id"
    result = db.session.execute(sql, {"interaction_id":interaction_id})
    combination = result.fetchall()

    return combination

def add(name, target, mechanism, metabolism, eff_duration, notes, risks):
    sql = "INSERT INTO substances(name, target, mechanism, metabolism, eff_duration, notes, risks) VALUES (:name, :target, :mechanism, :metabolism, :eff_duration, :notes, :risks)"
    db.session.execute(sql, {"name":name,"target":target,"mechanism":mechanism,"metabolism":metabolism,"eff_duration":eff_duration,"notes":notes,"risks":risks})
    db.session.commit()

def addinteraction(combination, description):
    sql = "INSERT INTO interactions(description) VALUES (:description) RETURNING id"
    result = db.session.execute(sql, {"description":description})
    interaction_id = result.fetchone()[0]

    for substance_id in combination:
        """
        sid = "SELECT id FROM substances WHERE name=:substance"
        res = db.session.execute(sid, {"name":substance})
        substance_id = res.fetchone()[0]
        """

        link = "INSERT INTO substanceInteraction(substance_id, interaction_id) VALUES (:substance_id, :interaction_id)"
        db.session.execute(link, {"substance_id":substance_id, "interaction_id":interaction_id})

    db.session.commit()
