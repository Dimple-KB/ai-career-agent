import sqlite3

conn = sqlite3.connect("career_agent.db", check_same_thread=False)
cursor = conn.cursor()

# USERS
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
)
""")

# RESUMES
cursor.execute("""
CREATE TABLE IF NOT EXISTS resumes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    resume_text TEXT
)
""")

# RESULTS (ATS + AI OUTPUT)
cursor.execute("""
CREATE TABLE IF NOT EXISTS results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    ats_score TEXT,
    matched_skills TEXT,
    missing_skills TEXT,
    suggestions TEXT
)
""")

conn.commit()


def save_resume(user_id, text):
    cursor.execute(
        "INSERT INTO resumes (user_id, resume_text) VALUES (?, ?)",
        (user_id, text)
    )
    conn.commit()


def save_result(user_id, score, matched, missing, suggestions):
    cursor.execute("""
        INSERT INTO results (user_id, ats_score, matched_skills, missing_skills, suggestions)
        VALUES (?, ?, ?, ?, ?)
    """, (user_id, score, matched, missing, suggestions))

    conn.commit()
