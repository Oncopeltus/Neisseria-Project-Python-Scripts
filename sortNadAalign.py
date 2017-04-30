#!/usr/bin/python
import os
outputfile = open('all_NadA_sortedmod.muscle','w')
alignfile = open('all_NadA_mod.fasta.muscle')
sortfile = open('STsorted.file')
align = alignfile.readlines()
sortlist = sortfile.readlines()
seqdic = dict()
namelist = []
for i in range(len(align)):
	if align[i][0] =='>':
		name = align[i].strip()[1:-9]
		seqdic[name] = align[i+1].strip()
		namelist.append(name)
for line in sortlist:
	tmp = line.split()
	if tmp[0] in namelist:
		newname = '>' + tmp[0]+ '_' + tmp[1] + '\n'
		outputfile.write(newname)
		outputfile.write(seqdic[tmp[0]])
		outputfile.write('\n')
	
	
outputfile.close()
alignfile.close()
sortfile.close()
