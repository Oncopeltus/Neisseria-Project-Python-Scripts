#!/usr/bin/python
seqfile = open('all.fasta')
outputfile = open('allunique.fasta','w')
seq = seqfile.readlines()
uniqseq = list()
uniqseq.append(seq[1])
outputfile.write(seq[0])
outputfile.write(seq[1].upper())
for i in range(2,len(seq), 2):
	if seq[i+1] not in uniqseq:
		uniqseq.append(seq[i+1])
		outputfile.write(seq[i])
		outputfile.write(seq[i+1].upper())
seqfile.close()
outputfile.close()

			
