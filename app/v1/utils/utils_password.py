from passlib.context import CryptContext


"""
This module contains the password utility functions.
"""


class PasswordUtils:
    def __init__(self):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def verify_password(self, plain_password, password):
        return self.pwd_context.verify(plain_password, password)

    def get_password_hash(self, password):
        return self.pwd_context.hash(password)
