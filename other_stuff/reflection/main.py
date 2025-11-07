import inspect
import sys
import other_stuff.reflection.lib as lib
import other_stuff.reflection.common as common

def get_all_functions(module):
    """Get all functions in a module."""
    functions = inspect.getmembers(module, inspect.isfunction)
    return functions

def display_all_classes(module):
    """Get all classes in a module."""
    print(f"display_all_classes for module: {module}")
    classes_in_lib=inspect.getmembers(module, inspect.isclass)
    for name, cls in classes_in_lib:
        instance = cls()
        print(f"Instantiated {name}: {instance}")
    return classes_in_lib

def display_all_concrete_classes(module):
    """Get all concrete classes in a module."""
    print(f"display_all_concrete_classes for module: {module}")
    classes_in_lib=inspect.getmembers(module, inspect.isclass)
    concrete_instances = []
    for name, cls in classes_in_lib:
        if not inspect.isabstract(cls) and issubclass(cls, common.SomeBase):
            instance = cls("Example")
            print(f"Instantiated Concrete Class {name}: {instance}")
            concrete_instances.append((name, instance))
    print("Going to invoke method using abstract method")
    for concrete_instance in concrete_instances:
        print(f"Invoking do_something on {concrete_instance[0]}")
        instance: lib.SomeBase = concrete_instance[1]
        instance.do_something()
    print("All done")
    return concrete_instances

def display_all_functions(module):
    print("display_all_functions")
    functions_in_lib = get_all_functions(module=module)
    for name, func in functions_in_lib:
        print(f"Function Name: {name}, Function: {func}")
    print("End of display_all_functions")

def inspect_vars_items():
    for name, obj in vars(lib).items():
        print(f"Inspecting: {name} {obj}")
        if callable(obj):
            print(f"Function: {name}")
        elif isinstance(obj, type):
            print(f"Class: {name}")

if __name__ == "__main__":
    print("This is the main module for reflection.") # __path__,__file__,__cached__
    # display_all_functions(lib)
    # display_all_classes(module=lib)
    display_all_concrete_classes(module=lib)
    print("------------------------")
    print("Showing all globals")
    print(*globals(),sep="\n")
    #inspect()
    # c=lib.Class1()
    # c.method1()

    # x: lib.SomeBase = lib.Concrete1()
    # x.do_something