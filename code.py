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
	# find � ������� ��������� � ������ � ���������� ������� ��������� ������, ���� -1:
	if line.find('[') == -1:
		print '1-� ���� - ������'
		print '���� �� ������. �������� � ������� ����������� ��������'
		print line
		print '1-� ���� - �����'
	else:
		print '2-� ���� - ������'
		start_key = line.find('[')
		end_key = line.find(']') + 1
		key = line[start_key:end_key]
		my_example_dict[key] = line
		print key
		pretty(my_example_dict)
		print '���� ������. ������� ����� �������'
		print line
		print '2-� ���� - �����'
		
