[[_TOC_]]

# About
How to deserialize JSON into simple Python classes

---

# Example of JSON
```json
[
    {
        "animal": "cat",
        "age": 3,
        "name": "Whiskers"
    },
    {
        "animal": "dog",
        "age": 5,
        "name": "Buddy"
    },
    {
        "animal": "fish",
        "age": 1,
        "name": "Goldie"
    }
]
```

---
# Define a class as follows

```python
class Cat:
    def __init__(self, age, name):
        self.age = age
        self.name = name

```

# Approach

```python
    json_file=os.path.join(os.path.dirname(__file__), 'sample.json')
    with open(json_file, 'r') as f:
        data = json.load(f)

    # Deserialize into class instances
    animals = []
    for item in data:
        if item['animal'] == 'cat':
            animals.append(Cat(item['age'], item['name']))
        elif item['animal'] == 'dog':
            animals.append(Dog(item['age'], item['name']))
        elif item['animal'] == 'fish':
            animals.append(Fish(item['age'], item['name']))
        else:
            raise ValueError(f"Unknown animal type: {item['animal']}")
        

```

