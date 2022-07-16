from pydantic import BaseModel
from typing import Optional


"""
Schema for Token
"""


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
