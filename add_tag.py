def process_func():
    out_text = codecs.open("outme", "wb", "utf-8")
    f = codecs.open("text.tex", "r", "utf-8")
    f.seek(0)
    p = re.compile(r"([Чч]то|what|lol)", re.UNICODE)
    while True:
        line = f.readline()
        if not line:
            print ('выхожу из цикла')
            out_text.close()
            f.close()
            break
        else:
            print (p.search(line))
            subline = p.sub(r'\Blabla{\g<1>}', line)
            out_text.write(subline)
