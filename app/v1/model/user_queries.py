from sqlmodel import Session, select
from app.v1.model.get_engine import CreateEngine
from app.v1.model.user_model import User
from app.v1.schema.user_schema import UserRegister
from app.v1.utils.utils_password import PasswordUtils
import datetime


"""
module used to query database
"""


class UserQueries:
    def __init__(self):
        self.EngineClass = CreateEngine()
        self.EncryptClass = PasswordUtils()
        self.__engine__ = self.EngineClass.__open__()

    def check_email(self, email: str):
        with Session(self.__engine__) as session:
            statement = select(User).where(User.email == email)
            results = session.exec(statement)
            _user = results.first()
            return _user

    def create_user(self, user: UserRegister):
        with Session(self.__engine__) as session:
            session.add(User(name=user.name, email=user.email,
                             password=self.EncryptClass.get_password_hash(user.password),  # noqa: E501
                             is_active=1, last_login=datetime.datetime.utcnow,
                             last_name=user.last_name))
            session.commit()
            _user = self.check_email(user.email)
            return _user

    def get_last_login(self, user_id: int):
        with Session(self.__engine__) as session:
            statement = select(User).where(User.id == user_id)
            results = session.exec(statement)
            try:
                _user = results.first()
                return _user.last_login
            except Exception:
                return None

    def update_login(self, user_id: int):
        with Session(self.__engine__) as session:
            statement = select(User).where(User.id == user_id)
            try:
                results = session.exec(statement)
                _user = results.one()
                _user.last_login = datetime.datetime.utcnow()
                session.add(_user)
                session.commit()
                return True
            except Exception:
                return False
