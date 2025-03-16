from xml.dom import minidom 
import os 


root = minidom.Document() 

container_element = root.createElement('container') 
root.appendChild(container_element) 

productChild = root.createElement('product') 
productChild.setAttribute('name', 'Geeks for Geeks') 

container_element.appendChild(productChild) 

xml_str = root.toprettyxml(indent ="\t") 

save_path_file = "gfg.xml"

with open(save_path_file, "w") as f: 
	f.write(xml_str) 
