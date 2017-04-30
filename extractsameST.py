#!/usr/bin/python
alignfile = open('allsorted_cas_dnaE.muscle')
outputfile = open('ST4821_cas.file', 'w')
align = alignfile.readlines()
for i in range(len(align)):
	if align[i][0] == '>':
		a = align[i].strip()
		b = a.find('_')
		STnum = int(a[b+1:])
		if STnum == 4821 :
			outputfile.write(align[i])
			cas = align[i + 1][:4605]
			outputfile.write(cas)
			outputfile.write('\n')
alignfile.close()
outputfile.close()
			
