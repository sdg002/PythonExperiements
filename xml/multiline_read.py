import logging
from xml.dom import minidom
from xml.dom.minidom import parse, parseString
import os 
import sys

def read_xml():
    pass


if __name__ =="__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info("Begin")
    logging.info(f"Command line args={sys.argv}")
    abs_file = os.path.join(os.path.dirname(__file__), "multi.xml")
    ds = open(abs_file)
    dom = parse(ds)
    xml_str = dom.toprettyxml(indent ="\t") 
    
    record_elements=dom.firstChild.getElementsByTagName("record")
    for record in record_elements:
        id=record.getAttribute("id")
        print(f"{id=}")
        
        print(f"{record.firstChild.data}")
        print("------------------")
    logging.info("End")
