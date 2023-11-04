#from config.config_wrapper import ConfigWrapper
import sys
print(sys.path)
from src.config import ConfigWrapper


if __name__ =="__main__":
    print("Inside oil prices scraper")
    config_parser = ConfigWrapper.create_instance()
