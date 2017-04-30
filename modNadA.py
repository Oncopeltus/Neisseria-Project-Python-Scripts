#!/usr/bin/python/

alignfile = open('all_NadA_sortedmod.muscle')
NadAfile = open('NadA.txt')
outputfile = open('all_NadA_modsorted.phy', 'w')
NadAprofile = NadAfile.readlines()
align = alignfile.readlines()
NadAdict = dict()
for line in NadAprofile:
	tmp = line.split()
	NadAdict[tmp[0][:-9]] = '_N'+tmp[0][-3:]
for line in align:
	if line[0] == '>':
		i = line.find('_')
		tmp = line[1:i]
		nameline = line.strip() + NadAdict[tmp] + '\n'
		outputfile.write(nameline)
	else:
		outputfile.write(line)
alignfile.close()
NadAfile.close()
outputfile.close()
