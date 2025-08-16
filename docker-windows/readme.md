[[_TOC_]]

# Objective
Experiment building docker images with Python using base Windows operating system.

# How does it work ?
- Take a base windows image (e.g. `mcr.microsoft.com/windows/servercore:ltsc2019`)
- Download the required vesion of Python
- Install Python

---

# Where can we find all the versions of Python ?
The base URL for downloading is here https://www.python.org/ftp/python/. You will need to insert the version in the URL.
However, not all versions have the Windows installer. Refer this link for a [summary of all versions](https://www.python.org/downloads/windows/) on Windows.

---

# Does Docker hub provide ready made Windows images with Python ?
Yes.  Refer this [Github link](https://github.com/docker-library/python/blob/master/3.13/windows/windowsservercore-ltsc2025/Dockerfile) for a Dockerfile with Python 3.14 on windowsservercore






# What do we learn?

- Not all Python versions are available on Windows
- There are indeed Windows docker images with Python installed. But, only some of the vesions are installed
- You will need to verify the SHA signaure using PowerShell script. Refer sample from Github of Docker (link below)
- The YAML property `vmImage` will influence which version of Windows base image to pull. Example: with  `windows-2019` you can use `mcr.microsoft.com/windows/servercore:ltsc2019` base image
- Windows Nanoserver image does not have PowerShell

## How to create a Dockerfile with the desired version of Python?

See the Dockerfile on Github link above

---

# Windows docker images

## All configurations

https://learn.microsoft.com/en-us/virtualization/windowscontainers/manage-containers/container-base-images

## Windows Nano server
https://hub.docker.com/r/microsoft/windows-nanoserver

# Next action item
- Push to your Azure ACR using docker task of Devops (not azure cli task)
- Build a base image with Python only
- Use the base image and add your custom Python scripts and requirements

---

# How to push images to Azure Container Registry ?

## Setting up a connection with Azure Container Registry for pushing images?
![alt text](docs/acr-service-connection.png)

## YAML 

You need the following variables:
```yml
variables:
  containerRegistry: "mywin001vm.azurecr.io"  # Replace with your registry URL
  repositoryName: "python-demo"
  dockerRegistryServiceConnection: "mywin001vmAzureAcr"  # Replace with your service connection name
```

Docker build and push

```yml
        steps:
          - task: Docker@2
            displayName: "Build and push Docker image"
            inputs:
              command: "buildAndPush"
              dockerfile: "$(workingDirectory)/Dockerfile"
              buildContext: "$(workingDirectory)"
              repository: "$(repositoryName)"
              tags: $(imagetag)
              containerRegistry: "$(dockerRegistryServiceConnection)"
```


---

# Misc

## Steps for pushing an image to a private repo

```
docker login <REGISTRY_HOST>:<REGISTRY_PORT>
docker tag <IMAGE_ID> <REGISTRY_HOST>:<REGISTRY_PORT>/<APPNAME>:<APPVERSION>
docker push <REGISTRY_HOST>:<REGISTRY_PORT>/<APPNAME>:<APPVERSION>
```
https://stackoverflow.com/a/45312996/2989655


## Verify a downloaded file using ASC 
https://crypto.stackexchange.com/questions/43537/verifying-a-downloaded-file-with-an-asc-file


## Official Github site for Windows docker images

https://github.com/docker-library/python/blob/master/3.13/windows/windowsservercore-ltsc2025/Dockerfile

We can see the Dockerfile contents here for various versions of Python. 
Note - I see a Windows folder for the following versions of Python only:
1. 3.13
1. 3.14-rc

## Docker hub tags with Python and Windows
https://hub.docker.com/r/winamd64/python/tags
and this
https://hub.docker.com/_/python
The latter looks more authorative. You will find images tagged with `windowsservercore`
