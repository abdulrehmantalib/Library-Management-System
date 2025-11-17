from models.user import User


# simple static user for demonstration
ADMIN = User("admin", "admin123")




def authenticate_user(username, password):
"""Return True if username/password is correct."""
return username == ADMIN.username and ADMIN.check_password(password)