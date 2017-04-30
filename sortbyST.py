#!/usr/bin/python
import os
outputfile = open('allsort.phy','w')
alignfile = open('all.newphy')
sortfile = open('allsort.csv')
align = alignfile.readlines()
sortlist = sortfile.readlines()
seqdic = dict()
for i in range(len(align)):
	if align[i][0] =='>':
		seqdic[align[i].strip()] = align[i+1].strip()
for j in range(8):
	outputfile.write(align[j])
for line in sortlist:
	tmp = line.strip()
	outputfile.write(line)
	outputfile.write(seqdic[tmp])
	outputfile.write('\n')
	
	
outputfile.close()
alignfile.close()
sortfile.close()
