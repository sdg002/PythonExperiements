"""
    this is a summary
"""
import sys
import os
import shutil
import time
import subprocess
import datetime

def copy_venv_folder(src_venv_folder: str, dest_venv_folder: str)->None:
    # if not os.path.exists(dest_venv_folder):
    #     print(f"Begin-Going to create the destination {dest_venv_folder}")
    #     start=time.time()
    #     shutil.copytree(src=src_venv_folder, dst=dest_venv_folder)
    #     end=time.time()
    #     print(f"End-Going to create the destination {dest_venv_folder}, elapsed={end-start} secs")
    # else:
    #     print(f"Not creating the destination {dest_venv_folder} because it already exists")
    print(f"Begin-Going to copy from {src_venv_folder=}  to {dest_venv_folder=}")
    start=time.time()
    shutil.copytree(src=src_venv_folder, dst=dest_venv_folder, dirs_exist_ok=True)
    end=time.time()
    print(f"End-Going to copy from {src_venv_folder=}  to {dest_venv_folder=}, elapsed={round(end-start,1)} secs")

def launch_python_script(dest_venv_folder: str, target_python: str):
    print(f"launch_python_script {target_python=} , {dest_venv_folder=}")
    env_path=os.environ["path"]
    new_python_interpreter_dir=os.path.join(dest_venv_folder,"Scripts")
    new_python_interpreter_exe=os.path.join(new_python_interpreter_dir,"python.exe")
    print(f"New python intepreter path is: {new_python_interpreter_dir}")
    env_new_path=f"{new_python_interpreter_dir};{env_path}"
    os.environ["path"]=env_new_path

    print(f"Going to launch the file: {target_python} using Python from:{new_python_interpreter_exe}")
    cmd=[new_python_interpreter_exe,target_python]
    target_python_args=["arg 100" ,"arg 200", "replace from sys.argv"]
    cmd.extend(target_python_args)
    print(f"------------Begin {target_python}------------")
    p=subprocess.Popen(tuple(cmd))
    p.wait()
    print("------------Complete------------")
    print(f"Exit code from child process was: {p.returncode}")
    sys.exit(p.returncode)

    pass


def clean_up_old_venv_folders(root_venv_folder: str):
    print(f"clean_up_old_venv_folders, {root_venv_folder}")
    pass


def create_new_venv_folder(root_folder: str)->str:
    """Summar comes here

    Args:
        root_folder (str): The base folder where all VENVS will be created

    Returns:
        str: The absolute path to the newly created VENV sub-folder
    """
    new_folder_name=datetime.datetime.now().strftime("%d-%B-%Y-%H-%m-%S")
    new_folder_path=os.path.join(root_folder,new_folder_name,".venv")
    os.makedirs(new_folder_path)
    print(f"New folder for VENV was created at:{new_folder_path}")
    return new_folder_path

if __name__ =="__main__":
    current_folder=os.path.dirname(__file__)
    #root_source_folder=os.environ["destination_venv_folder"] #should be desti-ven-folder
    DESTINATION_VENV_FOLDER_ROOT="c:/truetemp/destination_venvs/" #Should be all venvs under a 1 root - this helps clean up
    new_venv_folder: str=create_new_venv_folder(root_folder=DESTINATION_VENV_FOLDER_ROOT)
    target_python_abs_path=os.path.join(os.path.dirname(__file__),sys.argv[1])
    copy_venv_folder(src_venv_folder="C:/truetemp/general-python-venv/.venv", dest_venv_folder=new_venv_folder)
    launch_python_script(dest_venv_folder=new_venv_folder, target_python=target_python_abs_path)
    clean_up_old_venv_folders(root_venv_folder=DESTINATION_VENV_FOLDER_ROOT)
