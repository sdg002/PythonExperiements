import configparser
import os
import logging

class ConfigWrapper:
    def create_instance()->configparser.ConfigParser:
        print("Inside create_instance")
        config_parser = configparser.ConfigParser(os.environ,interpolation=configparser.ExtendedInterpolation())
        dir_name = os.path.dirname( __file__)
        base_ini_file = os.path.join(dir_name,"base_settings.ini")
        if not os.path.exists(base_ini_file):
            raise Exception(f"The base INI file '{base_ini_file}' was not found in this directory")
        env = os.environ.get("environment", None)
        logging.info(f"The environemnt variable 'environment' has the value '{env}'")
        if env is None:
            raise ValueError(f"The envrionment variable: 'environment' has not been set") 
        environment_specific_ini_file = os.path.join(dir_name,"base_settings.ini")
        if not os.path.exists(environment_specific_ini_file):
            raise Exception(f"The environment specific INI file '{environment_specific_ini_file}' was not found in this directory")
        config_parser.read(base_ini_file)
        config_parser.read(environment_specific_ini_file)
        return config_parser

    
    
