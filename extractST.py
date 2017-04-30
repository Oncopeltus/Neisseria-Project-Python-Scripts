#!/usr/bin/python
import os
namelist = open('STlist.file','w')
namelist.write('Name\tabcZ\tadk\taroE\tfumC\tgdh\tpdhC\tpgm\n')
abcZfile = open('abcZ.txt')
abcZ = abcZfile.readlines()
adkfile = open('adk.txt')
adk = adkfile.readlines()
aroEfile = open('aroE.txt')
aroE = aroEfile.readlines()
fumCfile = open('fumC.txt')
fumC = fumCfile.readlines()
gdhfile = open('gdh.txt')
gdh = gdhfile.readlines()
pdhCfile = open('pdhC.txt')
pdhC = pdhCfile.readlines()
pgmfile = open('pgm.txt')
pgm = pgmfile.readlines()
i = 0
while i < len(abcZ):
	abcZnum = abcZ[i].split()
	adknum = adk[i].split()
	aroEnum = aroE[i].split()
	fumCnum = fumC[i].split()
	gdhnum = gdh[i].split()
	pdhCnum = pdhC[i].split()
	pgmnum = pgm[i].split()
	namelist.write(abcZnum[0])
	namelist.write('\t')
	tmplist = [abcZnum[-1], adknum[-1], aroEnum[-1], fumCnum[-1], gdhnum[-1], pdhCnum[-1], pgmnum[-1]]
	for j in tmplist:
		if len(j)< 5:
			namelist.write(j)
		else:
			namelist.write('NA')
		namelist.write('\t')
	namelist.write('\n')
	i += 1
namelist.close()
abcZfile.close()
adkfile.close()
aroEfile.close()
fumCfile.close()
gdhfile.close()
pdhCfile.close()
pgmfile.close()
