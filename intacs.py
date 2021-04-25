from app import app
from db import db

def getlist(substance_id):
    ialist = []

    sql = "SELECT interactions.id, interactions.description FROM substances, interactions, substanceInteraction WHERE substanceInteraction.substance_id = :substance_id AND substanceInteraction.interaction_id = interactions.id"
    result = db.session.execute(sql, {"substance_id":substance_id})
    interaction = result.fetchone()

    if interaction:
       cmb = get_combination(interaction[0])
       ialist.append((interaction[0], cmb, interaction[1]))

    return ialist

def get_combination(interaction_id):
    sql = "SELECT substances.name FROM substances, substanceInteraction WHERE substanceInteraction.substance_id = substances.id AND substanceInteraction.interaction_id = :interaction_id"
    result = db.session.execute(sql, {"interaction_id":interaction_id})
    combination = result.fetchall()

    return combination

def add(combination, description):
    sql = "INSERT INTO interactions(description) VALUES (:description) RETURNING id"
    result = db.session.execute(sql, {"description":description})
    interaction_id = result.fetchone()[0]

    for substance_id in combination:
        link = "INSERT INTO substanceInteraction(substance_id, interaction_id) VALUES (:substance_id, :interaction_id)"
        db.session.execute(link, {"substance_id":substance_id, "interaction_id":interaction_id})

    db.session.commit()
