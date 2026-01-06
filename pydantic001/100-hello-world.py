"""
First model - just create a model and see how pydantic works.
"""

from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    is_active: bool = True  # default value


user = User(id=1, name="Alice")
print(user)
print(user.id, user.name, user.is_active)
print(type(user.id), type(user.name), type(user.is_active))
print("We can see the types are correctly inferred and assigned.")
