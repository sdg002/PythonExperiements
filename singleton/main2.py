#from .myclass import MyClass
from singleton.mysingleton2 import MySingleton2
from singleton.anotherclient import do_something

if __name__ == "__main__":
    print(f"Going to create instance of {MySingleton2}")
    y=MySingleton2()
    print(y)
    print("Going to call another module")
    do_something()
    do_something()
    print(f"Going to create another instance of {MySingleton2}")
    x1=MySingleton2()
    print(x1)
