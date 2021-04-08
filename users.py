from app import app
from werkzeug.security import check_password_hash, generate_password_hash

from db import db

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
        # session["username"] = usr
    
    return False

def create(username, password):
    hash_value = generate_password_hash(password)

    sql = "INSERT INTO users (username,password,role) VALUES (:username,:password,'user')"
    db.session.execute(sql, {"username":username,"password":hash_value})
    db.session.commit()
