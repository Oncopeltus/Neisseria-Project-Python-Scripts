#!usr/bin/python/

seqfile = open('allunique.fasta.muscle')
outputfile = open("AEEFnew.fasta", 'w')
lines = seqfile.readlines()
line1 = lines[32]
line2 = lines[33].replace('-', 'N')
outputfile.write(line1)
outputfile.write(line2)
seqfile.close()
outputfile.close()
