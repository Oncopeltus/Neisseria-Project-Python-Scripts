#/usr/bin/python
import os
for filename in os.listdir('/home/jinl/pythonsrc'):
	if filename.endswith('.file'):
		i = open(filename)
		a = i.readlines()
		print a[0]
		b = a[0].split()
		print b
		i.close()

