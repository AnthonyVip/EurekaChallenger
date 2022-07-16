from typing import Optional
from sqlmodel import Field, SQLModel
from datetime import datetime


"""
here we define the User table model for singup
"""


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    password: str
    email: str
    last_name: str
    is_active: int = Field(default=1)
    date_joined: datetime = Field(default_factory=datetime.utcnow)
    last_login: datetime = Field(default_factory=datetime.utcnow)
