#!/usr/bin/python
import os
namelist = open('allsort.namefile','w')
alignfile = open('all.newphy')
align = alignfile.readlines()
for line in align:
	if line[0] =='>':
		if len(line) > 6:
			namelist.write(line)
namelist.close()
alignfile.close()
