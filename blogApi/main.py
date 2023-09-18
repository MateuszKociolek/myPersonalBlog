from fastapi import FastAPI

from db.dbConfig import db_cursor, db_connections
from models.model import User
from functions import *


app = FastAPI()

@app.get("/")
async def root():
    return {"message" : "Hello World!"}

@app.post("/create_user")
async def add_new_user(user: User):
    res = create_new_user(user)
    return res

@app.on_event("shutdown")
def shutdown_db_connections():
    db_cursor.close()
    db_connections.close()