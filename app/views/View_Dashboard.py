import tkinter as tk
from tkinter import ttk
from views.billing import BillingWindow




class DashboardWindow(ttk.Frame):
def __init__(self, parent):
super().__init__(parent)
self.build_ui()


def build_ui(self):
ttk.Label(self, text="Dashboard", font=("Arial", 18)).pack(pady=20)


ttk.Button(self, text="Open Billing", command=self.open_billing).pack(pady=10)


def open_billing(self):
self.destroy()
BillingWindow(self.master).pack(fill="both", expand=True)