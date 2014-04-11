# -*- coding: utf-8 -*-

import codecs
import json
from sys import argv

data = {u'metadata': {u'name': u''},
 u'nbformat': 3,
 u'nbformat_minor': 0,
 u'worksheets': [{u'cells': [{u'cell_type': u'markdown',
                              u'metadata': {},
                              u'source': []}],
                  u'metadata': {}}]}

script, input_file_name = argv
input_text = codecs.open(input_file_name, "r", "utf-8")

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
    with open(input_file_name + '.ipynb', 'w') as outfile:
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
