# app/views/login_view.py

import tkinter as tk
from tkinter import ttk, messagebox
from app.services.login_services import authenticate


class LoginView(ttk.Frame):
    def __init__(self, parent, switch_to_dashboard):
        super().__init__(parent)
        self.parent = parent
        self.switch_to_dashboard = switch_to_dashboard
        self.build_ui()

    def build_ui(self):
        ttk.Label(self, text="Login", font=("Arial", 20)).pack(pady=20)

        ttk.Label(self, text="Username:").pack()
        self.username_entry = ttk.Entry(self)
        self.username_entry.pack()

        ttk.Label(self, text="Password:").pack()
        self.password_entry = ttk.Entry(self, show="*")
        self.password_entry.pack()

        ttk.Button(
            self,
            text="Login",
            command=self.handle_login
        ).pack(pady=10)

    def handle_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if authenticate(username, password):
            messagebox.showinfo("Success", "Logged in successfully!")
            self.switch_to_dashboard()   # Move to next page
        else:
            messagebox.showerror("Error", "Invalid username or password")
