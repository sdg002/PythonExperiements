Set-StrictMode -version "latest"
$ErrorActionPreference="Stop"

$file=Join-Path -Path $PSScriptRoot -ChildPath "powershell.log"
"" | Out-File  $file
$message="hello world at $(Get-Date) "
$message | Out-File  $file -append
"virtual env='$env:VIRTUAL_ENV'" | Out-File $file -append

$pythonexe=Join-Path -Path $env:VIRTUAL_ENV -ChildPath "scripts\python.exe"

"Displaying the Python version" | Out-File $file -append
& $pythonexe --version >> $file

& $pythonexe child_proc.py
