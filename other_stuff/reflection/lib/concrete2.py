from .somebase import SomeBase

class Concrete2(SomeBase):
    """Another skeletal class inheriting from SomeBase."""

    def __init__(self, name="awesome"):
        """Initialize the Concrete2 class with a name."""
        print("Concrete2 initialized with name:", name)
        self.name = name

    def do_something(self):
        """Implementation of the abstract method."""
        print("Concrete2 is doing something with name:", self.name)
        