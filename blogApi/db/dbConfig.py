import mysql.connector

db_connections = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "myblog"
)

db_cursor = db_connections.cursor()