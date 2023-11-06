[[_TOC_]]

# Overview
Demonstrates the usage of Python's out of box `ConfigParser` class to implement a layered system of configuration using mulitple config files and seamlessly redirecting the config entries to be read from an environment variable. We will demonstrate how such a system can make your Python code to dynamically adapt to any environment.

![overview](docs/images/overview_layered_with_plus.png)

---

# What is the problem we are trying to solve (to be done) ?

Lets imagine a classic scenario of Python code used for scraping information from various data sources. You have a **DEV** environment where you test your code (could be the feature branch) and a **PROD** environment which is more stable and producing data fit for consumption.

 You want to write your code in a manner which makes it possible for it be deployed to DEV/UAT/PROD environments and on Docker/VM hosts

[show a picture of hard wired code, ?? apikey in a variable, if-else for output directory using command line arguments]


1. How can we manage settings across DEV, PROD and other environments without having to change Python code?
1. How can we avoid hard coding confidential settings in Python or config files ?

---
# What does the final solution look like (to be done)?


![how_layered_config_works](docs/images/how_layered_config_works.png)

```python

# Create an instance of ConfigParser
config_parser = configparser.ConfigParser(os.environ,interpolation=configparser.ExtendedInterpolation())

# Read the base settings
config_parser.read("basesettings.ini")

# Read the environment specific settings
environment = os.environ["environment"]
config_parser.read(f"settings.{environment}.ini")

# All set!
# Read the config values
api_username = config_parse["oil"]["api_username"]
api_key = config_parse["oil"]["api_key"]

```

---

# Solution using the out of box ConfigParser (to be done)

[show a simple snippet]

---

# Implementation details

![overview](docs/images/overview_layered_with_plus.png)

---

# Accompanying code
to be done ??

---

# References 
- to be done ??

#  Where was I ?
- Show code snippets
- 