#!/usr/bin/python
import os
namelist = open('allglnBCeuDwST.fasta','w')
STlistfile = open('STsorted.file')
alignfile = open('allglnBCeuD.fasta')
align = alignfile.readlines()
STlist = STlistfile.readlines()
profiledic = dict()
for line in STlist:
	tmp = line.split()
	profiledic[tmp[0]] = tmp[-1]
for line in align:
	tmp1 = line.strip()
	if tmp1[0] =='>':
		if len(tmp1) == 9:
			name = str(tmp1[1:])
			namelist.write(tmp1)
		else:
			name = tmp1[1:]
			namelist.write(tmp1[:5])
		namelist.write('_')
		namelist.write(profiledic[name])
	else:
		namelist.write(tmp1)
	namelist.write('\n')
namelist.close()
STlistfile.close()
alignfile.close()
