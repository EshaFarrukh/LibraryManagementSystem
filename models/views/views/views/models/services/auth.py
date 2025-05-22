from models.user import get_connection

def login_user(username, password):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
        user = cursor.fetchone()
        conn.close()
        return user is not None
    except Exception as e:
        print("Login Error:", e)
        return False