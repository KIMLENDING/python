import xml.etree.ElementTree as ET
tree = ET.parse('c:/Users/gotsl/Desktop/새 폴더 (2)/person.xml')
root = tree.getroot()
for i in root:
    print(i.tag,i.text)

