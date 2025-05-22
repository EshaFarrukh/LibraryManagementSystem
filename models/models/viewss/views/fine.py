import tkinter as tk
from models.return import return_book

class FineCalculatorUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Fine Calculator")
        self.root.geometry("300x200")

        tk.Label(root, text="Lending ID").pack()
        self.lend_id_entry = tk.Entry(root)
        self.lend_id_entry.pack()

        tk.Button(root, text="Calculate Fine", command=self.calculate).pack(pady=10)
        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def calculate(self):
        lend_id = int(self.lend_id_entry.get())
        fine = return_book(lend_id)  # Caution: this also marks returned!
        self.result_label.config(text=f"Fine: Rs. {fine}")
