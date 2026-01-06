"""
Demonstrates type coercion in Pydantic models.
In this example we are validating a JSON before creating the model instance.
"""
from pydantic import BaseModel, ValidationError


class Product(BaseModel):
    name: str
    price: float
    in_stock: bool


data_ok = {"name": "Laptop", "price": "999.99", "in_stock": "true"}
data_bad = {"name": "Laptop", "price": "nine", "in_stock": "yes"}

print("=== OK DATA ===")
product_ok = Product.model_validate(data_ok)
print(product_ok)
print(type(product_ok.price), type(product_ok.in_stock))

print("\n=== BAD DATA ===")
try:
    product_bad = Product.model_validate(data_bad)
except ValidationError as e:
    print(e)
