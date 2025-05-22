import tkinter as tk
from models.book import load_books

class InventoryReport:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Report")
        self.root.geometry("400x300")

        self.text_area = tk.Text(root, wrap=tk.WORD)
        self.text_area.pack(expand=True, fill="both")

        self.show_inventory()

    def show_inventory(self):
        books = load_books()
        if not books:
            self.text_area.insert(tk.END, "No books found.\n")
        for book in books:
            line = f"Title: {book['title']}, Author: {book['author']}, Qty: {book['quantity']}\n"
            self.text_area.insert(tk.END, line)