# What was I trying ?
Create a singleton instance of a class using Python

# Lessons learnt
The private class variable should be initialized to None otherwise Python does not recognize it
Now we understand the complexity
you were reading this
https://www.geeksforgeeks.org/singleton-pattern-in-python-a-complete-guide/

# How to use hasattr and create a singleton instance

```python

class SingletonClass(object):
  def __new__(cls):
    if not hasattr(cls, 'instance'):
      cls.instance = super(SingletonClass, cls).__new__(cls)
    return cls.instance

```

# How to pass parameters to __new__ ?

```python
class MySingleton3:
    def __init__(self, someparam: str) -> None:
        self._someparam=someparam

    def __new__(cls,someparam: str):
        print(f"Inside __new__ {someparam=}")
        if not hasattr(cls, 'instance'):
            cls.instance = super(MySingleton3, cls).__new__(cls)
        return cls.instance

    def __str__(self) -> str:
        return f"This is {type(self)} {id(self)} , {self._someparam=}"

```
```python
y=MySingleton3(someparam="instance_y")
```


# What was the first approach ?
Use a classmethod named `instance()` which exposes an internal variable that stores the actual singleton instance.

# What was the second approach ?
Similar to the first, but use the `hasattr` method to dynamically create the internal member variable

# What was the third approach ?
Use the `hasattr` to dynamically create the internal member variable. Most importantly use the `__new__` method

# Is it truly singleton?
So it appears. I got the same instance when instantiated in other functions

# Why not use double underscore to name the internal singleton instance ?
The outer classmethod is unable to access the instance
