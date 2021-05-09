from app import app
from werkzeug.security import check_password_hash, generate_password_hash

from db import db

def getall():
    """
    Hakee kaikkien käyttäjien tunnisteet ja nimet tietokannasta.
    """
    sql = "SELECT * FROM users ORDER BY id ASC"
    result = db.session.execute(sql)
    userlist = result.fetchall()

    return userlist

def confirm_login(usr, pwd):
    sql = "SELECT password FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":usr})
    user = result.fetchone()

    if user == None:
        return False
    else:
        hash_value = user[0]

    if check_password_hash(hash_value, pwd):
        return True
    
    return False

def get_role(usr):
    sql = "SELECT role FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":usr})
    user = result.fetchone()

    return user[0]

def create(username, password, role):
    hash_value = generate_password_hash(password)

    sql = "INSERT INTO users (username,password,role) VALUES (:username,:password,:role)"
    db.session.execute(sql, {"username":username,"password":hash_value,"role":role})
    db.session.commit()

def exists(username):
    sql = "SELECT * FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()

    if user:
        return True

    return False

def make_admin(id):
    """
    Päivittää parametrina saatua tunnistetta vastaavan aineen tiedot tietokantaan.
    """
    sql = "UPDATE users SET role='admin' WHERE id=:id"
    db.session.execute(sql, {"id":id})
    db.session.commit()

def delete(id):
    """
    Poistaa aineen lopullisesti tietokannasta.
    """
    sql = "DELETE FROM users WHERE id = :id"
    db.session.execute(sql, {"id":id})
    db.session.commit()
