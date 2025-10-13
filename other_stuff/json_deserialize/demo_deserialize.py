import json
import os

# Define classes
class Cat:
    def __init__(self, age, name):
        self.age = age
        self.name = name

class Dog:
    def __init__(self, age, name):
        self.age = age
        self.name = name

class Fish:
    def __init__(self, age, name):
        self.age = age
        self.name = name



def main():
    # Load JSON
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
        
    # Example usage
    for animal in animals:
        print(type(animal).__name__, animal.name, animal.age)
        pass

if __name__ == "__main__":
    main()
    pass