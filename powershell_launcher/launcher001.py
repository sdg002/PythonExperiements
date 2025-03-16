#How to use this script?
#-----------------------
#Launch a CMD
#Set the environment variables
#Launch a child CMD
#Run the following command:
#"c:\Program files\Python39\python.exe" C:\Users\saurabhd\MyTrials\Python\any-python\powershell_launcher\launcher.py arg1 1233
#

import os
import sys
import shutil
import subprocess

#
#Capture the environment variables
#
root_source_folder=os.environ["destination_source_folder"]
venv_folder=os.environ["venv_folder"] #TODO rename to destination_venv_folder
current_folder=os.path.dirname(__file__)
target_python_abs_path=os.path.join(root_source_folder,sys.argv[1])
target_python_args=sys.argv[2:]
requirements_file=os.path.join(root_source_folder,"requirements.txt")

print(f"Current folder is {current_folder}")
print(f"Going to copy over to: {root_source_folder}")
print(f"Target python file: {target_python_abs_path}")
print(f"Targe arguments: {target_python_args}")
print(f"Requirements file: {requirements_file}")
#
#Display base interpreter Python version
#
p=subprocess.Popen((sys.executable,"--version"))
p.wait()

#
#Delete the destination source folder if it exists
#
if os.path.exists(root_source_folder):
    print(f"The folder:{root_source_folder} exists. Going to delete")
    shutil.rmtree(path=root_source_folder)
    print(f"The folder:{root_source_folder} was deleted")
#
#Copy over the code to the destination source
#
shutil.copytree(src=current_folder,dst=root_source_folder)
print(f"Copying source code to {root_source_folder} complete")
#
#Create the VENV folder if not found
#
if not os.path.exists(venv_folder):
    os.mkdir(venv_folder)
    print(f"The folder {venv_folder} was created")

print("Displaying cmdline arguments")
print(sys.argv)
#
#Install the requirements in the VENV
#
print(f"Begin-Install VENV in the folder {venv_folder}")
# cmd=f"'{sys.executable}' -m venv {venv_folder}"
# cmd=f'"{sys.executable}" --version'
# print(f"Going to run '{cmd}'")
# os.system(sys.executable)
#
#Create VENV
#
print("------------Begin VENV creation------------")
p=subprocess.Popen((sys.executable,"-m", "venv", venv_folder))
p.wait()
if p.returncode != 0:
    print(f"Fail! Python returned a non-zero exit code {p.returncode}. Quitting")
    sys.exit(p.returncode)

print(f"End-Install VENV in the folder {venv_folder}")
print("------------End VENV creation------------")
#
#Setup the environment variables before launching Python in VENV interpreter
#
env_path=os.environ["path"]
new_python_interpreter_dir=os.path.join(venv_folder,"Scripts")
new_python_interpreter_exe=os.path.join(new_python_interpreter_dir,"python.exe")
print(f"New python intepreter path is: {new_python_interpreter_dir}")
env_new_path=f"{new_python_interpreter_dir};{env_path}"
os.environ["path"]=env_new_path
#
#PIP install requirements in VENV
#
print("------------Begin requirements------------")
print(f"Going to install requirements file: {requirements_file}")
cmd=(new_python_interpreter_exe,"-m","pip","install","-r", requirements_file)
p=subprocess.Popen(tuple(cmd))
p.wait()
print("------------End requirements------------")
if p.returncode != 0:
    print(f"Fail! PIP install returned a non-zero exit code {p.returncode}. Quitting")
    sys.exit(p.returncode)
#
#Launch Python in VENV interpreter
#
print(f"Going to launch the file: {target_python_abs_path}")
cmd=[new_python_interpreter_exe,target_python_abs_path]
cmd.extend(target_python_args)
print(f"------------Begin {target_python_abs_path}------------")
p=subprocess.Popen(tuple(cmd))
p.wait()
print("------------Complete------------")
print(f"Exit code from child process was: {p.returncode}")
sys.exit(p.returncode)
#
#Follow this
#https://stackoverflow.com/a/62219010/2989655
#
#activate_script=YOU WERE HERE  - HOW TO RUN PIP ON VENV
#HOW TO ACTIVATE
