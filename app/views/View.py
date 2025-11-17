# app/views/View.py

import tkinter as tk
from tkinter import ttk


class DashboardView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.build_ui()

    # ---------------------------
    # DASHBOARD UI LAYOUT
    # ---------------------------
    def build_ui(self):
        title = ttk.Label(self, text="Library Dashboard", font=("Arial", 26))
        title.pack(pady=25)

        # Container for buttons
        button_frame = ttk.Frame(self)
        button_frame.pack(pady=20)

        # Button configuration
        buttons = [
            ("📚 Add Book", self.handle_add_book),
            ("❌ Remove Book", self.handle_remove_book),
            ("🧍 Member Registration", self.handle_member_registration),
            ("📤 Issue / Lend Book", self.handle_lend_book),
            ("📥 Return Book", self.handle_return_book),
            ("📊 Inventory Report", self.handle_inventory),
            ("💰 Fine Calculation", self.handle_fine_calc),
            ("🚪 Logout", self.handle_logout),
        ]

        # Create each button
        for text, command in buttons:
            btn = ttk.Button(button_frame, text=text, command=command)
            btn.pack(pady=8, ipadx=25, ipady=5)

    # ---------------------------
    # HANDLERS (Blank for now)
    # ---------------------------
    def handle_add_book(self):
        print("Add Book clicked")

    def handle_remove_book(self):
        print("Remove Book clicked")

    def handle_member_registration(self):
        print("Member Registration clicked")

    def handle_lend_book(self):
        print("Lend Book clicked")

    def handle_return_book(self):
        print("Return Book clicked")

    def handle_inventory(self):
        print("Inventory clicked")

    def handle_fine_calc(self):
        print("Fine Calculation clicked")

    def handle_logout(self):
        print("Logout clicked")
        # Go back to login
        self.master.show_login()  # Uses MainApp's method
