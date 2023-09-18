import models.model as mdl
from db.dbConfig import db_connections, db_cursor

def create_new_user(user: mdl.User):
    sql = "insert into users(email, password, username) values (%s, %s, %s)"
    val = (user.email, user.password, user.username,)
    db_cursor.execute(sql, val)
    db_connections.commit()
    return {"message": "User added properly"}