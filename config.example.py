import sqlite3

API_HASH = ""
APP_ID = ""
BOT_TOKEN = ""
TRACK_CHANNEL = "" # track_channel id started with -100
OWNERS_ID = "" # list  of bot admins id [id1, id2 , ...]
BOT_ID = "" # bot id without @

# create database
def create_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS users (
             user_id INTEGER PRIMARY KEY
     )""")
    conn.commit()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS chats (
             chat_id INTEGER PRIMARY KEY,
             chat_link TEXT
     )""")
    conn.commit()
    conn.close()


create_db()