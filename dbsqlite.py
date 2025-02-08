import sqlite3

from cryptogrghy import decrypt_password, encrypt_password

# Initialize database
def init_db():
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY,
            service TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Save password
def save_password(service, username, password, key):
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    encrypted_password = encrypt_password(password, key)
    cursor.execute("INSERT INTO passwords (service, username, password) VALUES (?, ?, ?)", 
                   (service, username, encrypted_password))
    conn.commit()
    conn.close()

# Retrieve password
def get_password(service, key):
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    cursor.execute("SELECT username, password FROM passwords WHERE service=?", (service,))
    result = cursor.fetchone()
    conn.close()
    if result:
        username, encrypted_password = result
        return username, decrypt_password(encrypted_password, key)
    return None
