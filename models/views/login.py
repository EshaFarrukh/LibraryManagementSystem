import tkinter as tk
from tkinter import messagebox
from services.auth import login_user

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Login")
        self.root.geometry("300x200")

        tk.Label(root, text="Username").pack()
        self.username_entry = tk.Entry(root)
        self.username_entry.pack()

        tk.Label(root, text="Password").pack()
        self.password_entry = tk.Entry(root, show='*')
        self.password_entry.pack()

        tk.Button(root, text="Login", command=self.login).pack(pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if login_user(username, password):
            messagebox.showinfo("Success", "Login Successful!")
            self.root.destroy()
            from views.dashboard import DashboardWindow
            DashboardWindow(tk.Tk())  # Open dashboard
        else:
            messagebox.showerror("Error", "Invalid credentials")