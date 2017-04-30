#!/usr/bin/python/

def modname(rawname):
    mod = rawname[-11:-3] + '\n'
    return mod
namefile = open("rawname.csv")
newname = open('name.file', 'w')
namelist = namefile.readlines()
for i in namelist:
	newname.write(modname(i))
namefile.close()
newname.close()
