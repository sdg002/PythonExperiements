Set-StrictMode -Version Latest
#$version = "3.12.5" #this works
#$version = "3.9.10" #this works
#$version = "3.9.11" #?
#$version = "3.9.12" #this works
#$version = "3.9.13" #this works
# Versions 3.9.14, .15 , .16, .17 do not have the EXE for amd64

$url = "https://www.python.org/ftp/python/$version/python-$version-amd64.exe"
Write-Host "Downloading Python from $url"
Invoke-WebRequest -Uri $url -OutFile "python.exe" -Verbose
Write-Host "Installing Python..."

