from singleton.mysingleton1 import MyClass
from singleton.mysingleton2 import MySingleton2
from singleton.mysingleton3 import MySingleton3

def do_something3():
    print("Inside do_something3 of another class")
    x1=MySingleton3(someparam="from another client")
    print(x1)
    print("--------------------------------")

def do_something():
    print("Inside do_something of another class")
    y=MyClass.instance1()
    print(y)
    print("----aonther instance")
    x=MyClass.instance2()
    print(x)
    print(f"Going to create another instance of {MySingleton2}")
    x1=MySingleton2()
    print(x1)

