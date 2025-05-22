from models.db import get_connection
import datetime

def lend_book(book_id, member_name, due_date):
    conn = get_connection()
    cursor = conn.cursor()
    lend_date = datetime.date.today()
    cursor.execute(
        "INSERT INTO lendings (book_id, member_name, lend_date, due_date) VALUES (%s, %s, %s, %s)",
        (book_id, member_name, lend_date, due_date)
    )
    conn.commit()
    conn.close()

def get_active_lendings():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM lendings WHERE returned = FALSE")
    results = cursor.fetchall()
    conn.close()
    return results
