import logging
from xml.dom import minidom
from xml.dom.minidom import parse, parseString
import os 
import sys




if __name__ =="__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info("Begin")
    logging.info(f"Command line args={sys.argv}")
    abs_file = os.path.join(os.path.dirname(__file__), "sample.xml")
    ds = open(abs_file)
    dom = parse(ds)
    
    record_elements=dom.firstChild.getElementsByTagName("record")
    for record in record_elements:
        print("--------------------")
        id=record.getAttribute("id")
        print(f"{id=}")
        #cdata_text=record.firstChild.nodeValue


        for child in record.childNodes:
            print(f"............{child.nodeType=}")
            if child.nodeType == minidom.Node.ELEMENT_NODE:
                print(f"Child element: {child.tagName}, Text: {child.firstChild.nodeValue.strip()}")
            elif child.nodeType == minidom.Node.TEXT_NODE:
                print(f"Text node: {child.nodeValue.strip()}")
            elif child.nodeType == minidom.Node.CDATA_SECTION_NODE:
                print(f"CDATA node: *{child.data.strip()}*")
            else:
                print(f"Unknown node type: {child.nodeType}")            
        print("------------------")
    logging.info("End")
