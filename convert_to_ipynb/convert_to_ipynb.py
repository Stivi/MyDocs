# -*- coding: utf-8 -*-

import codecs
import json

data = json.load( open('realle_test_data.ipynb', 'r') )
input_text = codecs.open("maintext", "r", "utf-8")

worksheet = data['worksheets'][0]['cells']
new_cells_list = [{1: [{u'cell_type': u'markdown', u'metadata': {}, u'source': []}]}]


def func_add_paragraph(num_string, input_string):
    current_index = len(new_cells_list)-1
    if num_string in new_cells_list[current_index]:
        new_cells_list[current_index][num_string][0][u'source'].append(input_string)
    else:
        new_cells_list.append({num_string: [{u'cell_type': u'markdown', u'metadata': {}, u'source': [input_string]}]})


def func_add_cells_to_worksheet():
    for index in range(0, len(new_cells_list)):
        worksheet.append(new_cells_list[index][new_cells_list[index].keys()[0]][0])


def save_my_work():
    with open('new_out.ipynb', 'w') as outfile:
        json.dump(data, outfile)


def grab_text(enter_text):
    enter_text.seek(0)
    counter = 0
    while True:
        somestring = enter_text.readline()
        if not somestring:
            func_add_cells_to_worksheet()
            save_my_work()
            break
        if somestring.isspace():
            counter += 1
        else:
            func_add_paragraph(counter, somestring)


grab_text(input_text)
