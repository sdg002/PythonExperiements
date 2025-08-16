# What was I trying ?

Trying to use the `nanosever` image. However this does not have PowerShell (to download and install Python). So, downloading Python

---

# Why nanoserver ?
It has a smaller footprint

---

# Error message
The `tar` command to uncompress the downloaded archive fails. Something to do with not being able to find the `C:` drive

---

# Script

```dockerfile
## Install PowerShell below
# Download and install PowerShell
ADD https://github.com/PowerShell/PowerShell/releases/download/v7.3.6/PowerShell-7.3.6-win-x64.zip C:/PowerShell.zip

# Extract PowerShell
RUN tar -xf C:/PowerShell.zip -C C:/PowerShell

# Clean up zip file
RUN del C:/PowerShell.zip

# Add PowerShell to PATH
RUN setx PATH "C:/PowerShell;%PATH%" /M

# Set PowerShell as default shell
SHELL ["C:\\PowerShell\\pwsh.exe", "-Command", "$ErrorActionPreference = 'Stop'; $ProgressPreference = 'SilentlyContinue';"]

# Test PowerShell installation
RUN Write-Host "PowerShell installed successfully" -ForegroundColor Green

## Install PowerShell above

```
