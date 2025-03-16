import datetime

class MyClass(object):
    __innersingletoninstance: object  = None
    def __init__(self) -> None:
        self.clock = datetime.datetime.now()
        pass

    def __str__(self) -> str:
        return f"This is MyClass {self.clock}"

    @classmethod
    def instance1(cls):
        print(f"Going to check {cls.__innersingletoninstance}")
        if cls.__innersingletoninstance is None:
            print("...........going to create")
            cls.__innersingletoninstance = MyClass()
        return cls.__innersingletoninstance
    
    @classmethod
    def instance2(cls):
        print("Going to check 'cls.__innersingletoninstance2'")
        if not hasattr(cls,"__innersingletoninstance2"):
            print("Going to create.....")
            cls.__innersingletoninstance2 = MyClass()
        return cls.__innersingletoninstance2


