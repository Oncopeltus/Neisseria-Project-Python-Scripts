#!/usr/bin/python
import os
def rev_comp(seq):
	revseq = seq[::-1]
	comp = {'a': 'T', 't':'A', 'c':'G','g':'C'}
	for i in comp:
		revseq = revseq.replace(i, comp[i])
	revseq = revseq.lower()
	return revseq

namefile = open('glnB_CeuD.file')
names = namefile.readlines()
for line in names:
	itemset = line.split()
	name = str(itemset[0])
	contig = '>' + str(itemset[1])
	glnBpos1 = int(itemset[2])
	glnBpos2 = int(itemset[3])
	CeuDpos1 = int(itemset[4])
	CeuDpos2 = int(itemset[5])
	filename = name + '.fasta'
	outputname = name + '_glnB+CeuD.fasta'
	outputfile = open(outputname, 'w')
	line1 = '>' + name
	outputfile.write(line1)
	outputfile.write('\n')
	seqfile = open(filename)
	a = seqfile.readlines()
	i = 0
	while a[i].strip() != contig:
		i += 2	
	wholeseq = a[i + 1].strip()
	if glnBpos2 > glnBpos1:
		extractseqglnB = wholeseq[glnBpos1-1:glnBpos2]
	else: 
		extractseqglnB = wholeseq[glnBpos2-1:glnBpos1]
		extractseqglnB = rev_comp(extractseqglnB)
	if CeuDpos2 > CeuDpos1:
                extractseqCeuD = wholeseq[CeuDpos1-1:CeuDpos2]
        else:
                extractseqCeuD = wholeseq[CeuDpos2-1:CeuDpos1]
                extractseqCeuD = rev_comp(extractseqCeuD)

	outputfile.write(extractseqglnB)
	outputfile.write('__')
	outputfile.write(extractseqCeuD)
	outputfile.write('\n')
	outputfile.close()
	seqfile.close()

namefile.close()
