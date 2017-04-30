#!/usr/bin/python
import os
namelist = open('abcZ.txt','w')
for filename in os.listdir('/home/jinl/ST_profiles/abcZ/'):
	if filename.endswith('.file'):
		f = open(filename)
		name = str(filename)[:-11]
		namelist.write(name)
		namelist.write(' ')
		result = f.readlines()
		indicator = 0
		i = 0
		while indicator == 0 and i < len(result):
			tmp = result[i].split()
			if int(tmp[-1][:-1]) == 100:
				namelist.write(tmp[0][6:])
				namelist.write('\n')
				indicator = 1
			i += 1
		f.close()
namelist.close()
