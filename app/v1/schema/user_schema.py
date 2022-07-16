from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr


"""
Schema for User
"""


class UserLogin(BaseModel):
    email: EmailStr = Field(..., example="email@eurekalabs.io")
    password: str = Field(...,
                          min_length=8,
                          max_length=64,
                          example="strongpass")


class UserBase(BaseModel):
    email: EmailStr = Field(..., example="email@eurekalabs.io")
    name: str = Field(...,
                      min_length=3,
                      max_length=50,
                      example="Anthony")
    last_name: str = Field(...,
                           min_length=3,
                           max_length=50,
                           example="Diaz")


class User(UserBase):
    id: int = Field(..., example="5")


class UserRegister(UserBase):
    password: str = Field(...,
                          min_length=8,
                          max_length=64,
                          example="strongpass")
