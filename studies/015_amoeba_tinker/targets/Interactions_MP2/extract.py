#!/usr/bin/env python

import re
from forcebalance.nifty import isfloat
from forcebalance.molecule import *
from numpy import *

dashes = 0
readxyz = 0
outxyz = []
oxygens = []
hydrogens = []
fnms = []
for line in open("wn_mp2_fc_avtz.coo").readlines():
    T = '_'.join(re.sub("[^A-Za-z0-9 ]","",line).split()).lower()
    s = line.split()
    if list(set(line.strip())) == ['-']:
        dashes += 1
    elif dashes%2 == 1:
        comment = line.strip()
        outfnm = T
    if len(s) == 4 and s[0] in ['O','H','o','h'] and isfloat(s[1]) and isfloat(s[2]) and isfloat(s[3]):
        readxyz = 1
        #outxyz.append(format_xyz_coord(s[0].upper(),[float(s[1]),float(s[2]),float(s[3])]))
        if s[0] in ['O','o']:
            oxygens.append(array([float(s[1]),float(s[2]),float(s[3])]))
        else:
            hydrogens.append(array([float(s[1]),float(s[2]),float(s[3])]))
    elif readxyz:
        for o in oxygens:
            nh = 0
            outxyz.append(format_xyz_coord('O',o))
            for h in hydrogens:
                if nh > 2:
                    print "Crap!"
                if linalg.norm(o-h) < 1.2: # Cutoff is 1.2 Angstrom
                    outxyz.append(format_xyz_coord('H',h))
                    #hydrogens.remove(h)
                    nh += 1
        if outfnm in fnms:
            print "Crap", outfnm
        fnms.append(outfnm)
        outxyz = ["%i" % len(outxyz), comment] + outxyz
        with open("%s.xyz" % outfnm,'w') as f: f.writelines([line + "\n" for line in outxyz])
        outxyz = []
        oxygens = []
        hydrogens = []
        readxyz = 0

if outxyz != []:
    with open("%s.xyz" % outfnm,'w') as f: f.writelines([line + "\n" for line in outxyz])
