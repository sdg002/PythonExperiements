[[_TOC_]]
# Step-by-step tutorial for learning SQLModel

SQLModel blends SQLAlchemy’s ORM with Pydantic’s data validation so you can define one model that works for both your database and your API layer, keeping your code cleaner and more consistent. Its official tutorial is structured to build concepts gradually and serves as a practical reference, with copy-pasteable, tested examples.

---

## Setup and project structure

- **Create a virtual environment:** Keep dependencies isolated.
  
  ```bash
  python -m venv .venv
  source .venv/bin/activate  # On Windows: .venv\Scripts\activate
  ```

- **Install packages:** SQLModel and a DB driver (we’ll use SQLite, included in Python).
  
  ```bash
  pip install sqlmodel
  ```

- **Project layout:**
  - **Label:** app/
  - **Label:** models.py
  - **Label:** db.py
  - **Label:** crud.py
  - **Label:** main.py
  - **Label:** tests/

SQLModel builds on Python type annotations across your models and queries, enabling powerful editor support and validation while keeping syntax familiar.

---

## Define your first model

Create a simple model with an auto-incrementing primary key and fields. SQLModel models are dataclasses-like with type hints; use `table=True` to make them persistable.

```python
# app/models.py
from typing import Optional
from sqlmodel import SQLModel, Field

class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None
```

- **Label:** `SQLModel` integrates Pydantic-style validation, so types are enforced at model creation and serialization.
- **Label:** `Field` lets you declare constraints, defaults, primary keys, and more.

The official tutorial demonstrates progressively feature-rich models, including indexes, defaults, and constraints, all driven by type hints.

---

## Create the database engine and tables

Use an SQLite file for simplicity. Tables are created from your SQLModel classes.

```python
# app/db.py
from sqlmodel import SQLModel, create_engine

sqlite_url = "sqlite:///database.db"
engine = create_engine(sqlite_url, echo=True)  # echo logs SQL

def init_db() -> None:
    SQLModel.metadata.create_all(engine)
```

- **Label:** `create_engine` configures the DB connection; `echo=True` helps you see generated SQL while learning.
- **Label:** `metadata.create_all` scans `table=True` models and creates tables.

These are standard building blocks shown in the official guide with step-by-step runnable code blocks.

---

## Sessions and basic CRUD

Sessions manage transactions. Use a context manager to ensure cleanup.

```python
# app/crud.py
from typing import Iterable, Optional, List
from sqlmodel import Session, select
from .db import engine
from .models import Hero

def create_heroes(heroes: Iterable[Hero]) -> None:
    with Session(engine) as session:
        for hero in heroes:
            session.add(hero)
        session.commit()

def get_hero_by_id(hero_id: int) -> Optional[Hero]:
    with Session(engine) as session:
        return session.get(Hero, hero_id)

def list_heroes() -> List[Hero]:
    with Session(engine) as session:
        statement = select(Hero)
        return session.exec(statement).all()

def update_hero_age(hero_id: int, age: int) -> Optional[Hero]:
    with Session(engine) as session:
        hero = session.get(Hero, hero_id)
        if not hero:
            return None
        hero.age = age
        session.add(hero)
        session.commit()
        session.refresh(hero)
        return hero

def delete_hero(hero_id: int) -> bool:
    with Session(engine) as session:
        hero = session.get(Hero, hero_id)
        if not hero:
            return False
        session.delete(hero)
        session.commit()
        return True
```

- **Label:** `Session(engine)` opens a unit of work; commit persists changes.
- **Label:** `session.get(Model, pk)` loads by primary key; `select(Model)` builds queries.
- **Label:** `session.exec(statement)` runs queries and returns results.

These operations mirror the official tutorial’s approach to inserts, selects, updates, and deletes with SQLModel’s typed queries.

---

## Put it together and run

Use a main script to initialize the DB and exercise CRUD.

```python
# app/main.py
from .db import init_db
from .crud import create_heroes, list_heroes, get_hero_by_id, update_hero_age, delete_hero
from .models import Hero

def seed() -> None:
    heroes = [
        Hero(name="Spider-Boy", secret_name="Pedro Parqueador", age=15),
        Hero(name="Captain North", secret_name="Bob Canada"),
        Hero(name="Madame Invisible", secret_name="Jane Doe", age=32),
    ]
    create_heroes(heroes)

def demo() -> None:
    all_heroes = list_heroes()
    print("All heroes:", all_heroes)

    hero = get_hero_by_id(all_heroes[0].id)
    print("First hero:", hero)

    updated = update_hero_age(all_heroes[0].id, 16)
    print("Updated:", updated)

    deleted = delete_hero(all_heroes[-1].id)
    print("Deleted last:", deleted)

if __name__ == "__main__":
    init_db()
    seed()
    demo()
```

