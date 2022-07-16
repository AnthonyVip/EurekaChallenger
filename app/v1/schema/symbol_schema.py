from pydantic import BaseModel
from pydantic import Field
from typing import Optional


"""
Schema for Symbol
"""


class SymbolBase(BaseModel):
    symbol: str = Field(...,
                        min_length=1,
                        max_length=15,
                        example="META")
    function: Optional[str] = Field(..., example="TIME_SERIES_DAILY")
    outputsize: Optional[str] = Field(..., example="compact")


class SymbolResponse(SymbolBase):
    data: dict
