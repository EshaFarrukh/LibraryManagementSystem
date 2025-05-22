import tkinter as tk

class DashboardWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Admin Dashboard")
        self.root.geometry("300x200")

        tk.Label(root, text="Welcome to Dashboard!", font=('Arial', 14)).pack(pady=20)

        tk.Button(root, text="Logout", command=root.destroy).pack()
        self.root.mainloop()