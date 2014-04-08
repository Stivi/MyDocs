# -*- coding: utf-8 -*-

import codecs

input_text = codecs.open("maintext", "r", "utf-8")
input_text.seek(0)

sample_list = [{1: []}]


def pretty(input_unicode_escape_obj):
     print repr(input_unicode_escape_obj).decode("unicode-escape")


def func_add_paragraph(num_string, input_string):
    print 'index_is ' + str(len(sample_list)-1)
    if num_string in sample_list[len(sample_list)-1]:
        sample_list[len(sample_list)-1][num_string].append(input_string)
    else:
        sample_list.append({num_string: [input_string]})


# прототип ф-ции
def grab_text(enter_text):
    enter_text.seek(0)
    counter = 0
    while True:
        somestring = enter_text.readline()
        if not somestring:
            print 'func_write_obj_with_paragraphs()'
            break
        if somestring.isspace():
            counter += 1
            print 'func_isspace()' + str(counter)
        else:
            #print 'func_add_paragraph()' + str(counter)
            func_add_paragraph(counter, somestring)


grab_text(input_text)
pretty(sample_list)
