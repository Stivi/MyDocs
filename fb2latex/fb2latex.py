# -*- coding: utf-8 -*-

# Lightweight XML support for Python.
from xml.etree import ElementTree as ET
tree = ET.parse('test.fb2')

root = tree.getroot()


# https://docs.python.org/3/library/xml.etree.elementtree.html

# Element  is  a  flexible   container  object  designed  to
# store hierarchical  data structures  in memory. It  can be
# described as a cross between a list and a dictionary. Each
# Element has a number of properties associated with it:
#
#    'tag' - a string containing the element's name.
#
#    'attributes'   -  a   Python  dictionary   storing  the
#    element's attributes.
#
#    'text'  -  a  string   containing  the  element's  text
#    content.
#
#    'tail' -  an optional string containing  text after the
#    element's end tag.
#
#    And  a number  of  child elements  stored  in a  Python
#    sequence.


# As an Element, root has a tag and a dictionary of attributes
root.tag
root.attrib


for child in root:
    print(child.tag, child.attrib)


import io
import base64


for elem in root.getiterator('{http://www.gribuser.ru/xml/fictionbook/2.0}binary'):
    input = io.StringIO()
    input.write(elem.text)
    pictname = elem.attrib.get("id")
    output = open(pictname, 'wb')
    input.seek(0)
    base64.decode(input, output)
    input.close()
    output.close()
