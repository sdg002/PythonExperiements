#from config.config_wrapper import ConfigWrapper
import sys
import logging
from src.config import ConfigWrapper


if __name__ =="__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info("Inside oil prices scraper")
    config_parser = ConfigWrapper.create_instance()
    url=config_parser.get("oil","endpoint")
    logging.info(f"Url={url}")

