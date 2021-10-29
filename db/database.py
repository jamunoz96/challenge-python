import sqlite3

class Database:
    def __init__(self):
        connect = sqlite3.connect('db/SQLite.db')
        cursor = connect.cursor()

        self.connection = connect
        self.cursor = cursor   