#!/usr/bin/python/

alignfile = open('allglnBCeuDwST.fasta.muscle')
NadAfile = open('NadA.txt')
outputfile = open('allglnBCeuDmod.phy', 'w')
NadAprofile = NadAfile.readlines()
align = alignfile.readlines()
NadAdict = dict()
for line in NadAprofile:
	tmp = line.split()
	NadAdict[tmp[0][:-9]] = '_N'+tmp[0][-3:]
for line in align:
	if line[0] == '>':
		NadA293 = ['APTO', 'CMXD', 'CMYD', 'ALYA']
		if line[1:5] in NadA293:
			nameline = line.strip() + '_N' + '293' + '\n'
		elif line[1:5] == 'AEQI':
			nameline = line.strip() + '_N' + '330' + '\n'
		elif line[1:5] == 'FEZZ' or line[0][1:5] == 'FESM':
			nameline = line.strip() + '_N' + '372' + '\n'
		else:
			i = line.find('_')
			if i == 5:
				tmp = line[1:i] + '00000000'
			else:
				tmp = line[1:i]
			if tmp in NadAdict:
				nameline = line.strip() + NadAdict[tmp] + '\n'
			else:
				nameline = line
		outputfile.write(nameline)
	else:
		outputfile.write(line)
alignfile.close()
NadAfile.close()
outputfile.close()
