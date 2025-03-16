#from .myclass import MyClass
from singleton.mysingleton3 import MySingleton3
from singleton.anotherclient import do_something3


if __name__ == "__main__":
    print(f"Going to create instance of {MySingleton3}")
    y=MySingleton3(someparam="instance_y")
    print(y)
    print("Going to call another module")
    do_something3()
    print(f"Going to create another instance of {MySingleton3}")
    x1=MySingleton3(someparam="instance_x1")
    print(x1)
