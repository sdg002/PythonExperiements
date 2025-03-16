import logging
from xml.dom import minidom 
import os 


def create_records(max:int)->minidom.Document:
    root = minidom.Document() 
    records=root.createElement("records")
    root.appendChild(records)
    for idx in range(max):
        logging.info(f"index={idx}")
        record=root.createElement("record")
        record.setAttribute(attname="id",value=str(idx))
        #record.nodeType = record.TEXT_NODE
        #record.nodeValue= "this is node text" #this did not work
        txt_node=root.createTextNode(data="\nhello\nworld\n")
        record.appendChild(txt_node)
        records.appendChild(record)
    return root

if __name__ =="__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info("Begin")
    root=create_records(max=10)
    xml_str = root.toprettyxml(indent ="\t") 
    print(xml_str)
    abs_file = os.path.join(os.path.dirname(__file__), "multi.xml")
    with open(file=abs_file, mode="w") as f:
        f.write(xml_str)
    logging.info("End")
