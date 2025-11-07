[[_TOC_]]

# About
We are introspecting classes and functions loaded in a specific module

---

# What do we learn ?

It is possible to find all functions and classes and also classes that inherit from a specific abstract base class. But, they should all have been imported.

Now, you can load the Python files dynamically - but you will have to write code in the `__ini__.py`.

# How to use inspect to find all classes?

```python
import other_stuff.reflection.lib as lib

classes_in_lib=inspect.getmembers(lib, inspect.isclass)
```

# How to determine if a type inherits from a base class ?

```python
import other_stuff.reflection.lib as lib
classes_in_lib=inspect.getmembers(lib, inspect.isclass)
for name, cls in classes_in_lib:
    if inspect.isabstract(cls) and issubclass(cls, common.SomeBase):
        instance=cls()

```