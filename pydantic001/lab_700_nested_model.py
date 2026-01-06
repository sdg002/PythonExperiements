from pydantic import BaseModel, Field


class Address(BaseModel):
    """
    A model representing an address with street, city, and country.
    """
    street: str
    city: str
    country: str


class Employee(BaseModel):
    """
    A model representing an employee with nested address and a list of skills.
    """
    id: int
    name: str
    address: Address
    skills: list[str] = Field(default_factory=list)


data = {
    "id": 1,
    "name": "Alice",
    "address": {
        "street": "123 High Street",
        "city": "Reading",
        "country": "UK",
    },
    "skills": ["Python", "Pydantic"],
}

employee = Employee.model_validate(data)
print(employee)
print("City:", employee.address.city)
print("Skills:", employee.skills)

# Dump to plain dict (ready for JSON, DB, etc.)
print("---- Going to dump as json ----")
print("\nAs dict:", employee.model_dump())
print("------------------------")
print("---------Create from JSON using the constructor")
employee2 = Employee(**data)
print(employee2)
