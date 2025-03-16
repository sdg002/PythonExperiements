import os
import datetime
import time
import sys

def dump_environment_variables():
    d=datetime.datetime.now()
    file_name=d.strftime('display-%d-%m-%Y-%H-%M.log')
    print(f"The output will be written to the file: {file_name}")
    
    with open(file=file_name, mode='w+') as f: 
        f.write(f"The current time is {datetime.datetime.now()}\n")       
        f.write(f"Total command line arguments:{len(sys.argv)}\n")
        for arg in sys.argv:
            f.write(f"Argument:{arg}\n")
            print(f"Argument:{arg}\n")
        for item in os.environ.items():
            line=f"{item[0]}={item[1]}\n"
            print(line)
            f.write(line)
        f.write("Before sleep\n")
        f.flush()
        time.sleep(3.0)
        f.write("Finishing...\n")
        f.write(f"exe={sys.executable}\n")
        f.flush()
    print(f"exe={sys.executable}")
    
    pass


if __name__ =="__main__":
    dump_environment_variables()

    