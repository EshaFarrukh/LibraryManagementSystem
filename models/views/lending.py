import tkinter as tk
from tkinter import messagebox
from models.lending import lend_book
from datetime import datetime

class LendingUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Lend Book")
        self.root.geometry("300x300")

        tk.Label(root, text="Book ID").pack()
        self.book_id_entry = tk.Entry(root)
        self.book_id_entry.pack()

        tk.Label(root, text="Member Name").pack()
        self.member_entry = tk.Entry(root)
        self.member_entry.pack()

        tk.Label(root, text="Due Date (YYYY-MM-DD)").pack()
        self.due_date_entry = tk.Entry(root)
        self.due_date_entry.pack()

        tk.Button(root, text="Lend", command=self.lend).pack(pady=10)

    def lend(self):
        try:
            book_id = int(self.book_id_entry.get())
            member = self.member_entry.get()
            due_date = datetime.strptime(self.due_date_entry.get(), "%Y-%m-%d").date()
            lend_book(book_id, member, due_date)
            messagebox.showinfo("Success", "Book lent successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to lend book: {e}")
