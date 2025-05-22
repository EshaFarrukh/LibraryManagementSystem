import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="library_db"
    )

def register_user(username, password, role):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password, role) VALUES (%s, %s, %s)",
                       (username, password, role))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print("Error:", e)
        return False