- **Label:** `init_db()` ensures tables exist before writing.
- **Label:** Typed models ensure data consistency and friendly errors early.

The tutorial’s “Run the code” philosophy means you can copy blocks like these and see them work immediately.

---

## Queries, filters, and ordering

Use `select()` with filters and sort results.

```python
from sqlmodel import select, Session
from .db import engine
from .models import Hero

def heroes_older_than(min_age: int):
    with Session(engine) as session:
        statement = select(Hero).where(Hero.age >= min_age).order_by(Hero.age)
        return session.exec(statement).all()

def find_by_name(name_substring: str):
    with Session(engine) as session:
        statement = select(Hero).where(Hero.name.contains(name_substring))
        return session.exec(statement).all()
```

- **Label:** `.where(...)` builds typed predicates; `.order_by(...)` sorts.
- **Label:** `.contains(...)` is a convenient text predicate.

The guide walks through `where`, `select`, limit/offset pagination, and more, with clear examples.

---

## Relationships and foreign keys

Define related tables with foreign keys and use list relationships.

```python
# app/models.py (extend)
from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship

class Team(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

    heroes: List["Hero"] = Relationship(back_populates="team")

class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None
    team_id: Optional[int] = Field(default=None, foreign_key="team.id")

    team: Optional[Team] = Relationship(back_populates="heroes")
```

- **Label:** `foreign_key="team.id"` creates the linkage.
- **Label:** `Relationship` sets up bidirectional navigation.

The tutorial includes many-to-one and many-to-many relationships, plus how to join and load related data efficiently.

---

## Validation, serialization, and API integration

Because SQLModel inherits from Pydantic’s BaseModel, you get validation and `.model_dump()` (or `.dict()` in earlier versions) for JSON responses. Integrating with FastAPI is straightforward:

```python
# app/api.py
from fastapi import FastAPI
from sqlmodel import Session, select
from .db import engine, init_db
from .models import Hero

app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/heroes")
def get_heroes():
    with Session(engine) as session:
        return session.exec(select(Hero)).all()

@app.post("/heroes")
def create_hero(hero: Hero):
    with Session(engine) as session:
        session.add(hero)
        session.commit()
        session.refresh(hero)
        return hero
```

- **Label:** Models double as request/response schemas, avoiding duplicate definitions.
- **Label:** FastAPI and SQLModel share a type-first design, making endpoints concise.

This unified model approach is a core SQLModel benefit highlighted across beginner tutorials and community guides.

---

## Migrations and evolving schemas

For production, add Alembic to manage schema changes over time.

```bash
pip install alembic
alembic init migrations
```

- **Label:** Use autogenerate with SQLModel/SQLAlchemy metadata to create revision scripts.
- **Label:** Run migrations to upgrade/downgrade DB schemas safely.

Community tutorials commonly pair SQLModel with Alembic to handle migrations reliably in growing applications.

---

## Common patterns and tips

- **Label:** Separate read/write sessions. Keep sessions short; commit intentionally.
- **Label:** Use `session.refresh(obj)` after commits to get auto-generated values like IDs.
- **Label:** Prefer typed queries with `select(Model)` over raw SQL for maintainability.
- **Label:** Paginate with `limit()` and `offset()` for large result sets.
- **Label:** Start simple with SQLite; switch to Postgres by changing your URL and driver.

The official tutorial provides focused sections for inserts, selects, updates, deletes, where filters, limit/offset, indexes, and project structure, each with tested examples you can reuse.

---

## Next steps

- **Label:** Explore the full SQLModel tutorial sections end-to-end to deepen mastery and use as a reference when you’re stuck.
- **Label:** Build a small FastAPI app with SQLModel models and test endpoints to practice the validation/ORM synergy.
- **Label:** Add Alembic once your schema starts changing to keep databases in sync across environments.

If you share your target database (SQLite vs Postgres) and the shape of your data, I’ll tailor the model and queries to your exact needs.