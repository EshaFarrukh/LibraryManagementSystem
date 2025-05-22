import json
import os

BOOK_FILE = 'books.json'

def load_books():
    if not os.path.exists(BOOK_FILE):
        return []
    with open(BOOK_FILE, 'r') as file:
        return json.load(file)

def save_books(books):
    with open(BOOK_FILE, 'w') as file:
        json.dump(books, file, indent=4)

def add_book(title, author, quantity):
    books = load_books()
    for book in books:
        if book['title'].lower() == title.lower():
            book['quantity'] += quantity
            save_books(books)
            return True
    books.append({"title": title, "author": author, "quantity": quantity})
    save_books(books)
    return True

def remove_book(title):
    books = load_books()
    updated_books = [book for book in books if book['title'].lower() != title.lower()]
    if len(books) == len(updated_books):
        return False  # Book not found
    save_books(updated_books)
    return True