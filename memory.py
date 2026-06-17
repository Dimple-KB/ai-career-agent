import sqlite3
import datetime

DB = "db.sqlite"


def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS memory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            query TEXT,
            response TEXT,
            timestamp TEXT
        )
    """)
    conn.commit()
    conn.close()


def save_memory(query, response):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute(
        "INSERT INTO memory (query, response, timestamp) VALUES (?, ?, ?)",
        (query, response, str(datetime.datetime.now()))
    )
    conn.commit()
    conn.close()


def get_memory():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT query, response FROM memory ORDER BY id DESC LIMIT 5")
    rows = c.fetchall()
    conn.close()
    return rows
