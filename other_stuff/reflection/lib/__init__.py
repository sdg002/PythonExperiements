# This was the original approach - this is vanilla and one by one
# from .class1 import Class1
# from .class2 import Class2
# from .somebase import SomeBase
# from .concrete1 import Concrete1
# from .concrete2 import Concrete2

import os
import importlib

# Dynamically import all modules in the current folder
current_dir = os.path.dirname(__file__)
print(f"Going to import from {current_dir} , {__name__=}")
for filename in os.listdir(current_dir):
    if not filename.endswith(".py"):
        continue
    if filename == "__init__.py":
        continue
    module_name = filename[:-3]  # Remove the .py extension
    # the following imports the files
    module = importlib.import_module(f".{module_name}", package=__name__)
    print(f"Imported module: {module_name}")

    # Import all classes from the module and add them to the lib module
    print("Gloal namespace-going to add")
    for name, obj in vars(module).items():
        if isinstance(obj, type):  # Check if the object is a class
            print(f"{name} : {obj}")
            globals()[name] = obj
            print(f"Added class {name} to lib module")
    print("Global namespace-added")
    print("------------------------")
