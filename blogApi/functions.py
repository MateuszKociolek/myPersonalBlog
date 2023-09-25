import models.model as mdl
from db.dbConfig import db_connections, db_cursor

def createNewUser(user: mdl.User):
    sql = "insert into users(email, password, username) values (%s, %s, %s)"
    val = (user.email, user.password, user.username,)
    db_cursor.execute(sql, val)
    db_connections.commit()
    return {"res": {
        "email":val[0],
        "username":val[2],
    }}

def show_all_users():
    sql = "select * from users"
    db_cursor.execute(sql)
    res = db_cursor.fetchall()
    return res

def log_To_Account(user: mdl.User):
    sql = "SELECT * FROM users WHERE email = %s"
    val = (user.email,)
    try:
        db_cursor.execute(sql,val)
        res = db_cursor.fetchall()
        return res

    except Exception as e:
        return {"message" : "no user found: "+ str(e) }