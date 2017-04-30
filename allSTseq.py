#!usr/bin/python
def createSTseqdict(gene):
	filename = gene + '.fasta'
	genefile = open(filename)
	seqdict = dict()
	key = 'key'
	seq = ''
	for line in genefile:
		if line[0]=='>':
			seqdict[key] = seq
			key = line[line.rfind('_')+1:-1]
			seq = ''
		else:
			seq = seq + line.rstrip()
	return seqdict
STlst = open('STsorted.file')
STlist = []
genelist = ['abcZ', 'adk', 'aroE','fumC', 'gdh','pdhC', 'pgm']
for line in STlst:
	tmp = line.split()
	if tmp[-1].isdigit():
		STnum = tmp[-1]
		if STnum not in STlist:
			STlist.append(STnum)
STlst.close()
STdict = dict()
STprofile = open('bigsdb.file')
for line in STprofile:
	tmp = line.split()
	STdict[tmp[0]] = list(tmp[1:8])
STprofile.close()
outputfile = open('allSTseq.fasta', 'w')
for i in STlist:
	STtmp = STdict[i]
	STname = '>ST_' + str(i)+ '\n'
	seq = ''
	for j in range(0, len(STtmp)):
		genedict = createSTseqdict(genelist[j])
		seq = seq + genedict[STtmp[j]]
	outputfile.write(STname)
	outputfile.write(seq)
	outputfile.write('\n')
outputfile.close()

