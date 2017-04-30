#!/usr/bin/python
import os
namelist = open('glnB_CeuD.txt','w')
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
				pos1 = max(positions)
				pos2 = min(positions)
				if min([positions[0], positions[1]]) > max([positions[2], positions[3]]):
					namelist.write(str(pos1))
					namelist.write('\t')
					namelist.write(str(pos2))
				elif max([positions[0], positions[1]]) < min([positions[2], positions[3]]):
					namelist.write(str(pos2))
					namelist.write('\t')
					namelist.write(str(pos1))	
				namelist.write('\n')
		f.close()
namelist.close()
