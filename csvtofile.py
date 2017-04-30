#!/usr/bin/python
csvfile = open('STnumbers.csv')
outputfile = open('STsorted.file', 'w')
csvread = csvfile.readlines()
for line in csvread:
	tmp = line.strip()
	if len(tmp) > 12 and tmp[12] == ',':
		newline = tmp[:12] + '\t' + tmp[13:]
	elif tmp[8] == ',':
		newline = tmp[:8] + '\t' + tmp[9:]
	outputfile.write(newline)
	outputfile.write('\n')
outputfile.close()
csvfile.close()
