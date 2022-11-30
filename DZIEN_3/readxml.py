import xml.etree.ElementTree as ET

try:
    tree = ET.parse("kraj.xml")
    root = tree.getroot()
    for child in root:
        print(f"element: {child.tag}, atrybut: {child.attrib}")

except:
    print("element nie istnieje!")
