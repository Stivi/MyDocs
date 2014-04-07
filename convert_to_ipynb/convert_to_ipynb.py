import codecs

out_text = codecs.open("outme", "wb", "utf-8")
input_text = codecs.open("maintext", "r", "utf-8")
input_text.seek(0)

big_lol_test = []

def grab_text(enter_text):
    enter_text.seek(0)
    while True:
        somestring = enter_text.readline()
        if not somestring:
            print 'end of work'
            break
        if somestring.isspace():
            print 'пустая строка. current list append to full list, and clear. Maybe pass here'
        else:
            big_lol_test.append(somestring)
