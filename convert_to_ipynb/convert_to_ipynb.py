import codecs

out_text = codecs.open("outme", "wb", "utf-8")
input_text = codecs.open("maintext", "r", "utf-8")
input_text.seek(0)

while True:
    line = input_text.readline()
    if not line:
        out_text.close()
        input_text.close()
        break
    else:
        out_text.write(line.encode('unicode_escape'))
