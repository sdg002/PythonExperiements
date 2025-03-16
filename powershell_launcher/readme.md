[[_TOC_]]

# Purpose
- To help in launching Python batch scripts from Schedulers
- Create an isolated VENV and then launch the Python script in this virtual environmen


# First Attempt
These are the files `launcher001.ps1` (with PowerShell) and `launcher001.py` (with Python). In this attemp, we re-create the virtual environment at the point of execution.

# Second Attempt
In this approach - we assume that a VENV has been created by a prior CI/CD process. We will copy over the VENV to a new folder and executed Python from here. **Attention** - It is important that we copy over because this avoids collisions with running Python jobs

# Details
- Launch any Python script with arguments
- Create a new venv in a separate folder
- Then copy over the Pyhon file(s)
- Run the specified Python file

```
C:\Users\saurabhd\MyTrials\Python\any-python\powershell_launcher\launcher.ps1 \src\demo.py arg1 arg2 "hello world 1233444"
```

# Next step
- Use a Python approach as opposed to PowerShell
- Why? Avoids another tech stack

# Usage from external scheduler
```
$ErrorActionPreference="Stop"
& $env:basepython $env:rootfolder\launcher.py arg1 arg2 arg3
```

# What are the external environment variables ?
- **basepython** - The main Python exe
- **rootfolder** - The folder where Azure Devops CI/CD will copy over the source code on the job server
- **venvfolder** - The folder which will be used for setting up a Python virtual environment
- **sourcefolder** - The folder where all the source code will be copied over and executed from
- **environment** - This can be DEV,UAT or PROD


# Progress on Attempt 2

## How to launch ?
- Start a **PowerShell** console
- Ensure base Python is in path
- Ensure that the virtual environment at `C:\Users\saurabhd\MyTrials\Python\any-python\.venv`
- 
- Set the environment variable `$env:destination_venv_folder="C:\truetemp\destination_venvs"`
- Kick off the launcher using `python C:\Users\saurabhd\MyTrials\Python\any-python\powershell_launcher\launcher002.py src\demo.py`
- 


1. Derive the path to the VENV from the local .VENV and copy this VENV
1. Create a time stamped folder under the destination .VENV folder and DONE)
1. Pass the arguments to the target Python script (YOU WERE HERE)
1. Delete old tieme stamped folders
1. Call the launcher as ActiveBatch.py
1. 
1. 


# What was I thinking about AB ?
Xcopy all source code to a TEMP folder in RELEASE   $TEMP_SRC=\\ab\ql-report\TEMP
install VENV under $TEMP_SRC\.VENV
Pip install packages to this VENV
Copy entire $TEMP_SRC\.VENV to \\ab\ql-repor\DEPLOY\$(ENVIRONMENT)
Single launcher.py under c:\petroineos\
Use single launcher


---

# Simpler approach - no need for launcher

Set the following variables

```
set DEST_SRC=\\remote\\AzureDevops\BlahReports\%ENVIRONMENT%
set DEST_VENV=$(DEST_SRC)\.devopsvenv 

```


- Devops will XCOPY the source code to $(DEST_SRC)
- Devops will kick off remote PowerShell to install venv at $(DEST_VENV)
- Do manual scheduling
- **Stop here!!!**


# Even simpler approach - no need for launcher or XCOPY - 
- Let Devops created versioned folders during VENV creation
- Make Devops set a system wide environment variable DEVOPS-MYREPO-VERSION-DEV=<pipeline version >
- This variable holds the name of the oflder with the latest VENV 
- The scheduling engine should use this variable as the path for Python interpreter

