import configparser
import os
from typing import Any
from collections import UserDict

def display_setting(config: configparser.ConfigParser,section: str, key: str):
    value=config.get(section, key)
    print(f"Value of {section}:{key}={value}")

class MyDict(dict):
    def __getitem__(self, key: Any) -> Any:
        print(f"Inside method __getitem__ of MyDict, key={key}")
        return f"Value of {key} from overiden dictionary class"

class AnotherMyDict(UserDict):
    def __getitem__(self, key: Any) -> Any:
        env_val=os.environ.get(key,None)
        if env_val is not None:
            print(f"Inside method __getitem__, got {env_val=} for {key=}")
            return env_val
        print(f"Inside method __getitem__ of AnotherMyDict, key={key}")
        return f"Value of '{key}' from AnotherMyDict"
#https://realpython.com/inherit-python-dict/#inheriting-from-the-python-built-in-dict-class




def try_custom_dict():
    #mydict=MyDict() # this works , but overriden __getitem__ is not called
    #configparser.InterpolationMissingOptionError: Bad value substitution: option 'from_dict' in section 'shared' contains an interpolation key 'dictkey1' which is not a valid option name. Raw value: '${dictkey1}'
    #
    #
    
    mydict=AnotherMyDict() # This worked. You will need to override __getitem__
    mydict["temp"]="custom temp value"
    mydict["dictkey1"]="Hard coded value of dictkey1"
    dir_name = os.path.dirname( __file__)
    #custom_dict={"from_dict":"value from custom dict"}
    config = configparser.ConfigParser(
        mydict,
        interpolation=configparser.ExtendedInterpolation())
    print("Going to read INI file")
    ini_file=os.path.join(dir_name,"config003.ini")
    print(ini_file)
    config.read(ini_file)
    display_setting(config=config,section="shared", key="prop1")
    display_setting(config=config,section="shared", key="temp_dir")
    #display_setting(config=config,section="shared", key="some_random_key")
    display_setting(config=config,section="shared", key="from_dict")


if __name__ =="__main__":
    try_custom_dict()