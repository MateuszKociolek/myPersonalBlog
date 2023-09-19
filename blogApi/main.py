from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from db.dbConfig import db_cursor, db_connections
from models.model import User
from functions import *


app = FastAPI()

# Konfiguracja CORS
origins = [
    "http://localhost:8080",  # Dodaj inne adresy URL, które mają dostęp
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Pozwala na wszystkie metody HTTP
    allow_headers=["*"],  # Pozwala na wszystkie nagłówki HTTP
)

@app.get("/")
async def root():
    return {"message" : "Hello World!"}

@app.post("/create_user")
async def add_new_user(user: User):
    res = createNewUser(user)
    return res

@app.get("/showAllUsers")
async def showAllUsers():
    res = show_all_users()
    return {"res": res}

@app.post("/logToAccount/")
async def logToAccount(user: User):
    try:
        res = log_To_Account(user)  
        return {"res": res}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.on_event("shutdown")
def shutdown_db_connections():
    db_cursor.close()
    db_connections.close()