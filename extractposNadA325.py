#!/usr/bin/python
import os
namelist = open('NadAlist.txt','w')
for filename in os.listdir('/home/jinl/NadA_blastoutput/gln_CeuD/'):
	if filename.endswith('.file'):
		f = open(filename)
		name = str(filename)[:-21]
		result = f.readlines()
		if len(result) == 1:
			line = result[0].split()
			if line[0][-3:] == '311' or line[0][-3:] == '325':
				if line[0][-3:] == '311':
					pos1 = line[4]
					pos2 = line[3]
				elif line[0][-3:] == '325':
					pos1 = line[3]
					pos2 = line[4]
				namelist.write(name)
				namelist.write('_')
				NadA_name = line[0][1:]
				namelist.write(NadA_name)
				writeline = '\t' + pos1 + '\t' + pos2 + '\n'
				namelist.write(writeline)
		f.close()
namelist.close()
