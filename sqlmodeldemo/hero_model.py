from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine, select


# app/models.py
from typing import Optional
from sqlmodel import SQLModel, Field


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None
