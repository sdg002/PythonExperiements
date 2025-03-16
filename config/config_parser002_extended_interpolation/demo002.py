import configparser
import os


dir_name = os.path.dirname( __file__)
config = configparser.ConfigParser(os.environ, interpolation=configparser.ExtendedInterpolation())

print("----------SafeConfigParser-------------")
#try the 1 line with SafeConfigParser
#config.read(['config1.ini', 'config2.ini'])
config.read(os.path.join(dir_name,"config1.ini"))
config.read(os.path.join(dir_name,"config2_extended_interpolation.ini"))


def display_setting(section: str, key: str):
    value=config.get(section, key)
    print(f"Value of {section}:{key}={value}")


print(config.sections()) # ['shared', 'unique1', 'unique2']




display_setting(section='shared' , key='prop_shared')
display_setting(section='shared' , key='prop_uniue1')
display_setting(section='shared' , key='cn_string')
display_setting(section='unique1' , key='test_unique')

display_setting(section='unique2' , key='test_unique')
display_setting(section='unique2' , key='temp_folder1')
display_setting(section='unique2' , key='temp_folder2')
display_setting(section='unique2' , key='temp_folder3')
display_setting(section='DEFAULT' , key='TEMP')
display_setting(section='DEFAULT' , key='TEMP_BASE')
display_setting(section='DEFAULT' , key='USERPROFILE')
display_setting(section='DEFAULT' , key='USERBASEFOLDER')

display_setting(section='unique2' , key='TEMP0')
display_setting(section='unique2' , key='TEMP01')
display_setting(section='unique2' , key='temp_folder_$_temp')
display_setting(section='DEFAULT' , key='WINDIR')
display_setting(section='unique2' , key='WINDIR01')
display_setting(section='unique2' , key='WINDIR02')
display_setting(section='shared' , key='cn_string')

display_setting(section='unique2' , key='MYFOLDER1')
display_setting(section='unique2' , key='MYFOLDER2')

#
#Try https://stackoverflow.com/questions/26586801/configparser-and-string-interpolation-with-env-variable
#SafeConfigParser
#