import configparser
import os


dir_name = os.path.dirname( __file__)
config = configparser.ConfigParser()
#config.read(['config1.ini', 'config2.ini'])
config.read(os.path.join(dir_name,"config1.ini"))
config.read(os.path.join(dir_name,"config2.ini"))


def display_setting(section: str, key: str):
    value=config.get("shared", "prop_uniue1")
    print(f"Value of {section}:{key}={value}")


print(config.sections()) # ['shared', 'unique1', 'unique2']
print(config.get("shared", "prop_uniue1"))  # 1
print(config.get("shared", "prop_shared"))  # 14
print(config.get("unique1", "test_unique")) # 101

print(config.get("shared", "prop_uniue2"))  # 2
print(config.get("unique2", "test_unique")) # 102

display_setting(section='unique2' , key='temp_folder')

