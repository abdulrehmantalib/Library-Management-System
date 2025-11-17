import sys
import unittest
import tkinter as tk

from app.views.login_view import LoginView
from app.views.View import DashboardView


class MainApp(tk.Tk):
    """Main Tkinter application controller."""

    def __init__(self):
        super().__init__()
        self.title("Library Management System")
        self.geometry("900x600")

        self.show_login()

    def clear_window(self):
        """Clear entire window before switching screens."""
        for widget in self.winfo_children():
            widget.destroy()

    def show_login(self):
        """Open login window."""
        self.clear_window()
        login_page = LoginView(self, self.show_dashboard)
        login_page.pack(fill="both", expand=True)

    def show_dashboard(self):
        """Open dashboard window."""
        self.clear_window()
        dashboard = DashboardView(self)
        dashboard.pack(fill="both", expand=True)


# ------------------------------------------------
# UNIT TEST RUNNER (NO pytest needed)
# ------------------------------------------------
def run_tests():
    """
    Discover and run all unit tests inside /tests directory
    using Python's built-in unittest.
    """
    print("\n🔍 Running unit tests...\n")

    loader = unittest.TestLoader()
    suite = loader.discover("tests")

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

    print("\n✅ Tests finished.\n")


# ------------------------------------------------
# MAIN ENTRY
# ------------------------------------------------
def main():
    # If argument "test" is provided → run tests
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        run_tests()
        return

    # Otherwise, start the GUI normally
    app = MainApp()
    app.mainloop()


if __name__ == "__main__":
    main()
