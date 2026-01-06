"""
Demonstrates field constraints and metadata in Pydantic models.
In this example, we define a Person model with various field constraints.
Example: name must be between 2 and 50 characters, age must be between 0 and 120.
"""
from typing import Optional
from pydantic import BaseModel, Field


class Person(BaseModel):
    """
    A model representing a person with constrained fields.
    """
    name: str = Field(..., min_length=2, max_length=50,
                      description="Full name")
    age: int = Field(..., ge=0, le=120, description="Age in years")
    email: Optional[str] = Field(None, description="Optional email address")


p = Person(name="John Doe", age=30)
print(p)
print(p.model_dump())

try:
    Person(name="J", age=-5)
except Exception as e:
    print("\nValidation error:")
    print(e)
