#!/usr/bin/python
import os
namelist = open('NadA.txt','w')
for filename in os.listdir('/home/jinl/NadA_blastoutput/gln_CeuD/'):
	if filename.endswith('.file'):
		f = open(filename)
		name = str(filename)[:-21]
		result = f.readlines()
		if len(result) > 1:
			namelist.write(name)
			tmpdic = dict()
			for line in result: 
				tmp = line.split()
				if tmp[7] == '1.00':
					tmpdic[tmp[-1]] = tmp[0][1:]					
			NadA = max(tmpdic)
			NadA_name = tmpdic[NadA]
			for line in result:
				tmp1 = line.split()
				if tmp1[0][1:] == NadA_name:
					namelist.write('_')
					namelist.write(NadA_name)
					writeline = '\t' + tmp1[3] + '\t' + tmp1[4] + '\n'
					namelist.write(writeline)
		elif len(result) == 1:
			namelist.write(name)
			line = result[0].split()
			if line[0][-3:] == '311':
				pos1 = line[4]
				pos2 = line[3]
			else:
				pos1 = line[3]
				pos2 = line[4]
			namelist.write('_')
			if line[0][6:].isdigit():
				NadA_name = line[0][1:]
			else:
				NadA_name = line[0][1:6] + 'ins'
			namelist.write(NadA_name)
			writeline = '\t' + pos1 + '\t' + pos2 + '\n'
			namelist.write(writeline)
		f.close()
namelist.close()
