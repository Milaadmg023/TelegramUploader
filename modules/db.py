import sqlite3

class DB:
    def __init__(self):
        self.connection = sqlite3.connect("database.db")
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()

    def close(self):
        self.connection.close()

    def commit(self):
        self.connection.commit()

    def add_user(self, user_id):
        try:
            self.cursor.execute("INSERT INTO users VALUES (?)", (user_id,))
            self.commit()
            print("User added")
        except Exception as e:
            print(e)

    def get_users(self):
        try:
            self.cursor.execute("SELECT * FROM users")
            return self.cursor.fetchall()
        except Exception as e:
            print(e)
    
    def add_chat(self, chat_id , chat_link):
        try:
            self.cursor.execute("INSERT INTO chats VALUES (? , ?)", (chat_id , chat_link))
            self.commit()
            print("Chat added")
        except Exception as e:
            print(e)

    def get_chat_id(self):
        try:
            self.cursor.execute("SELECT chat_id FROM chats")
            return self.cursor.fetchall()
        except Exception as e:
            print(e)
    def get_chat_link(self):
        try:
            self.cursor.execute("SELECT chat_link FROM chats")
            return self.cursor.fetchall()
        except Exception as e:
            print(e)

    def get_chats(self):
        try:
            self.cursor.execute("SELECT * FROM chats")
            return self.cursor.fetchall()
        except Exception as e:
            print(e)