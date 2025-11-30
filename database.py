import sqlite3

DB_NAME = "medical.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS uploads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_name TEXT,
            contact_number TEXT,
            filename TEXT,
            doctor_comment TEXT DEFAULT '',
            status TEXT DEFAULT 'pending'
        )
    ''')
    conn.commit()
    conn.close()

def add_upload(patient_name, contact_number, filename):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute(
        "INSERT INTO uploads (patient_name, contact_number, filename) VALUES (?, ?, ?)",
        (patient_name, contact_number, filename)
    )
    conn.commit()
    conn.close()

def get_pending_uploads():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM uploads WHERE status='pending'")
    data = c.fetchall()
    conn.close()
    return data

def get_reviewed_uploads():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM uploads WHERE status='reviewed'")
    data = c.fetchall()
    conn.close()
    return data

def update_doctor_comment(upload_id, comment):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("UPDATE uploads SET doctor_comment=?, status='reviewed' WHERE id=?",
              (comment, upload_id))
    conn.commit()
    conn.close()
