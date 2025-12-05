from typing import Optional
from sqlmodel import SQLModel, Field


class Hero(SQLModel, table=True):
    """_summary_
    Args:
        SQLModel (_type_): _description_
        table (bool, optional): _description_. Defaults to True.
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None
