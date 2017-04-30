#!/usr/bin/python
import os
def rev_comp(seq):
        """This function returns the reverse and compliment sequence of a given sequence"""
	revseq = seq[::-1]
	comp = {'a': 't', 't':'a', 'c':'g','g':'c'}
	revcompseq = ''
	for n in revseq:
		revcompseq = revcompseq + comp[n]
	return revcompseq

namefile = open('names.txt')
names = namefile.readlines()
for line in names:
	itemset = line.split()
	name = str(itemset[0])
	contig = '>' + str(itemset[1])
	pos1 = int(itemset[2])
	pos2 = int(itemset[3])
	filename = name + '.fasta'
	outputname = name + '_FhuE_dnaE.fasta'
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
	if pos2 > pos1:
		extractseq = wholeseq[pos1-1:pos2]
	else: 
		extractseq = wholeseq[pos2-1:pos1]
		extractseq = rev_comp(extractseq)
	outputfile.write(extractseq)
	outputfile.write('\n')
	outputfile.close()
	seqfile.close()

namefile.close()
