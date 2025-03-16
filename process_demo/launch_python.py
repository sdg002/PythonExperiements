print("Hello world")
from subprocess import Popen, PIPE
import subprocess
import datetime
import time

def generate_timestamped_filename(identifier: str):
    d=datetime.datetime.now()
    file_name=d.strftime(f'{identifier}-%d-%m-%Y-%H-%M.log')
    print(f"The output will be written to the file: {file_name}")
    return file_name


def launch_child_process(identifier: str):
    stdout_filename=generate_timestamped_filename(identifier=f'{identifier}-stdout')
    #f"{identifier}-child-proc-stdout.txt"
    stderr_filename=generate_timestamped_filename(identifier=f'{identifier}-stderr')
    #f"{identifier}-child-proc-stderr.txt"
    with open(stdout_filename,"wb") as stdout, open(stderr_filename,"wb") as stderr:
        process = Popen(['python.exe', 'child_proc.py', 'hello world', '100','200', 'procidentifer',identifier], stdout=stdout, stderr=stderr)
    print(process)
    print("Done")
    pass

def launch_child_process2(identifier: str):
    #
    #Same file for stdout and stderr
    #
    stdout_filename=generate_timestamped_filename(identifier=f'{identifier}-stdout')
    stdout=open(stdout_filename,"wb")
    process = Popen(['ping.exe', 'www.google.com', '-t' ], stdout=stdout, stderr=subprocess.STDOUT)
    print("Done with lauunch child process 2")
    pass

if __name__ =="__main__":
    #launch_child_process(identifier='proc001')
    #launch_child_process(identifier='proc002')
    launch_child_process2(identifier="pingtest")
    print("Waiting...")
    time.sleep(50)
    print("Wait complete")