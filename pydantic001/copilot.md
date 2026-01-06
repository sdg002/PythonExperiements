[[_TOC_]]

# How to use this tutorial ?
Here’s a practical, step‑by‑step Pydantic tutorial you can follow in order. You can paste each step into a fresh `main.py` and run it.

---

# 1. What Pydantic is and how to install it

Pydantic is a Python library that uses type hints to validate and parse data into strongly-typed “models” (classes). Instead of writing manual `if` checks, you define a schema once and Pydantic validates and converts input data for you.

Install:

```bash
pip install pydantic
```

For this tutorial, we’ll assume Pydantic v2 (current major version).

---

# 2. Your first model

Create a simple `User` model and see how validation works.

```python
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    is_active: bool = True  # default value

user = User(id=1, name="Alice")
print(user)
print(user.id, user.name, user.is_active)
print(type(user.id), type(user.name), type(user.is_active))
```

Key ideas:

- **Models are classes** inheriting from `BaseModel`.
- **Attributes with type hints** become fields (`id`, `name`, `is_active`).
- **Default values** are applied when not provided.

Try passing invalid data:

```python
User(id="not-an-int", name="Bob")
```

You’ll get a detailed validation error.

---

# 3. Type coercion and validation errors

Pydantic often tries to coerce types (e.g., `"1"` → `1`) but will error when it can’t.

```python
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
```

What to notice:

- **`model_validate`** is the recommended v2 way to validate an arbitrary input object (like a dict).
- `"999.99"` becomes `float`, `"true"` becomes `bool`, but `"nine"` cannot become a float, so you get a `ValidationError`.

---

# 4. Field configuration with `Field`

Use `Field` to add constraints, defaults, and metadata like descriptions.

```python
from pydantic import BaseModel, Field

class Person(BaseModel):
    name: str = Field(..., min_length=2, max_length=50, description="Full name")
    age: int = Field(..., ge=0, le=120, description="Age in years")
    email: str | None = Field(None, description="Optional email address")

p = Person(name="John Doe", age=30)
print(p)
print(p.model_dump())

try:
    Person(name="J", age=-5)
except Exception as e:
    print("\nValidation error:")
    print(e)
```

Key points:

- **`Field(...)`** means “required”.
- Common constraints:
  - `min_length`, `max_length` for strings.
  - `ge`, `le`, `gt`, `lt` for numeric ranges.
- `email` is optional (`str | None`) with default `None`.

---

# 5. Field validators

Field validators let you run custom logic on individual fields.

```python
from pydantic import BaseModel, Field, field_validator

class UserSignup(BaseModel):
    username: str = Field(..., min_length=3)
    password: str = Field(..., min_length=8)

    @field_validator("username")
    @classmethod
    def no_spaces_in_username(cls, v: str) -> str:
        if " " in v:
            raise ValueError("Username must not contain spaces")
        return v

    @field_validator("password")
    @classmethod
    def password_complexity(cls, v: str) -> str:
        if v.isdigit() or v.isalpha():
            raise ValueError("Password must contain letters and numbers")
        return v

print(UserSignup(username="saurabh", password="abc12345"))

try:
    UserSignup(username="my user", password="abc12345")
except Exception as e:
    print("\nUsername error:")
    print(e)

try:
    UserSignup(username="saurabh", password="password")
except Exception as e:
    print("\nPassword error:")
    print(e)
```

What’s happening:

- **`@field_validator("field_name")`** gets raw input for that field.
- You can raise `ValueError` with a message, and it appears in the error output.

---

# 6. Model-level validators and derived fields

Model validators let you validate relationships between multiple fields. You can also define “computed” fields that derive from others.

```python
from pydantic import BaseModel, Field, model_validator, computed_field

class Order(BaseModel):
    quantity: int = Field(..., gt=0)
    price_per_unit: float = Field(..., gt=0)
    discount_percent: float = Field(0, ge=0, le=100)

    @model_validator(mode="after")
    def check_discount(self):
        if self.discount_percent > 50:
            raise ValueError("Discount cannot exceed 50% for any order")
        return self

    @computed_field
    @property
    def total_price(self) -> float:
        subtotal = self.quantity * self.price_per_unit
        discount = subtotal * (self.discount_percent / 100)
        return subtotal - discount

order = Order(quantity=10, price_per_unit=20.0, discount_percent=10)
print(order)
print("Total price:", order.total_price)

try:
    Order(quantity=10, price_per_unit=20.0, discount_percent=60)
except Exception as e:
    print("\nOrder error:")
    print(e)
```

Notes:

- **`model_validator(mode="after")`** sees the fully constructed model; you can enforce cross-field rules.
- **`@computed_field`** exposes derived values as if they were normal fields (included in `model_dump()` unless configured otherwise).

---

# 7. Nested models

Models can contain other models, which is powerful for structured data (APIs, configs, etc.).

```python
from pydantic import BaseModel, Field

class Address(BaseModel):
    street: str
    city: str
    country: str

class Employee(BaseModel):
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
print("\nAs dict:", employee.model_dump())
```

What to see:

- Pydantic automatically converts nested dicts into nested model instances.
- `default_factory=list` avoids using a mutable default at class definition time.

---

# 8. Serialization and parsing (JSON, dicts, etc.)

Pydantic models are meant to serialize and deserialize data easily.

```python
from pydantic import BaseModel
import json

class BlogPost(BaseModel):
    id: int
    title: str
    tags: list[str]

post = BlogPost(id=1, title="Hello Pydantic", tags=["python", "validation"])

# Model → dict
post_dict = post.model_dump()
print("Dict:", post_dict, type(post_dict))

# Model → JSON string
post_json = post.model_dump_json()
print("JSON:", post_json, type(post_json))

# JSON string → Model
data_from_json = json.loads(post_json)
post2 = BlogPost.model_validate(data_from_json)
print("Post2:", post2)
```

Key operations:

- **`model_dump()`** → Python dict.
- **`model_dump_json()`** → JSON string.
- **`model_validate(input)`** → build model from arbitrary input (dict, etc.).

---

# 9. Settings and environment variables (bonus)

Pydantic is commonly used for configuration: read env vars, validate types, set defaults.

```python
import os
from pydantic import BaseSettings

class AppSettings(BaseSettings):
    app_name: str = "MyApp"
    debug: bool = False
    database_url: str

    class Config:
        env_prefix = "MYAPP_"

# Set an environment variable for demo
os.environ["MYAPP_DATABASE_URL"] = "postgresql://user:pass@localhost:5432/db"
os.environ["MYAPP_DEBUG"] = "true"

settings = AppSettings()
print(settings)
print("Debug:", settings.debug)
print("Database:", settings.database_url)
```

- `BaseSettings` reads from environment variables, then applies validation and type conversion.
- `env_prefix` lets you have a consistent prefix for all config vars.

---

# 10. How to keep going

If you want to go deeper into best practices and more advanced patterns:

- **Real Python Pydantic guide**: good for a thorough conceptual tour with examples.
- **In-depth BaseModel guide**: covers advanced configuration, ORM mode, and real-world usage patterns.
- **Simple validation examples**: short snippets to reinforce how validation works.
- There’s also a step‑by‑step GitHub repo that walks through field validation, model validation, computed fields, nested models, and serialization with Pydantic scripts.

If you tell me what you’re planning to use Pydantic for (FastAPI APIs, ETL scripts, configs, etc.), I can tailor a next mini‑tutorial specifically to that.