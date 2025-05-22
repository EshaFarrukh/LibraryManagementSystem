from models.db import get_connection
import datetime

def return_book(lending_id):
    conn = get_connection()
    cursor = conn.cursor()
    return_date = datetime.date.today()

    cursor.execute("SELECT due_date FROM lendings WHERE id = %s", (lending_id,))
    due = cursor.fetchone()[0]
    delta = (return_date - due).days
    fine = max(0, delta * 10)

    cursor.execute("INSERT INTO returns (lending_id, return_date, fine) VALUES (%s, %s, %s)", (lending_id, return_date, fine))
    cursor.execute("UPDATE lendings SET returned = TRUE WHERE id = %s", (lending_id,))
    conn.commit()
    conn.close()
    return fine
