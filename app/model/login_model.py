# app/model/login_model.py

class User:
    """
    Simple User model.
    In a real app you can extend this to use SQLite DB.
    """
    def __init__(self):
        # Hardcoded user for demo
        self.valid_username = "admin"
        self.valid_password = "admin123"

    def check_credentials(self, username, password):
        """Check if username and password match."""
        return username == self.valid_username and password == self.valid_password
