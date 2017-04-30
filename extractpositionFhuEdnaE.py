#!/usr/bin/python
import os
namelist = open('names.txt','w')
for filename in os.listdir('/home/jinl/NMBblastoutput'):
	if filename.endswith('.file'):
		f = open(filename)
		result = f.readlines()
		if len(result) > 1:
			FhuE = result[0].split()
			dnaE = result[1].split()
			if FhuE[1] == dnaE[1]:
				name = str(filename)
				namelist.write(name[:-11])
				namelist.write('\t')
				namelist.write(str(FhuE[1]))
				namelist.write('\t')
				positions = [int(FhuE[3]),int(FhuE[4]),int(dnaE[3]),int(dnaE[4])]
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
