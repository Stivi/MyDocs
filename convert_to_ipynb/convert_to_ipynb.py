# -*- coding: utf-8 -*-

import codecs

input_text = codecs.open("maintext", "r", "utf-8")
input_text.seek(0)

big_lol_test = []


def pretty(input_unicode_escape_obj):
     print repr(input_unicode_escape_obj).decode("unicode-escape")


def grab_text(enter_text):
    while True:
        somestring = enter_text.readline()
        if not somestring:
            print 'end of work'
            break
        if somestring.isspace():
            print 'null line. current list append to full list, and clear. Maybe pass here'
        else:
            big_lol_test.append(somestring)

grab_text(input_text)
