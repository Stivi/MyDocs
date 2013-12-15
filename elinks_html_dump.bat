SET PATH="d:\Programs\elinks-0.11.6\elinks.exe"

FOR %%I IN (*.html) DO (%PATH% -dump -dump-charset 1251 -no-numbering -no-references "%%I" > "%%I.txt" && DEL "%%I")
