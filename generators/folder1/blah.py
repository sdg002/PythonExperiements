import sys

def hello_hello():
    print("Inside hello_hello")
    print("Going to display syspath")
    
    paths=sys.path
    paths.sort(key=len)
    print(*paths, sep="\n")
    pass


hello_hello()
