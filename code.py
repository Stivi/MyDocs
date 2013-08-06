>>> import sys, os, codecs
>>> os.chdir('C:\\test')
>>> f = codecs.open("mydict.txt", "r", "utf-8")

>>> def pretty(dict):
	print '-'*60
	print repr(dict).decode("unicode-escape")
	print '-'*60

>>> def cut_key_to_dict():
	# переходим в начало файла и обнуляем словарь
	f.seek(0)
	my_example_dict.clear()
	while 1:
		line = f.readline()
		if not line:
			print 'выхожу из цикла'
			break
		if line.find('[') == -1:
			print '1-й цикл - начало'
			print 'Ключ не найден. Ожидается строка с ключем в начале.'
			print 'Тут ожидается пустая строка', "|" , line, "|"
			print '1-й цикл - конец'
		else:
			print '2-й цикл - начало'
			start_key = line.find('[')
			end_key = line.find(']') + 1
			key = line[start_key:end_key]
			print 'Сброс в словарь готового элемента'
			my_example_dict[key] = line
			pretty(my_example_dict)
			print '2-й цикл - конец'

