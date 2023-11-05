import sys
import logging
from src.config import ConfigWrapper


if __name__ =="__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info("Inside oil prices scraper")
    config_parser = ConfigWrapper.create_instance()
    logging.info("Displaying the OIL configuration for current environment")
    logging.info("---------------------------------------")
    logging.info("Url={}".format(config_parser.get("oil","endpoint")))
    logging.info("API key={}".format(config_parser.get("oil","api_key")))
    logging.info("Output folder={}".format(config_parser.get("oil","output_folder")))


