import configparser
import os

def display_setting(config: configparser.ConfigParser,section: str, key: str):
    value=config.get(section, key)
    print(f"Value of {section}:{key}={value}")

print("Begin....")
config = configparser.ConfigParser(os.environ, interpolation=configparser.ExtendedInterpolation())
sample_ini_file=os.path.join(os.path.dirname(__file__),"sample.ini")
print(f"Going to load the INI file {sample_ini_file}")
config.read(sample_ini_file)

display_setting(config=config, section="magic_module", key="magic_directory")
display_setting(config=config, section="another_section", key="another_directory")
