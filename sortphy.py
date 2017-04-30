#!/usr/bin/python
import os
outputfile = open('allsorted_cas_dnaE.muscle','w')
alignfile = open('all.fasta.muscle')
sortfile = open('STsorted.file')
align = alignfile.readlines()
sortlist = sortfile.readlines()
seqdic = dict()
for i in range(len(align)):
	if align[i][0] =='>':
		key = align[i].strip()
		seqdic[key[:-1]] = align[i+1].strip()
for line in sortlist:
	linecon = line.split()
	index = '>' + linecon[0]
	if index in seqdic:
		outputindex = index + '_' + linecon[1]+ '\n'
		outputfile.write(outputindex)
		outputfile.write(seqdic[index])
		outputfile.write('\n')
	
	
outputfile.close()
alignfile.close()
sortfile.close()
