"""
First model - we are trying to create a model with invalid data to see validation error.
"""

from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    is_active: bool = True  # default value


User(id="not-an-int", name="Bob")
