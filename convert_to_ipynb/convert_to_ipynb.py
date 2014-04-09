# -*- coding: utf-8 -*-

import codecs

import json

#загрузка
data = json.load( open('realle_test_data.ipynb', 'r') )

workshit = data['worksheets'][0]['cells']


input_text = codecs.open("maintext", "r", "utf-8")

sample_list = [{1: [{u'cell_type': u'markdown', u'metadata': {}, u'source': []}]}]


def pretty(input_unicode_escape_obj):
     print repr(input_unicode_escape_obj).decode("unicode-escape")


def func_add_paragraph(num_string, input_string):
    current_index = len(sample_list)-1
    if num_string in sample_list[current_index]:
        sample_list[current_index][num_string][0][u'source'].append(input_string)
    else:
        sample_list.append({num_string: [{u'cell_type': u'markdown', u'metadata': {}, u'source': [input_string]}]})


# прототип ф-ции
def grab_text(enter_text):
    enter_text.seek(0)
    counter = 0
    while True:
        somestring = enter_text.readline()
        if not somestring:
            #print 'func_add_cells_to_worksheet()'
            break
        if somestring.isspace():
            counter += 1
        else:
            func_add_paragraph(counter, somestring)


def func_add_cells_to_worksheet():
    for index in range(0, len(sample_list)):
        #print str(index) + ' ' + str(sample_list[index].keys()[0]) + ' 0'
        workshit.append(sample_list[index][sample_list[index].keys()[0]][0])


grab_text(input_text)
#pretty(sample_list)
func_add_cells_to_worksheet()

with open('123.ipynb', 'w') as outfile:
    json.dump(data, outfile)
