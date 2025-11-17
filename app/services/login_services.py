# app/services/login_services.py

from app.model.login_model import User

user_model = User()   # create user model instance


def authenticate(username, password):
    """
    Service layer: handles login authentication.
    Returns True or False.
    """
    return user_model.check_credentials(username, password)
