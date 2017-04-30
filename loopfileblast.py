#/usr/bin/python
import os
namelist = open('namelist.txt','w')
gphonly = open('gphonly.txt','w')
dnaEonly = open ('dnaEonly.txt','w')
for filename in os.listdir('/home/jinl/blastoutput'):
	if filename.endswith('.file'):
		f = open(filename)
		result = f.readlines()
		if len(result) > 1:
			gph = result[0].split()
			dnaE = result[1].split()
			if gph[1] == dnaE[1]:
				name = str(filename)
				namelist.write(name[:-11])
				namelist.write('\n')
		elif len(result) == 1:
			l = result[0].split()
			if l[0]== '>gph':
				gphname = str(filename)
				gphonly.write(gphname[:-11])
			elif l[0] == '>dnaE':
				dnaEname = str(filename)
				dnaEonly.write(dnaEname[:-11])
				dnaEonly.write('\n')
		f.close()
namelist.close()
gphonly.close()
dnaEonly.close()
