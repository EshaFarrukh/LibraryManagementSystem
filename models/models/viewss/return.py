import tkinter as tk
from tkinter import messagebox
from models.return import return_book

class ReturnUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Return Book")
        self.root.geometry("300x200")

        tk.Label(root, text="Lending ID").pack()
        self.lend_id_entry = tk.Entry(root)
        self.lend_id_entry.pack()

        tk.Button(root, text="Return", command=self.return_book).pack(pady=10)

    def return_book(self):
        try:
            lend_id = int(self.lend_id_entry.get())
            fine = return_book(lend_id)
            messagebox.showinfo("Returned", f"Book returned.\nFine: Rs. {fine}")
        except Exception as e:
            messagebox.showerror("Error", str(e))
