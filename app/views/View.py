import tkinter as tk
from tkinter import ttk, messagebox
from services.auth import authenticate_user




class LoginWindow(ttk.Frame):
def __init__(self, parent):
super().__init__(parent)
self.parent = parent
self.build_ui()


def build_ui(self):
ttk.Label(self, text="Login", font=("Arial", 20)).pack(pady=20)


self.username = ttk.Entry(self)
self.username.pack(pady=5)
self.username.insert(0, "admin")


self.password = ttk.Entry(self, show='*')
self.password.pack(pady=5)
self.password.insert(0, "admin123")


ttk.Button(self, text="Login", command=self.handle_login).pack(pady=10)


def handle_login(self):
user = self.username.get()
pwd = self.password.get()


if authenticate_user(user, pwd):
messagebox.showinfo("Success", "Login successful!")
from views.dashboard import DashboardWindow
self.destroy()
DashboardWindow(self.parent).pack(fill="both", expand=True)
else:
messagebox.showerror("Error", "Invalid credentials")