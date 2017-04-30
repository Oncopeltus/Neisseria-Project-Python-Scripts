#!usr/bin/python
STlst = open('STsorted.file')
STlist = []
for line in STlst:
	tmp = line.split()
	if tmp[-1].isdigit():
		STnum = int(tmp[-1])
		if STnum not in STlist:
			STlist.append(STnum)
print STlist
print len(STlist)
STlst.close()
