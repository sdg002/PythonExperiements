import configparser
import os


dir_name = os.path.dirname( __file__)
config = configparser.SafeConfigParser(os.environ)

print("----------SafeConfigParser-------------")
#try the 1 line with SafeConfigParser
#config.read(['config1.ini', 'config2.ini'])
config.read(os.path.join(dir_name,"config1.ini"))
config.read(os.path.join(dir_name,"config2.ini"))


def display_setting(section: str, key: str):
    value=config.get(section, key)
    print(f"Value of {section}:{key}={value}")


print(config.sections()) # ['shared', 'unique1', 'unique2']
print(config.get("shared", "prop_uniue1"))  # 1
print(config.get("shared", "prop_shared"))  # 14
print(config.get("unique1", "test_unique")) # 101

print(config.get("shared", "prop_uniue2"))  # 2
print(config.get("unique2", "test_unique")) # 102

display_setting(section='unique2' , key='temp_folder1')
display_setting(section='unique2' , key='temp_folder2')
display_setting(section='unique2' , key='temp_folder3')
display_setting(section='DEFAULT' , key='TEMP')
display_setting(section='shared' , key='prop_shared')
display_setting(section='unique2' , key='TEMP0')
display_setting(section='unique2' , key='TEMP01')
display_setting(section='DEFAULT' , key='WINDIR')
display_setting(section='unique2' , key='WINDIR01')
display_setting(section='shared' , key='cn_string')

#
#Try https://stackoverflow.com/questions/26586801/configparser-and-string-interpolation-with-env-variable
#SafeConfigParser
#