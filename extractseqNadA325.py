#/usr/bin/python
import os
def rev_comp(seq):
	revseq = seq[::-1]
	comp = {'a': 'T', 't':'A', 'c':'G','g':'C'}
	for i in comp:
		revseq = revseq.replace(i, comp[i])
	revseq = revseq.lower()
	return revseq

namefile = open('NadAlist.txt')
names = namefile.readlines()
for line in names:
	itemset = line.split()
	name = str(itemset[0])[:-9]
	pos1 = int(itemset[1])
	pos2 = int(itemset[2])
	filename = name + '_glnB_CeuD.fasta'
	outputname = name + '_NadA325.fasta'
	outputfile = open(outputname, 'w')
	line1 = '>' + itemset[0]
	outputfile.write(line1)
	outputfile.write('\n')
	seqfile = open(filename)
	a = seqfile.readlines()
	wholeseq = a[1].strip()
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
