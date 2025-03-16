$ErrorActionPreference="Stop"

Write-Host "Display command line arguments. Count: $($args.Length)"

$args



if ($args.Length -lt 1)
{
    Write-Error -Message "The first argument should be the relative path of the Python file, second "
}

$PythonFile=$args[0]
$DestinationBaseFolder="C:\truetemp\python_launcher_demo"
$VenvFolder=Join-Path -Path $DestinationBaseFolder -ChildPath "virtualvenv"
$SourceCopyFolder=Join-Path -Path $DestinationBaseFolder -ChildPath "source"

$CurrentFolder=$PSScriptRoot
$PythonBaseInterpreter="C:\Program Files\Python39\python.exe"
$PythonAbsoluteFile=Join-Path -Path $SourceCopyFolder -ChildPath $PythonFile
$ActivateScript = Join-Path -Path $VenvFolder -ChildPath "Scripts\Activate.ps1"
$VenvPythonInterpreter=Join-Path -Path $VenvFolder -ChildPath "Scripts\Python.exe"
$RequirementsFile=Join-Path -Path $SourceCopyFolder -ChildPath "requirements.txt"

#######################################################

#copy over
if (Test-Path -Path $VenvFolder)
{
    Remove-Item -Path $VenvFolder -Force -Recurse
    Write-Host "The folder $VenvFolder was removed"
}
else
{
    Write-Host "The folder $VenvFolder was not found"
}

#######################################################
New-Item -Path $VenvFolder -ItemType Directory

Write-Host "The folder $VenvFolder was created"

if (Test-Path -Path $SourceCopyFolder)
{
    Write-Host "Deleting $SourceCopyFolder"
    Remove-Item -Path $SourceCopyFolder -Force -Recurse
    Write-Host "The folder $SourceCopyFolder was removed"
}
else
{
    Write-Host "Not deleting $SourceCopyFolder"
}
Copy-Item -Path $CurrentFolder -Destination $SourceCopyFolder -Recurse #todo How to copy without copying the top level folder
Write-Host "Finished copying over code to $SourceCopyFolder"

#######################################################

Write-Host "Begin-Creating VENV at $VenvFolder"
& $PythonBaseInterpreter -m venv $VenvFolder
Write-Host "End-Creating VENV at $VenvFolder"


Write-Host "Begin-Activating VENV at $ActivateScript"
& $ActivateScript
Write-Host "End-Activating VENV at $ActivateScript"

#######################################################

Push-Location -Path $SourceCopyFolder

Write-Host "Begin-Installing requirements"
& pip install -r $RequirementsFile
Write-Host "End-Installing requirements"

#######################################################

Write-Host "Going to launch Python from $VenvPythonInterpreter"
Write-Host "Python file: $PythonAbsoluteFile "
& $VenvPythonInterpreter $PythonAbsoluteFile  "arg0001" "arg002"

#######################################################
