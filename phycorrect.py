#!/usr/bin/python
import os
outputfile = open('all.FhuE_dnaE.phy','w')
alignfile = open('all.FhuE_dnaE.sp')
align = alignfile.readlines()
for line in align:
	tmpline = line.split()
	if len(tmpline) > 2:
		numline1 = '>' + tmpline[0] + '_' + tmpline[1] + '\n'
		numline2 = str(tmpline[2]) +'\n'
		outputfile.write(numline1)
		outputfile.write(numline2)
	elif tmpline[0][8] == '_':
		seqline1 = '>' + tmpline[0][:8] + '\n'
		seqline2 = tmpline[1] + '\n'
		outputfile.write(seqline1)
		outputfile.write(seqline2)
	else:
		seqline1 = '>' + tmpline[0][:12] + '\n'
		seqline2 = tmpline[1] + '\n'
		outputfile.write(seqline1)
		outputfile.write(seqline2)

	
	
outputfile.close()
alignfile.close()
