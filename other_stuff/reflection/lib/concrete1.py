from ..common.somebase import SomeBase

class Concrete1(SomeBase):
    """A skeletal class inheriting from SomeBase."""

    def __init__(self, name="cool"):
        """Initialize the Concrete1 class with a name."""
        print("Concrete1 initialized with name:", name)
        self.name = name

    def do_something(self):
        """Implementation of the abstract method."""
        print("Concrete1 is doing something with name:", self.name)
        pass
