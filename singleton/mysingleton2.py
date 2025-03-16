import datetime

class MySingleton2(object):
    def __init__(self) -> None:
        pass
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(MySingleton2, cls).__new__(cls)
        return cls.instance
  
    def __str__(self) -> str:
        return f"This is {type(self)} {id(self)}"

