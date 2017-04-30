#!/usr/bin/python
import os
namelist = open('glnB_CeuD.file','w')
for filename in os.listdir('/home/jinl/glnB_CeuD_blastoutput/'):
	if filename.endswith('.file'):
		f = open(filename)
		result = f.readlines()
		if len(result) > 1:
			glnB = result[0].split()
			CeuD = result[1].split()
			if glnB[1] == CeuD[1]:
				name = str(filename)
				namelist.write(name[:-11])
				namelist.write('\t')
				namelist.write(str(glnB[1]))
				namelist.write('\t')
				positions = [int(glnB[3]),int(glnB[4]),int(CeuD[3]),int(CeuD[4])]
				namelist.write(glnB[3])
				namelist.write('\t')
				namelist.write(glnB[4])
				namelist.write('\t')
				namelist.write(CeuD[3])
				namelist.write('\t')
				namelist.write(CeuD[4])
				namelist.write('\t')	
				namelist.write('\n')
		f.close()
namelist.close()
