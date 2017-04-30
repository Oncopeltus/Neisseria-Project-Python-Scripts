#!usr/bin/python/

seqfile = open('all.fasta.muscle')
outputfile = open("ANSG.fasta", 'w')
line1 = seqfile.readline()
line2 = seqfile.readline()
line2 = line2.replace('-', 'N')
outputfile.write(line1)
outputfile.write(line2)
seqfile.close()
outputfile.close()
