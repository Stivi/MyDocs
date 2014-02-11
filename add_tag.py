import os
import re
import codecs

os.chdir(os.getcwd())


def process_func():
    out_text = codecs.open("outme", "wb", "utf-8")
    f = codecs.open("text.tex", "r", "utf-8")
    f.seek(0)
    p = re.compile(r"""
        (
            \b[Аа]\b
            |\b[Бб]удто\b
            |\b[Дд]а\b
            |\b[Дд]ля\ того\b       # In verbose regular expression
            |\b[Ее]два\b            # whitespace is ignored. So I
            |\b[Ее]сли\b            # putting a backslash
            |\b[Зз]ато\b            # in front of space to match it.
            |\b[Ии]\b
            |\b[Ии]ли\b
            |\b[Кк]ак\b
            |\b[Кк]огда\b
            |\b[Лл]ибо\b
            |\b[Нн]е\ то\b
            |\b[Нн]е\ только\b
            |\b[Нн]и\b
            |\b[Нн]о\b
            |\b[Оо]днако\b
            |\b[Оо]ттого\b
            |\b[Пп]отому\ что\b
            |\b[Пп]оэтому\b
            |\b[Сс]ловно\b
            |\b[Тт]ак\b
            |\b[Тт]акже\b
            |\b[Тт]аким\ образом\b
            |\b[Тт]о\b
            |\b[Тт]оже\b
            |\b[Чч]то\b
            |\b[Чч]тобы\b
        )
        """, re.VERBOSE)

    while True:
        line = f.readline()
        if not line:
            print('выхожу из цикла')
            out_text.close()
            f.close()
            break
        else:
            subline = p.sub(r'\\textcolor{conjunctions}{\g<1>}', line)
            out_text.write(subline)
