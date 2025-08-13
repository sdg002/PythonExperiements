[[_TOC_]]

# Which docker image ?

## What did not work ?
python:3.11-windowsservercore


## What to do next ?
I was read this:
https://hub.docker.com/r/winamd64/python/tags
and this
https://hub.docker.com/_/python
The latter looks more authorative. You will find images tagged with `windowsservercore`

# Official Github site for Windows docker images
https://github.com/docker-library/python/blob/master/3.13/windows/windowsservercore-ltsc2025/Dockerfile

We can see the Dockerfile contents here for various versions of Python. 
Note - I see a Windows folder for the following versions of Python only:
1. 3.13
1. 3.14-rc

## What do we learn?
There are indeed Windows docker images with Python installed. But, only some of the vesions are installed

## How to create a Dockerfile with the desired version of Python?
See the Dockerfile on Github link above

---

# Windows docker images

## All configurations

https://learn.microsoft.com/en-us/virtualization/windowscontainers/manage-containers/container-base-images

## Windows Nano server
https://hub.docker.com/r/microsoft/windows-nanoserver

# Next action item
- Find the right docker image
- if not then build one
- Devops pipeline