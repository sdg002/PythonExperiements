import configparser
import os
from typing import Any

class MyDict(dict):
    def __getitem__(self, key: Any) -> Any:
        print(f"Inside method __getitem__ of MyDict, key={key}")
        return f"Value of {key} from within MyDict"
        #U WILL NEED TO RETU ANOTHER DICT,FIRST CALL ONE IS SECTION

    def __contains__(self, key: object) -> bool:
        print(f"Inside __contains__, {key=}")
        return super().__contains__(key)

def display_setting(config: configparser.ConfigParser,section: str, key: str):
    value=config.get(section, key)
    print(f"Value of {section}:{key}={value}")


def try_custom_dict():
    dir_name = os.path.dirname( __file__)
    config = configparser.ConfigParser(os.environ, interpolation=configparser.ExtendedInterpolation())
    print("Going to read INI file")
    ini_file=os.path.join(dir_name,"config003.ini")
    print(ini_file)
    config.read(ini_file)

    mydict=MyDict()
    mydict["shared"] = {"prop2":"from MyDict"}
    #mydict["shared"] = MyDict()
    print(mydict["shared"])
    print(f"{mydict=}")
    config.read_dict(mydict)
    another_dict={"shared":{"from_inline_dict":"999 from another dict"}} #NOT BEING READ!!!
    print(f"{another_dict=}")
    config.read_dict(another_dict)
    display_setting(config=config,section="shared", key="prop1")
    display_setting(config=config,section="shared", key="temp_dir")
    display_setting(config=config,section="shared", key="from_inline_dict")
    display_setting(config=config,section="shared", key="prop2")




if __name__ =="__main__":
    try_custom_dict()