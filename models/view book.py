import tkinter as tk
from tkinter import messagebox
from models.book import add_book, remove_book

class BookUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Manage Books")
        self.root.geometry("350x300")

        tk.Label(root, text="Title").pack()
        self.title_entry = tk.Entry(root)
        self.title_entry.pack()

        tk.Label(root, text="Author").pack()
        self.author_entry = tk.Entry(root)
        self.author_entry.pack()

        tk.Label(root, text="Quantity").pack()
        self.qty_entry = tk.Entry(root)
        self.qty_entry.pack()

        tk.Button(root, text="Add Book", command=self.add).pack(pady=5)
        tk.Button(root, text="Remove Book", command=self.remove).pack(pady=5)

    def add(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        try:
            quantity = int(self.qty_entry.get())
            add_book(title, author, quantity)
            messagebox.showinfo("Success", "Book added!")
        except ValueError:
            messagebox.showerror("Error", "Quantity must be a number.")

    def remove(self):
        title = self.title_entry.get()
        if remove_book(title):
            messagebox.showinfo("Removed", "Book removed.")
        else:
            messagebox.showerror("Error", "Book not found.")