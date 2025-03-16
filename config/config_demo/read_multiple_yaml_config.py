import configparser
import os

dir_name = os.path.dirname( __file__)
config = configparser.ConfigParser()
first_ini=os.path.join(dir_name,"example.ini")
second_ini=os.path.join(dir_name,"example_partial.ini")
#config.read_file(["example.ini","example_partial.ini"])

print("Going to read from config file")
print(first_ini)
config.read([first_ini]  ) #this works
config.read([second_ini])
pass

#
print(config["bitbucket.org"]["user0"])
print(config["bitbucket.org"]["user"])
print("success in reading")

print(config["bitbucket.org"]["user1"])
print("success in reading")

#
#works after reading in multiple lines
#
print(config["section1"]["user1"])

