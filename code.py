>>> import sys, os, codecs
>>> os.chdir('C:\\test')
>>> f = codecs.open("mydict.txt", "r", "utf-8")

>>> def pretty(dict):
	print '-'*60
	print repr(dict).decode("unicode-escape")
	print '-'*60

>>> f.seek(0)
>>> my_example_dict = {}
>>> for line in f:
	# find Ц находит подстроку в строке Ц возвращает позицию вхождени€ строки, либо -1:
	if line.find('[') == -1:
		print '1-й цикл - начало'
		print ' люч не найден. ƒобавл€ю в словарь предыдущего элемента'
		print line
		print '1-й цикл - конец'
	else:
		print '2-й цикл - начало'
		start_key = line.find('[')
		end_key = line.find(']') + 1
		key = line[start_key:end_key]
		my_example_dict[key] = line
		print key
		pretty(my_example_dict)
		print ' люч найден. Ќачинаю новый элемент'
		print line
		print '2-й цикл - конец'
		
