# -*- coding: utf-8 -*-

import codecs

input_text = codecs.open("maintext", "r", "utf-8")
input_text.seek(0)

big_lol_test = []


def pretty(input_unicode_escape_obj):
     print repr(input_unicode_escape_obj).decode("unicode-escape")


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
            #big_lol_test.append(somestring)

grab_text(input_text)
