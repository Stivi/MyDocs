# -*- coding: utf-8 -*-

import sys, os, base64

inputfile = open('input', 'r')
outfile = open('out.jpg', 'wb')

base64.decode(inputfile, outfile)

inputfile.close()
outfile.close()

## Для  полной   уверенности  в  закрытии
## файла можно использовать блок try/finally:
## 
##   try:
##      # Тут идет запись в файл
##   finally:
##      file.close()
