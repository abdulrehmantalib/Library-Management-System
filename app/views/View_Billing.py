import tkinter as tk
from tkinter import ttk




class BillingWindow(ttk.Frame):
def __init__(self, parent):
super().__init__(parent)
self.build_ui()


def build_ui(self):
ttk.Label(self, text="Billing", font=("Arial", 18)).pack(pady=20)
ttk.Label(self, text="(Billing UI content here)").pack(pady=10)