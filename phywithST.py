#!/usr/bin/python
import os
namelist = open('allunique.phy','w')
STlistfile = open('STsorted.file')
alignfile = open('allunique.newsp')
align = alignfile.readlines()
STlist = STlistfile.readlines()
profiledic = dict()
for line in STlist:
	tmp = line.split()
	profiledic[tmp[0]] = tmp[-1]
for line in align:
	tmp1 = line.strip()
	if tmp1[0] =='>':
		if len(tmp1) > 7:
			if tmp1[13] == '.':
				name = tmp1[1:13]
				namelist.write(tmp1[:14])
			else:
				name = tmp1[1:9]
				namelist.write(tmp1[:10])
			namelist.write('ST')
			namelist.write(profiledic[name])
		else:
			namelist.write(tmp1)
	else:
		namelist.write(tmp1)
	namelist.write('\n')
namelist.close()
STlistfile.close()
alignfile.close()
