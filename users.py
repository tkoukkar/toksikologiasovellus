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
