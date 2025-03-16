import sys


def do_some_work():
    print(f"Hello world, found {len(sys.argv)} command line arguments")
    print(f"sys.executable={sys.executable}")
    print(f"sys.path={sys.path}")
    print(f"__file__={__file__}")
    print("---------------------")
    print("Displaying the command line arguments")
    for index,arg in enumerate(sys.argv):
        print(f"\t{index}.....{arg}")
    print("Displaying the command line arguments")


def display_modules():
    from importlib import metadata as importlib_metadata
    print("-----------Available modules-----------")
    dists = importlib_metadata.distributions()
    for dist in dists:
        name = dist.metadata["Name"]
        version = dist.version
        #license = dist.metadata["License"]
        print(f'found distribution {name}=={version}')
    print("-----------Available modules-----------")

def outer_func():
    exit_code =0
    try:
        do_some_work()
        display_modules();
        exit_code=int(sys.argv[1])
        print(f"The exit code {exit_code} will be used")
    except Exception as err:
        print("Exception was raised")
        print(str(err))
        exit_code=999
    sys.exit(exit_code)

if __name__ == "__main__":
    outer_func()
