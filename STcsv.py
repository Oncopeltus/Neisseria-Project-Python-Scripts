#!/usr/bin/python
STlst = open('STnumbers.file')
outputfile = open('STnumbers.csv', 'w')
STnum = STlst.readlines()
for line in STnum:
	tmp = line.split()
	outputfile.write(tmp[0])
	outputfile.write('\t')
	outputfile.write(tmp[-1])
	outputfile.write('\n')

STlst.close()
outputfile.close()
