#!/usr/bin/python/

treealignfile = open('allunique.sp')
outputfile = open('allunique.newsp', 'w')
a = treealignfile.readlines()
for line in a:
	if len(line)< 30:
		outputfile.write(line)
	elif len(line) > 30:
		split = '--'
		newline = line[0:6] + split + line[6:81] + split + line[81:87] + split + line[87:616] + split + line[616:622] + split + line[622:]
		outputfile.write(newline)

treealignfile.close()
outputfile.close()
