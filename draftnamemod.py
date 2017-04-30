#!/usr/bin/python/

MOD = '00000000'
def moddraftname(draftname, mod):
    draftname = draftname[0:4] + mod + '\n'
    return draftname
namefile = open("rawdraftname.csv")
newdraftname = open('draftname.file', 'w')
namelist = namefile.readlines()
for i in namelist:
	newdraftname.write(moddraftname(i,MOD))
namefile.close()
newdraftname.close()
