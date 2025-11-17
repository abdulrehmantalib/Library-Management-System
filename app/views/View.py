# app/views/View.py

import tkinter as tk
from tkinter import ttk


class DashboardView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        ttk.Label(self, text="Welcome to Dashboard!", font=("Arial", 20)).pack(pady=20)
