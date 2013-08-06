>>> import sys, os, codecs
>>> os.chdir('C:\\test')
>>> f = codecs.open("mydict.txt", "r", "utf-8")

>>> def pretty(dict):
	print '-'*60
	print repr(dict).decode("unicode-escape")
	print '-'*60

>>> def init_start():
	f.seek(0)
	my_example_dict.clear()
	my_example_dict['0'] = 'lol'

>>> def cut_key_to_dict():
	for line in f:
		# find – находит подстроку в строке – возвращает позицию вхождения строки, либо -1:
		if line.find('[') == -1:
			print '1-й цикл - начало'
			print 'Ключ не найден. Добавляю в список предыдущего элемента'
			print line
			print '1-й цикл - конец'
		else:
			print '2-й цикл - начало'
			start_key = line.find('[')
			end_key = line.find(']') + 1
			key = line[start_key:end_key]
			print 'Сброс в словарь готового элемента'
			my_example_dict[key] = line
			print key
			pretty(my_example_dict)
			print 'Ключ найден. Начинаю новый элемент'
			print line
			print '2-й цикл - конец'


		
