import configparser
import os

class WrapperConfig(configparser.ConfigParser):
    def __init__(self):
        print("Inside ctor of WrapperConfig")
        super().__init__(os.environ, interpolation=configparser.ExtendedInterpolation())
        dir_name = os.path.dirname( __file__)
        self.read(os.path.join(dir_name,"config1.ini"))
        self.read(os.path.join(dir_name,"config2_extended_interpolation.ini"))
        print("Completed initialization of WrapperConfig")
        pass

    def display_setting(self, section: str, key: str):
        value=self.get(section, key)
        print(f"Value of {section}:{key}={value}")


#config = configparser.ConfigParser(os.environ, interpolation=configparser.ExtendedInterpolation())
config = WrapperConfig()

print("----------SafeConfigParser-------------")
#try the 1 line with SafeConfigParser
#config.read(['config1.ini', 'config2.ini'])




print(config.sections()) # ['shared', 'unique1', 'unique2']
print(config.get("shared", "prop_uniue1"))  # 1
print(config.get("shared", "prop_shared"))  # 14
print(config.get("unique1", "test_unique")) # 101

print(config.get("shared", "prop_uniue2"))  # 2
print(config.get("unique2", "test_unique")) # 102

config.display_setting(section='unique2' , key='temp_folder1')
config.display_setting(section='unique2' , key='temp_folder2')
config.display_setting(section='unique2' , key='temp_folder3')
config.display_setting(section='DEFAULT' , key='TEMP')
config.display_setting(section='DEFAULT' , key='TEMP_BASE')
config.display_setting(section='DEFAULT' , key='USERPROFILE')
config.display_setting(section='DEFAULT' , key='USERBASEFOLDER')

config.display_setting(section='shared' , key='prop_shared')
config.display_setting(section='unique2' , key='TEMP0')
config.display_setting(section='unique2' , key='TEMP01')
config.display_setting(section='unique2' , key='temp_folder_$_temp')
config.display_setting(section='DEFAULT' , key='WINDIR')
config.display_setting(section='unique2' , key='WINDIR01')
config.display_setting(section='shared' , key='cn_string')

config.display_setting(section='unique2' , key='MYFOLDER1')
config.display_setting(section='unique2' , key='MYFOLDER2')

#
#Try https://stackoverflow.com/questions/26586801/configparser-and-string-interpolation-with-env-variable
#SafeConfigParser
#