#from .myclass import MyClass
from singleton.mysingleton1 import MyClass
from singleton.anotherclient import do_something

if __name__ == "__main__":
    # x=MyClass()
    # MyClass._innersingletoninstance=MyClass()  #this works
    # print(x)


    y=MyClass.instance1()
    print(y)
    print(MyClass.instance1())
    print("Going to call another module")
    do_something()
    do_something()
    x1=MyClass.instance1()
    print(x1)
