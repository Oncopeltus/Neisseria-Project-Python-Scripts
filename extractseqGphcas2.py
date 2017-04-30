#/usr/bin/python
import os
namefile = open('names.txt')
names = namefile.readlines()
for line in names:
	itemset = line.split()
	name = str(itemset[0])
	pos1 = int(itemset[2])
	pos2 = int(itemset[3]) + 1
	filename = name + '_Gph_dnaE.fasta'
	outputname = name + '_Gph_cas2.fasta'
	outputfile = open(outputname, 'w')
	line1 = '>' + name + ' ' + itemset[2] + ' ' + itemset[3]
	outputfile.write(line1)
	outputfile.write('\n')
	seqfile = open(filename)
	a = seqfile.readlines()
	wholeseq = a[1].strip()
	extractseq = wholeseq[pos1:pos2]
	outputfile.write(extractseq)
	outputfile.close()
	seqfile.close()

namefile.close()
