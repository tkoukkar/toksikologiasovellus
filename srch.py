from app import app
from db import db
import substs

def by_name(srchstring):
    srchres = []

    substances = substs.getall()

    for substance in substances:
        if srchstring in substance[1]:
            srchres.append(substance)

    return srchres

def by_indication(indication_id):
    if indication_id == 0:
        return range(1, 100)

    res_ids = []

    sql = "SELECT substances.id FROM substances, substanceIndication WHERE substanceIndication.substance_id = substances.id AND substanceIndication.indication_id = :indication_id"
    result = db.session.execute(sql, {"indication_id":indication_id})
    substances = result.fetchall()

    for substance in substances:
        res_ids.append(substance.id)

    return res_ids

def by_moa(moa_id):
    if moa_id == 0:
        return range(1, 100)

    res_ids = []

    sql = "SELECT substances.id FROM substances, substanceMoa WHERE substanceMoa.substance_id = substances.id AND substanceMoa.moa_id = :moa_id"
    result = db.session.execute(sql, {"moa_id":moa_id})
    substances = result.fetchall()

    for substance in substances:
        res_ids.append(substance.id)

    return res_ids

def adv(class_id, name, metabolism, ind_id, moa_id):
    srchres = []

    sql = "SELECT * FROM substances WHERE visible=TRUE ORDER BY id ASC"
    result = db.session.execute(sql)
    substances = result.fetchall()

    ind_filter = by_indication(ind_id)
    moa_filter = by_moa(moa_id)

    for substance in substances:
        if substance[0] in ind_filter and substance[0] in moa_filter:
            if class_id == 0:
                if name in substance[2] and metabolism in substance[3]:
                    srchres.append([substance[0], substance[2]])
            else:
                if substance[1] == class_id and name in substance[2] and metabolism in substance[3]:
                    srchres.append([substance[0], substance[2]])

    return srchres
