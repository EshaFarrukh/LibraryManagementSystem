import tkinter as tk
from tkinter import messagebox
from models.user import register_user

class RegistrationWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Register New User")
        self.root.geometry("300x250")

        tk.Label(root, text="Username").pack()
        self.username_entry = tk.Entry(root)
        self.username_entry.pack()

        tk.Label(root, text="Password").pack()
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack()

        tk.Label(root, text="Role (admin/member)").pack()
        self.role_entry = tk.Entry(root)
        self.role_entry.pack()

        tk.Button(root, text="Register", command=self.register).pack(pady=10)

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        role = self.role_entry.get()

        if register_user(username, password, role):
            messagebox.showinfo("Success", "User registered!")
            self.root.destroy()
        else:
            messagebox.showerror("Error", "Registration failed!")