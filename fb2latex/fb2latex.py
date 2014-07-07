# -*- coding: utf-8 -*-

# Lightweight XML support for Python.
from xml.etree import ElementTree as ET
tree = ET.parse('test.fb2')

root = tree.getroot()


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
