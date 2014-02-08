# -*- coding: utf-8 -*-

# TODO Извлечь binary в файлы

import sys, os, base64

input = open('input', 'r')
output = open('out.jpg', 'wb')

try:
    base64.decode(input, output)

finally:
    input.close()
    output.close()
