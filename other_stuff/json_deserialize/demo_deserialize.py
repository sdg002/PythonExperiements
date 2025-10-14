import json
import os
from abc import ABC, abstractmethod

# Define an abstract base class
class AnimalBase(ABC):
    def __init__(self, age, name):
        self.age = age
        self.name = name

    @abstractmethod
    def speak(self):
        pass

# Modify Cat, Dog, and Fish to inherit from AnimalBase
class Cat(AnimalBase):
    def speak(self):
        return "Meow"

class Dog(AnimalBase):
    def speak(self):
        return "Woof"

class Fish(AnimalBase):
    def speak(self):
        return "Blub"

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
        print(type(animal).__name__, animal.name, animal.age, animal.speak())
        pass

if __name__ == "__main__":
    main()
    pass