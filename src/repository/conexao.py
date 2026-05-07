import sqlite3

class DatabaseConnection:
    _instance = None

    @classmethod
    def get_connection(cls):
        if cls._instance is None:
            cls._instance = sqlite3.connect('cinema_db.sqlite')
            cls._instance.row_factory = sqlite3.Row
            cls._criar_tabelas(cls._instance)
        return cls._instance

    @staticmethod
    def _criar_tabelas(conn):
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS filmes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            genero TEXT,
            duracao INTEGER,
            diretor TEXT,
            elenco TEXT
        )""")
        conn.commit()
