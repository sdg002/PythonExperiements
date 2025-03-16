"""
Singleton
"""



class MySingleton3:
    """
    Sample class that shows how to pass ctor parameters when using __new__
    """
    def __init__(self, someparam: str) -> None:
        self._someparam=someparam

    def __new__(cls,someparam: str):
        print(f"Inside __new__ {someparam=}")
        if not hasattr(cls, 'instance'):
            cls.instance = super(MySingleton3, cls).__new__(cls)
        return cls.instance

    def __str__(self) -> str:
        return f"This is {type(self)} {id(self)} , {self._someparam=}"
