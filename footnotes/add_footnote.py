# -*- coding: utf-8 -*-


import sys
import os
import codecs

os.chdir('C:\\test')
f = codecs.open("ref.txt", "r", "utf-8")
input_text = codecs.open("text.tex", "r", "utf-8")
out_text = codecs.open("outme", "wb", "utf-8")


def pretty(dict):
     print repr(dict).decode("unicode-escape")


def replace_all(text, dic):
    for i, j in dic.iteritems():
        text = text.replace(i, j)
    return text

my_example_dict = {}


def pull_to_dict():
        # переходим в начало файла и обнуляем словарь
        f.seek(0)
        my_example_dict.clear()
        while True:
                line = f.readline()
                if not line:
                        print 'выхожу из цикла'
                        break
                if line.find('[') == -1:
                        pass
                else:
                        start_key = line.find('[')
                        end_key = line.find(']') + 1
                        key = line[start_key:end_key]
                        my_example_dict[key] = u'\\footnote{' + line.replace(str(key), '').strip() + u'}'


def push_to_file():
        out_text.seek(0)
        while True:
                inputline = input_text.readline()
                if inputline:
                        inputline = replace_all(inputline, my_example_dict)
                        out_text.write(inputline)
                else:
                        print 'выхожу из цикла'
                        my_example_dict.clear()
                        out_text.close()
                        input_text.close()
                        break
