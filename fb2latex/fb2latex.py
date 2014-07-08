# -*- coding: utf-8 -*-

# Lightweight XML support for Python.
# https://docs.python.org/3/library/xml.etree.elementtree.html
from xml.etree import ElementTree as ET
from xml.etree.ElementTree import QName
import io
import base64


tree = ET.parse('test.fb2')
root = tree.getroot()


# Simple get str with URI
uri = ''
if root.tag[0] == '{':
    uri = root.tag[1:].split('}')[0]
else:
    print('Tree has not namespace URI')


for child in root:
    print(child.tag, child.attrib)


for elem in root.getiterator(QName(uri, 'binary')):
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
    if node.tag != QName(uri, 'binary'):
        print(node.tag, node.attrib, node.text)


# Extracting text from nodes
for elem in root.iter(QName(uri, 'title')):
        print('\section{' + elem[0].text + '}')
