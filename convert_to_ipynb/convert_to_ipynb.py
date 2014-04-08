# -*- coding: utf-8 -*-

import codecs

input_text = codecs.open("maintext", "r", "utf-8")
input_text.seek(0)

sample_list = []


def pretty(input_unicode_escape_obj):
     print repr(input_unicode_escape_obj).decode("unicode-escape")

# если '1' не существует, то #1, иначе #2
#1
sample_list.append({'1': ['first']})
#2
sample_list[len(sample_list)]['1'].append('really cool')

sample_list.append({'2': ['second']})
sample_list[1]['2'].append('really cool')

pretty(sample_list)
print len(sample_list)


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
            print 'func_add_paragraph()' + str(counter)


grab_text(input_text)
