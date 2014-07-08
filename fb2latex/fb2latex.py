# -*- coding: utf-8 -*-

# Lightweight XML support for Python.
from xml.etree import ElementTree as ET
import io
import base64


tree = ET.parse('test.fb2')

root = tree.getroot()


# https://docs.python.org/3/library/xml.etree.elementtree.html


# As an Element, root has a tag and a dictionary of attributes
root.tag
root.attrib


for child in root:
    print(child.tag, child.attrib)


for elem in root.getiterator('{http://www.gribuser.ru/xml/fictionbook/2.0}binary'):
    input = io.StringIO()
    input.write(elem.text)
    pictname = elem.attrib.get("id")
    output = open(pictname, 'wb')
    input.seek(0)
    base64.decode(input, output)
    input.close()
    output.close()


# Print whole tree without binary
for node in tree.iter():
    if node.tag != '{http://www.gribuser.ru/xml/fictionbook/2.0}binary':
        print(node.tag, node.attrib, node.text)
