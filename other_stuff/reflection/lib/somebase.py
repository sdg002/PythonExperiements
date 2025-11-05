from abc import ABC, abstractmethod

class SomeBase(ABC):
    """A simple abstract base class."""

    @abstractmethod
    def do_something(self):
        """Abstract method to be implemented by subclasses."""
        pass