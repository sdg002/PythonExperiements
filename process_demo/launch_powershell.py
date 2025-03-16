from subprocess import Popen, PIPE
import datetime



if __name__ =="__main__":
    print("Hello world")
    process = Popen(['powershell.exe', '-file', 'child_powershell.ps1', ])
