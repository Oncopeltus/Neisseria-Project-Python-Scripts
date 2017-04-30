#/usr/bin/python
import os
namelist = open('names.txt','w')
for filename in os.listdir('/home/jinl/blastoutput1'):
	if filename.endswith('.file'):
		f = open(filename)
		result = f.readlines()
		if len(result) > 1:
			Gph = result[0].split()
			cas2 = result[1].split()
			if Gph[2] == cas2[2]:
				name = str(filename)
				namelist.write(name[:-20])
				namelist.write(' ')
				namelist.write(str(Gph[1]))
				namelist.write(' ')
				positions = {int(Gph[6]),int(Gph[7]),int(cas2[6]),int(cas2[7])}
				a = max(positions)
				b = min(positions)
				positions.remove(a)
				positions.remove(b)
				position1 = min(positions)
				namelist.write(str(position1))
				namelist.write(' ')
				position2 = max(positions)
				namelist.write(str(position2))
				namelist.write('\n')
		f.close()
namelist.close()
